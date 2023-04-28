# window.py
#
# Copyright 2023 Francesco Caracciolo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio
from .layouts import LAYOUTS
from .layouts import COLORS
import os
import json
import subprocess

@Gtk.Template(resource_path='/moe/nyarchlinux/customize/window.ui')
class NyarchcustomizeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchcustomizeWindow'

    layoutbox = Gtk.Template.Child("layoutbox")
    applyButton = Gtk.Template.Child("applylayout")
    layout_amount = 6
    themingBox = Gtk.Template.Child("themingbox")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutgrid, themingpage = self.load_layouts()
        self.layoutbox.prepend(layoutgrid)
        self.themingBox.append(themingpage)
        self.checkboxes = []
        for i in range(self.layout_amount):  # To generalize and remove layout_amount
        	self.checkboxes.append(self.layoutbuilder.get_object("l" + str(i)))
        self.applyButton.connect("clicked", self.apply_layout)
        self.theming_page()

    def theming_page(self):
        r = self.execute_command("gsettings get org.gnome.shell enabled-extensions")
        print(r.replace("'", '"'))
        enabled_extensions = json.loads(r.replace("'", '"'))
        materialyou_switch = self.themingPageBuilder.get_object("materialyou_switch")
        blur_switch = self.themingPageBuilder.get_object("blur_switch")
        wobblywindows_switch = self.themingPageBuilder.get_object("wobblywindows_switch")
        magiclamp_switch = self.themingPageBuilder.get_object("magiclamp_switch")
        desktopcube_switch = self.themingPageBuilder.get_object("desktopcube_switch")
        systemtray_switch = self.themingPageBuilder.get_object("systemtray_switch")
        desktopicons_switch = self.themingPageBuilder.get_object("desktopicons_switch")
        backgroundlogo_switch = self.themingPageBuilder.get_object("backgroundlogo_switch")
        colorbox = self.themingPageBuilder.get_object("colorbox")
        self.build_colorbox(colorbox)
        if "material-you-theme@asubbiah.com" in enabled_extensions:
            materialyou_switch.set_active(True)
        materialyou_switch.connect('notify::active', self.toggle_materialyou)
        if "blur-my-shell@aunetx" in enabled_extensions:
            blur_switch.set_active(True)
        blur_switch.connect('notify::active', self.toggle_blur)
        if "compiz-windows-effect@hermes83.github.com" in enabled_extensions:
            wobblywindows_switch.set_active(True)
        wobblywindows_switch.connect('notify::active', self.toggle_wobbly)
        if "compiz-alike-magic-lamp-effect@hermes83.github.com" in enabled_extensions:
            magiclamp_switch.set_active(True)
        magiclamp_switch.connect('notify::active', self.toggle_magiclamp)
        if "desktop-cube@schneegans.github.com" in enabled_extensions:
            desktopcube_switch.set_active(True)
        desktopcube_switch.connect('notify::active', self.toggle_desktopcube)
        if "trayIconsReloaded@selfmade.pl" in enabled_extensions:
            systemtray_switch.set_active(True)
        systemtray_switch.connect('notify::active', self.toggle_trayicons)
        if "desktopicons-neo@darkdemon" in enabled_extensions:
            desktopicons_switch.set_active(True)
        desktopicons_switch.connect('notify::active', self.toggle_desktopicons)
        if "background-logo@fedorahosted.org" in enabled_extensions:
            backgroundlogo_switch.set_active(True)
        backgroundlogo_switch.connect('notify::active', self.toggle_backgroundlogo)

    def build_colorbox(self, colorbox):
        self.colorbuttons = {}
        current = self.get_current_color()
        for color in COLORS:
            button = Gtk.Button()
            button.set_css_classes([".cicular"])
            csss = Gtk.CssProvider();
            csss.load_from_data(bytes("button { background-color: "+ color +"; border-radius: 999px;}", "utf-8"))
            button.get_style_context().add_provider(csss, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
            if COLORS[color] == current:
                button.set_icon_name("object-select-symbolic")
            button.connect("clicked", self.colorbutton_clicked)
            self.colorbuttons[button] = color
            colorbox.append(button)
    def colorbutton_clicked(self, button):
        color = self.colorbuttons[button]
        self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/material-you-theme@asubbiah.com/schemas set org.gnome.shell.extensions.material-you-theme accent-color " + str(COLORS[color]))
        for cbutton in self.colorbuttons:
            cbutton.set_icon_name("")
        button.set_icon_name("object-select-symbolic")
    def apply_layout(self, info=None):
        choosen = self.get_enabled()
        actions = self.load_layouts_actions()
        for x in actions[choosen]["enable_extensions"]:
            self.set_extension(x, True)
        for x in actions[choosen]["disable_extensions"]:
            self.set_extension(x, False)
        for x in actions[choosen]["extra_commands"]:
            self.execute_command2(x)

    def get_enabled(self):
        i = 0
        for checkbox in self.checkboxes:
            if checkbox.get_active():
                return i
            i += 1

    def load_layouts_actions(self):
        return LAYOUTS

    def load_layouts(self):
    	self.layoutbuilder = Gtk.Builder.new_from_resource('/moe/nyarchlinux/customize/layoutgrid.ui')
    	self.themingPageBuilder = Gtk.Builder.new_from_resource('/moe/nyarchlinux/customize/theming.ui')
    	return self.layoutbuilder.get_object("gridcontent"), self.themingPageBuilder.get_object("themepage")

    def set_extension(self, uiid:str, enabled:bool):
    	if enabled:
    		arg = "enable"
    	else:
    		arg = "disable"
    	self.execute_command("gnome-extensions " + arg + " " + uiid)

    def execute_command(self, command):
        try:
        	    result = subprocess.check_output(['flatpak-spawn', '--host'] + command.split()).decode('utf-8')
        except Exception as e:
            return None
        return result
    def execute_command3(self, command):
        try:
        	    result = subprocess.check_output(['flatpak-spawn', '--host', 'bash', '-c', command]).decode('utf-8')
        	    print(result)
        except Exception as e:
            return None
        return result
    def get_current_color(self):
        self.execute_command3("cat ~/.local/share/gnome-shell/extensions/material-you-theme@asubbiah.com/schemas/gschemas.compiled")
        return int(self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/material-you-theme@asubbiah.com/schemas get org.gnome.shell.extensions.material-you-theme accent-color").replace("'", "").replace("\n", ""))

    def execute_command2(self, command):
        os.system("flatpak-spawn --host " + command)

    def toggle_materialyou(self, switch=False, active=None):
    	self.set_extension("material-you-theme@asubbiah.com", switch.get_active())
    def toggle_blur(self, switch=False, active=None):
    	self.set_extension("blur-my-shell@aunetx", switch.get_active())
    def toggle_wobbly(self, switch=False, active=None):
    	self.set_extension("compiz-windows-effect@hermes83.github.com", switch.get_active())
    def toggle_magiclamp(self, switch=False, active=None):
    	self.set_extension("compiz-alike-magic-lamp-effect@hermes83.github.com", switch.get_active())
    def toggle_desktopcube(self, switch=False, active=None):
    	self.set_extension("desktop-cube@schneegans.github.com", switch.get_active())
    def toggle_trayicons(self, switch=False, active=None):
    	self.set_extension("trayIconsReloaded@selfmade.pl", switch.get_active())
    def toggle_desktopicons(self, switch=False, active=None):
    	self.set_extension("desktopicons-neo@darkdemon", switch.get_active())
    def toggle_backgroundlogo(self, switch=False, active=None):
    	self.set_extension("background-logo@fedorahosted.org", switch.get_active())
