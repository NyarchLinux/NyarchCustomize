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

MAGIC_LAMP_UUID = "compiz-alike-magic-lamp-effect@hermes83.github.com"
BLUR_MY_SHELL_UUID = "blur-my-shell@aunetx"
WOBBLY_UUID = "compiz-windows-effect@hermes83.github.com"
CUBE_UUID = "desktop-cube@schneegans.github.com"
TRAYICONS_UUID = "trayIconsReloaded@selfmade.pl"
ICONS_UUID = "ding@rastersoft.com"
LOGO_UUID = "background-logo@fedorahosted.org"
MU_UUID = "material-you-colors@francescocaracciolo.github.io"
MU_SCHEMA = "org.gnome.shell.extensions.material-you-colors"

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
        enabled_extensions = json.loads(r.replace("'", '"'))
        self.materialyou_switch = self.themingPageBuilder.get_object("materialyou_switch")
        blur_switch = self.themingPageBuilder.get_object("blur_switch")
        wobblywindows_switch = self.themingPageBuilder.get_object("wobblywindows_switch")
        magiclamp_switch = self.themingPageBuilder.get_object("magiclamp_switch")
        desktopcube_switch = self.themingPageBuilder.get_object("desktopcube_switch")
        systemtray_switch = self.themingPageBuilder.get_object("systemtray_switch")
        desktopicons_switch = self.themingPageBuilder.get_object("desktopicons_switch")
        backgroundlogo_switch = self.themingPageBuilder.get_object("backgroundlogo_switch")
        colorbox = self.themingPageBuilder.get_object("colorbox")
        colortheming = self.themingPageBuilder.get_object("colortheming")
        self.colortheming_switch = self.themingPageBuilder.get_object("colortheming_switch")
        colortheming.add_action(self.colortheming_switch)
        self.build_colorbox(colorbox)
        self.materialyou_switches()
        self.materialyou_switch.connect('notify::active', self.toggle_materialyou)
        self.colortheming_switch.connect('notify::active', self.toggle_materialyou)
        if BLUR_MY_SHELL_UUID in enabled_extensions:
            blur_switch.set_active(True)
        blur_switch.connect('notify::active', self.toggle_blur)
        if WOBBLY_UUID in enabled_extensions:
            wobblywindows_switch.set_active(True)
        wobblywindows_switch.connect('notify::active', self.toggle_wobbly)
        if MAGIC_LAMP_UUID in enabled_extensions:
            magiclamp_switch.set_active(True)
        magiclamp_switch.connect('notify::active', self.toggle_magiclamp)
        if CUBE_UUID in enabled_extensions:
            desktopcube_switch.set_active(True)
        desktopcube_switch.connect('notify::active', self.toggle_desktopcube)
        if TRAYICONS_UUID in enabled_extensions:
            systemtray_switch.set_active(True)
        systemtray_switch.connect('notify::active', self.toggle_trayicons)
        if ICONS_UUID in enabled_extensions:
            desktopicons_switch.set_active(True)
        desktopicons_switch.connect('notify::active', self.toggle_desktopicons)
        if LOGO_UUID in enabled_extensions:
            backgroundlogo_switch.set_active(True)
        backgroundlogo_switch.connect('notify::active', self.toggle_backgroundlogo)

    def materialyou_switches(self):
        r = self.execute_command("gsettings get org.gnome.shell enabled-extensions")
        enabled_extensions = json.loads(r.replace("'", '"'))
        acen = self.accent_colors_enabled()
        print(acen)
        if MU_UUID in enabled_extensions:
            if not acen:
                self.materialyou_switch.set_active(True)
            else:
                self.colortheming_switch.set_active(True)
        else:
            self.materialyou_switch.set_active(False)
            self.colortheming_switch.set_active(False)

    def build_colorbox(self, colorbox):
        self.colorbuttons = {}
        current = self.get_current_color()
        for color in COLORS:
            button = Gtk.Button()
            button.set_css_classes([".cicular"])
            csss = Gtk.CssProvider();
            csss.load_from_data("button { background-color: "+ color +"; border-radius: 999px;}", -1)
            button.get_style_context().add_provider(csss, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
            if COLORS[color] == current:
                button.set_icon_name("object-select-symbolic")
            button.connect("clicked", self.colorbutton_clicked)
            self.colorbuttons[button] = color
            colorbox.append(button)

    def colorbutton_clicked(self, button):
        color = self.colorbuttons[button]
        self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + MU_UUID + "/schemas set "+ MU_SCHEMA + " accent-color " + str(COLORS[color]))
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
        except Exception as e:
            return None
        return result

    def get_current_color(self):
        return int(self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + MU_UUID + "/schemas get " + MU_SCHEMA + " accent-color").replace("'", "").replace("\n", ""))

    def accent_colors_enabled(self):
        r = self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + MU_UUID + "/schemas get " + MU_SCHEMA + " enable-accent-colors").replace("'", "").replace("\n", "")
        if r == "true":
            return True
        else:
            return False
    def execute_command2(self, command):
        os.system("flatpak-spawn --host " + command)

    def toggle_materialyou(self, switch=False, active=None):
        mu = self.materialyou_switch.get_active()
        ct = self.colortheming_switch.get_active()
        if ct and mu:
            if switch == self.materialyou_switch:
                ct = False
                self.colortheming_switch.set_active(False)
            elif switch == self.colortheming_switch:
                mu = False
                self.materialyou_switch.set_active(False)
        if ct or mu:
            self.set_extension(MU_UUID, True)
        if not ct and not mu:
            self.set_extension(MU_UUID, False)
        if ct and not mu:
            self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/"+ MU_UUID +"/schemas set "+ MU_SCHEMA + " enable-accent-colors true")
        if mu and not ct:
            self.execute_command3("gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + MU_UUID + "/schemas set "+ MU_SCHEMA + " enable-accent-colors false")


    def toggle_blur(self, switch=False, active=None):
    	self.set_extension(BLUR_MY_SHELL_UUID, switch.get_active())
    def toggle_wobbly(self, switch=False, active=None):
    	self.set_extension(WOBBLY_UUID, switch.get_active())
    def toggle_magiclamp(self, switch=False, active=None):
    	self.set_extension(MAGIC_LAMP_UUID, switch.get_active())
    def toggle_desktopcube(self, switch=False, active=None):
    	self.set_extension(CUBE_UUID, switch.get_active())
    def toggle_trayicons(self, switch=False, active=None):
    	self.set_extension(TRAYICONS_UUID, switch.get_active())
    def toggle_desktopicons(self, switch=False, active=None):
    	self.set_extension(ICONS_UUID, switch.get_active())
    def toggle_backgroundlogo(self, switch=False, active=None):
    	self.set_extension(LOGO_UUID, switch.get_active())
