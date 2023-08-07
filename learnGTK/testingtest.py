# this is what the application looks like simply.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window): # my sub class
    def __init__(self):
        super().__init__(title="Calculator") # the base class
        self.set_border_width(10)

        # the header and title bar
        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Calculator"
        self.set_titlebar(headerBar)

        # this is my button and calling the function.
        self.button1 = Gtk.Button(label="1")
        self.button1.connect("clicked", self.clickedButton1)

        # creating the entry field
        self.entry = Gtk.Entry()
        self.entry.set_text("")

        # this creates the grid
        grid = Gtk.Grid()
        grid.add(self.button1)
        grid.attach_next_to(self.entry,self.button1,Gtk.PositionType.TOP,4,4)

        self.add(grid)

        # my function
    def clickedButton1(self, entry):
        self.entry.set_text("1")
        return self.entry


# creating the actual window, exit button, and running continuosly.
win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
