import gi

gi.require_version("Nautilus", "4.0")
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Nautilus, Gtk


def back():
    app = Gtk.Application.get_default()
    if not app.get_actions_for_accel("BackSpace"):
        app.set_accels_for_action("win.up", ["BackSpace"])


class BackspaceBack(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def update_file_info(self, file):
        back()
        return None
