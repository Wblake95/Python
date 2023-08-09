import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calculator")
        self.set_border_width(10)

        # Header bar and exit button
        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Calculator"
        self.set_titlebar(headerBar)

        # All the buttons
        # Numbers
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

        # Zero 
        self.button0 = Gtk.Button(label="0")
        self.button0.connect("clicked", self.clickedButton0)
        self.buttonSign = Gtk.Button(label="-/+")
        # self.buttonSign.connect("clicked", self.clickedButton9)

        # Oporator buttons
        self.buttonMultiply = Gtk.Button(label="x")
        self.buttonMultiply.connect("clicked", self.clickedMultiply)
        self.buttonDivide = Gtk.Button(label="/")
        self.buttonDivide.connect("clicked", self.clickedDivide)
        self.buttonAdd = Gtk.Button(label="+")
        self.buttonAdd.connect("clicked", self.clickedAdd)
        self.buttonSubtract = Gtk.Button(label="-")
        self.buttonSubtract.connect("clicked", self.clickedSubtract)
        self.buttonEnter = Gtk.Button(label="=")
        # self.buttonEnter.connect("clicked", self.clickedEnter)
        self.buttonClear = Gtk.Button(label="c")
        self.buttonClear.connect("clicked", self.clickedClear)

        # Entry field
        self.entry = Gtk.Entry()
        self.entry.set_text("")

        # Organizing the application buttons and entry field
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
        grid.attach(self.buttonEnter,2,4,2,1)
        grid.attach(self.buttonClear,0,4,2,1)

        self.add(grid)

    # logic of buttons
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

    def signCheck(self, text):
        check = ["x","/","+","-"]
        checkSign = self.entry.get_text()
        if checkSign[-1] in check:
            return False
        else:
            return True

    def clickedMultiply(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text): text += "x"
        self.entry.set_text(text)
    def clickedDivide(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text): text += "/"
        self.entry.set_text(text)
    def clickedAdd(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text): text += "+"
        self.entry.set_text(text)
    def clickedSubtract(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text): text += "-"
        self.entry.set_text(text)
    # def clickedEnter(self):
    def clickedClear(self, entry):
        self.entry.set_text("")

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
