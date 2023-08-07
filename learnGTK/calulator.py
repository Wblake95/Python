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
        self.button2.connect("clicked", self.clickedButton2)
        self.button3 = Gtk.Button(label="3")
        self.button3.connect("clicked", self.clickedButton3)
        self.button4 = Gtk.Button(label="4")
        self.button4.connect("clicked", self.clickedButton4)
        self.button5 = Gtk.Button(label="5")
        self.button5.connect("clicked", self.clickedButton5)
        self.button6 = Gtk.Button(label="6")
        self.button6.connect("clicked", self.clickedButton6)
        self.button7 = Gtk.Button(label="7")
        self.button7.connect("clicked", self.clickedButton7)
        self.button8 = Gtk.Button(label="8")
        self.button8.connect("clicked", self.clickedButton8)
        self.button9 = Gtk.Button(label="9")
        self.button9.connect("clicked", self.clickedButton9)

        self.button0 = Gtk.Button(label="0")
        self.button0.connect("clicked", self.clickedButton0)
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

        # self.text = ""
        self.entry = Gtk.Entry()
        self.entry.set_text("")
        # self.entry.set_text(self.text)

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

    def clickedButton1(self, entry):
        text = self.entry.get_text()
        text += "1"
        self.entry.set_text(text)
    def clickedButton2 (self, entry):
        text = self.entry.get_text()
        text += "2"
        self.entry.set_text(text)
    def clickedButton3(self, entry):
        text = self.entry.get_text()
        text += "3"
        self.entry.set_text(text)
    def clickedButton4(self, entry):
        text = self.entry.get_text()
        text += "4"
        self.entry.set_text(text)
    def clickedButton5(self, entry):
        text = self.entry.get_text()
        text += "5"
        self.entry.set_text(text)
    def clickedButton6(self, entry):
        text = self.entry.get_text()
        text += "6"
        self.entry.set_text(text)
    def clickedButton7(self, entry):
        text = self.entry.get_text()
        text += "7"
        self.entry.set_text(text)
    def clickedButton8(self, entry):
        text = self.entry.get_text()
        text += "8"
        self.entry.set_text(text)
    def clickedButton9(self, entry):
        text = self.entry.get_text()
        text += "9"
        self.entry.set_text(text)
    def clickedButton0(self, entry):
        text = self.entry.get_text()
        text += "0"
        self.entry.set_text(text)
    # def buttonMultiply(self, entry)
    # def buttonDivide(self, entry)
    # def buttonAdd(self, entry)
    # def buttonEnter(self, entry)
    # def buttonSign(self, entry)

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
