import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calculator")
        # self.box = Gtk.Box(spacing=6)
        # self.add(self.box)

        button1 = Gtk.Button(label="1")
        # self.button1.connect("clicked", self.on_button1_clicked)
        button2 = Gtk.Button(label="2")
        button3 = Gtk.Button(label="3")
        button4 = Gtk.Button(label="4")
        button5 = Gtk.Button(label="5")
        button6 = Gtk.Button(label="6")
        button7 = Gtk.Button(label="7")
        button8 = Gtk.Button(label="8")
        button9 = Gtk.Button(label="9")

        button0 = Gtk.Button(label="0")
        buttonSign = Gtk.Button(label="-/+")

        buttonMultiply = Gtk.Button(label="x")
        buttonDivide = Gtk.Button(label="/")
        buttonAdd = Gtk.Button(label="+")
        buttonSubtract = Gtk.Button(label="-")
        buttonEnter = Gtk.Button(label="=")
        
        grid = Gtk.Grid()
        grid.add(button1)
        grid.attach(button2,1,0,1,1)
        grid.attach(button3,2,0,1,1)
        grid.attach(button4,0,1,1,1)
        grid.attach(button5,1,1,1,1)
        grid.attach(button6,2,1,1,1)
        grid.attach(button7,0,2,1,1)
        grid.attach(button8,1,2,1,1)
        grid.attach(button9,2,2,1,1)

        grid.attach(button0,0,3,2,1)
        grid.attach_next_to(buttonSign,button0,Gtk.PositionType.RIGHT,1,1)

        grid.attach(buttonMultiply,3,0,1,1)
        grid.attach(buttonDivide,3,1,1,1)
        grid.attach(buttonAdd,3,2,1,1)
        grid.attach(buttonSubtract,3,3,1,1)
        grid.attach(buttonEnter,0,4,4,1)

        self.add(grid)

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
