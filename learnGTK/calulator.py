import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calculator")
        self.set_border_width(10)

        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Calculator"
        self.set_titlebar(headerBar)

        self.button1 = Gtk.Button(label="1")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.button2 = Gtk.Button(label="2")
        # self.button2.connect("clicked", self.on_button2_clicked)
        self.button3 = Gtk.Button(label="3")
        # self.button3.connect("clicked", self.on_button3_clicked)
        self.button4 = Gtk.Button(label="4")
        # self.button4.connect("clicked", self.on_button4_clicked)
        self.button5 = Gtk.Button(label="5")
        # self.button5.connect("clicked", self.on_button5_clicked)
        self.button6 = Gtk.Button(label="6")
        # self.button6.connect("clicked", self.on_button6_clicked)
        self.button7 = Gtk.Button(label="7")
        # self.button7.connect("clicked", self.on_button7_clicked)
        self.button8 = Gtk.Button(label="8")
        # self.button8.connect("clicked", self.on_button8_clicked)
        self.button9 = Gtk.Button(label="9")
        # self.button9.connect("clicked", self.on_button9_clicked)

        self.button0 = Gtk.Button(label="0")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.buttonSign = Gtk.Button(label="-/+")
        # self.button1.connect("clicked", self.on_button1_clicked)

        self.buttonMultiply = Gtk.Button(label="x")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.buttonDivide = Gtk.Button(label="/")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.buttonAdd = Gtk.Button(label="+")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.buttonSubtract = Gtk.Button(label="-")
        # self.button1.connect("clicked", self.on_button1_clicked)
        self.buttonEnter = Gtk.Button(label="=")
        # self.button1.connect("clicked", self.on_button1_clicked)

        text = ""
        resultBox = Gtk.Label(label=text,xalign=0)
        listBox = Gtk.ListBox()
        listBox.add(resultBox)

        grid = Gtk.Grid()
        grid.add(self.button1)
        grid.attach_next_to(listBox,self.button1,Gtk.PositionType.TOP,4,4)
        grid.attach(self.button2,1,0,1,1)
        grid.attach(self.button3,2,0,1,1)
        grid.attach(self.button4,0,1,1,1)
        grid.attach(self.button5,1,1,1,1)
        grid.attach(self.button6,2,1,1,1)
        grid.attach(self.button7,0,2,1,1)
        grid.attach(self.button8,1,2,1,1)
        grid.attach(self.button9,2,2,1,1)

        grid.attach(self.button0,0,3,2,1)
        grid.attach_next_to(self.buttonSign,self.button0,Gtk.PositionType.RIGHT,1,1)

        grid.attach(self.buttonMultiply,3,0,1,1)
        grid.attach(self.buttonDivide,3,1,1,1)
        grid.attach(self.buttonAdd,3,2,1,1)
        grid.attach(self.buttonSubtract,3,3,1,1)
        grid.attach(self.buttonEnter,0,4,4,1)

        self.add(grid)

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
