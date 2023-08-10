import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ToggleButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="ToggleButton Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button1 = Gtk.ToggleButton(label="Button 1")
        button1.set_active(True)
        button1.connect("toggled", self.on_button1, "1")
        hbox.pack_start(button1, True, True, 0)

        button2 = Gtk.ToggleButton(label="B_utton 2", use_underline=True)
        button2.connect("toggled", self.on_button2, "2")
        hbox.pack_start(button2, True, True, 0)

    def on_button1(self, button, name):
        if button.get_active():
            self.on_button2(button, "2")
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def on_button2(self, button, name):
        if button.get_active():
            self.on_button1(button, "1")
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

win = ToggleButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
