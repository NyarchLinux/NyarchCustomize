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
import os
import json

@Gtk.Template(resource_path='/moe/nyarchlinux/customize/window.ui')
class NyarchcustomizeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchcustomizeWindow'

    layoutbox = Gtk.Template.Child("layoutbox")
    applyButton = Gtk.Template.Child("applylayout")
    layout_amount = 6

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutgrid = self.load_layouts()
        self.layoutbox.prepend(layoutgrid)
        self.checkboxes = []
        for i in range(self.layout_amount):
        	self.checkboxes.append(self.layoutbuilder.get_object("l" + str(i)))
        self.applyButton.connect("clicked", self.apply_layout)

    def apply_layout(self, info=None):
        choosen = self.get_enabled()
        actions = self.load_layouts_actions()
        for x in actions[choosen]["enable_extensions"]:
            self.set_extension(x, True)
        for x in actions[choosen]["disable_extensions"]:
            self.set_extension(x, False)
        for x in actions[choosen]["extra_commands"]:
            self.execute_command(x)

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
    	return self.layoutbuilder.get_object("gridcontent")

    def set_extension(self, uiid:str, enabled:bool):
    	if enabled:
    		arg = "enable"
    	else:
    		arg = "disable"
    	self.execute_command("gnome-extensions " + arg + " " + uiid)

    def execute_command(self, command):
        os.system("flatpak-spawn --host " + command)
