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
        button1 = Gtk.Button(label="1")
        button1.connect("clicked", self.clickedButton1)
        button2 = Gtk.Button(label="2")
        button2.connect("clicked", self.clickedButton2)
        button3 = Gtk.Button(label="3")
        button3.connect("clicked", self.clickedButton3)
        button4 = Gtk.Button(label="4")
        button4.connect("clicked", self.clickedButton4)
        button5 = Gtk.Button(label="5")
        button5.connect("clicked", self.clickedButton5)
        button6 = Gtk.Button(label="6")
        button6.connect("clicked", self.clickedButton6)
        button7 = Gtk.Button(label="7")
        button7.connect("clicked", self.clickedButton7)
        button8 = Gtk.Button(label="8")
        button8.connect("clicked", self.clickedButton8)
        button9 = Gtk.Button(label="9")
        button9.connect("clicked", self.clickedButton9)

        # Zero and sign
        button0 = Gtk.Button(label="0")
        button0.connect("clicked", self.clickedButton0)
        buttonSign = Gtk.Button(label="-/+")
        # self.buttonSign.connect("clicked", self.clickedSign)

        # Operator buttons
        buttonMultiply = Gtk.Button(label="*")
        buttonMultiply.connect("clicked", self.clickedMultiply)
        buttonDivide = Gtk.Button(label="/")
        buttonDivide.connect("clicked", self.clickedDivide)
        buttonAdd = Gtk.Button(label="+")
        buttonAdd.connect("clicked", self.clickedAdd)
        buttonSubtract = Gtk.Button(label="-")
        buttonSubtract.connect("clicked", self.clickedSubtract)

        # Enter and clear buttons
        buttonEnter = Gtk.Button(label="=")
        buttonEnter.connect("clicked", self.clickedEnter)
        buttonClear = Gtk.Button(label="c")
        buttonClear.connect("clicked", self.clickedClear)
        buttonPara = Gtk.Button(label="()")
        buttonPeriod = Gtk.Button(label=".")
        buttonPecent = Gtk.Button(label="%")

        # Entry field
        self.entry = Gtk.Entry()
        self.entry.set_text("")


        # Organizing the application buttons and entry field
        grid = Gtk.Grid()
        grid.add(buttonClear)
        grid.attach_next_to(self.entry, buttonClear, Gtk.PositionType.TOP,3,4)
        grid.attach(buttonPara,1,0,1,1)
        grid.attach(buttonPecent,2,0,1,1)
        grid.attach(button7,0,1,1,1)
        grid.attach(button8,1,1,1,1)
        grid.attach(button9,2,1,1,1)
        grid.attach(button4,0,2,1,1)
        grid.attach(button5,1,2,1,1)
        grid.attach(button6,2,2,1,1)
        grid.attach(button1,0,3,1,1)
        grid.attach(button2,1,3,1,1)
        grid.attach(button3,2,3,1,1)

        grid.attach(button0,1,4,1,1)
        grid.attach(buttonSign,0,4,1,1)
        grid.attach(buttonPeriod,2,4,1,1)

        grid.attach(buttonDivide,3,0,1,1)
        grid.attach(buttonMultiply,3,1,1,1)
        grid.attach(buttonSubtract,3,2,1,1)
        grid.attach(buttonAdd,3,3,1,1)
        grid.attach(buttonEnter,3,4,1,1)

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
        check = ["*","/","+","-"]
        checkSign = self.entry.get_text()
        if checkSign[-1] in check:
            return False
        else:
            return True

    def clickedMultiply(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text):
            text += "*"
        self.entry.set_text(text)
    def clickedDivide(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text):
            text += "/"
        self.entry.set_text(text)
    def clickedAdd(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text):
            text += "+"
        self.entry.set_text(text)
    def clickedSubtract(self, entry):
        text = self.entry.get_text()
        if self.signCheck(text):
            text += "-"
        self.entry.set_text(text)

    def clickedEnter(self, entry):
        # match self.operator:
        #     case "m": self.entry.set_text(self.a[0]*self.a[1])
        #     case "d": self.entry.set_text(self.a[0]/self.a[1])
        #     case "a": self.entry.set_text(self.a[0]+self.a[1])
        #     case "s": self.entry.set_text(self.a[0]-self.a[1])
        submit = self.entry.get_text()
        answer = eval(submit)
        self.entry.set_text(str(answer))
    def clickedClear(self, entry):
        self.entry.set_text("")
    # def clickedSign():

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
