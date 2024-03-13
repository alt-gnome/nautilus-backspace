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


import os
import configparser
import gi

gi.require_version("Nautilus", "4.0")
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Nautilus, Gtk

config_dir = "/etc/nautilus_backspace/"
config_file = config_dir + "config"
user_config_dir = os.path.expanduser("~/.config/nautilus_backspace/")
user_config_file = user_config_dir + "config"


config = configparser.ConfigParser()

if os.path.exists(user_config_file):
    config.read(user_config_file)
elif os.path.exists(config_file):
    config.read(config_file)
else:
    config["DEFAULT"] = {
        "shortcut": "BackSpace"
    }
    os.makedirs(user_config_dir, exist_ok=True)
    with open(user_config_file, "w") as file:
        config.write(file)


shortcut = config.get("DEFAULT", "shortcut")

def back():
    app = Gtk.Application.get_default()
    if not app.get_actions_for_accel(shortcut):
        app.set_accels_for_action("win.up", [shortcut])

class Back(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def update_file_info(self, file):
        back()
        return None
