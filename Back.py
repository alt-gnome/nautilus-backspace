# Copyright 2024 Fiersik Kouji
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

# Version: 0.6.0

import gi

gi.require_version("Nautilus", "4.1")
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Nautilus, Gtk, Gio

settings = Gio.Settings(schema="io.github.alt-gnome-team.nautilus-backspace")

shortcut = settings.get_string("back")

def back():
    app = Gtk.Application.get_default()
    if not app.get_actions_for_accel(shortcut):
        app.set_accels_for_action("slot.up", [shortcut])

class Back(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def update_file_info(self, file):
        back()
        return None
