import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
winType = "destroy"

win = Gtk.Window() # instantiating the Gtk object
win.connect(winType, Gtk.main_quit) # this is creating an exit button
# win.button("text", )
label = Gtk.Label()
label.set_text(winType)
txt = label.get_text()
win.show_all()
Gtk.main()
