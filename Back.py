import os
import configparser
import gi

gi.require_version("Nautilus", "4.0")
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Nautilus, Gtk

path = os.path.expanduser("~/.config/nautilus_backspace/")
os.makedirs(path, exist_ok=True)

config_file = path + "config"
config = configparser.ConfigParser()

if os.path.exists(config_file):
    config.read(config_file)
else:
    config["DEFAULT"] = {
        "shortcut": "BackSpace"
    }
    with open(config_file, "w") as file:
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
