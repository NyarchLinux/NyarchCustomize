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

@Gtk.Template(resource_path='/moe/nyarchlinux/customize/window.ui')
class NyarchcustomizeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchcustomizeWindow'

    layoutbox = Gtk.Template.Child("layoutbox")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutgrid = self.load_layouts()
        self.layoutbox.append(layoutgrid)

    def load_layouts(self):
    	self.layoutbuilder = Gtk.Builder.new_from_resource('/moe/nyarchlinux/customize/layoutgrid.ui')
    	return self.layoutbuilder.get_object("gridcontent")
    	
