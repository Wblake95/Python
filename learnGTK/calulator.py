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
        self.button1.connect("clicked", self.clickedButton1)
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
        # self.button0.connect("clicked", self.on_button0_clicked)
        self.buttonSign = Gtk.Button(label="-/+")
        # self.buttonSign.connect("clicked", self.on_buttonSign_clicked)

        self.buttonMultiply = Gtk.Button(label="x")
        # self.buttonMultiply.connect("clicked", self.on_buttonMultiply_clicked)
        self.buttonDivide = Gtk.Button(label="/")
        # self.buttonDivide.connect("clicked", self.on_buttonDivide_clicked)
        self.buttonAdd = Gtk.Button(label="+")
        # self.buttonAdd.connect("clicked", self.on_buttonAdd_clicked)
        self.buttonSubtract = Gtk.Button(label="+")
        # self.buttonSubtract.connect("clicked", self.on_buttonSubtract_clicked)
        self.buttonEnter = Gtk.Button(label="=")
        # self.buttonEnter.connect("clicked", self.on_buttonEnter_clicked)

        self.entry = Gtk.Entry()
        self.entry.set_text("")

        grid = Gtk.Grid()
        grid.add(self.button1)
        grid.attach_next_to(self.entry,self.button1,Gtk.PositionType.TOP,4,4)
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

    def clickedButton1():
        self.entry.set_text("1")
    # def button2 ():
    #     return 2
    # def button3 ():
    #     return 4
    # def button5 ()
    #     return 5
    # def button6 ()
    #     return 6
    # def button7 ()
    #     return 7
    # def button8 ()
    #     return 8
    # def button9 ()
    #     return 9
    # def button0 ()
    #     return 0
    # def buttonMultiply ()
    # def buttonDivide ()
    # def buttonAdd ()
    # def buttonEnter ()
    # def buttonSign ()

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
