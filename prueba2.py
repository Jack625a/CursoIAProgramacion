from tkinter import *
import math
class Calculator:

    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.var = StringVar()
        self.entry = Entry(self.frame, textvariable=self.var)
        self.entry.pack(side=TOP)

        self.btn7 = Button(self.frame, text="7", command=lambda: self.input(7))
        self.btn7.pack(side=LEFT)
        self.btn8 = Button(self.frame, text="8", command=lambda: self.input(8))
        self.btn8.pack(side=LEFT)
        self.btn9 = Button(self.frame, text="9", command=lambda: self.input(9))
        self.btn9.pack(side=LEFT)
        self.btn4 = Button(self.frame, text="4", command=lambda: self.input(4))
        self.btn4.pack(side=LEFT)
        self.btn5 = Button(self.frame, text="5", command=lambda: self.input(5))
        self.btn5.pack(side=LEFT)
        self.btn6 = Button(self.frame, text="6", command=lambda: self.input(6))
        self.btn6.pack(side=LEFT)
        self.btn1 = Button(self.frame, text="1", command=lambda: self.input(1))
        self.btn1.pack(side=LEFT)
        self.btn2 = Button(self.frame, text="2", command=lambda: self.input(2))
        self.btn2.pack(side=LEFT)
        self.btn3 = Button(self.frame, text="3", command=lambda: self.input(3))
        self.btn3.pack(side=LEFT)
        self.btn0 = Button(self.frame, text="0", command=lambda: self.input(0))
        self.btn0.pack(side=LEFT)

        self.btn_plus = Button(self.frame, text="+", command=lambda: self.input("+"))
        self.btn_plus.pack(side=LEFT)
        self.btn_minus = Button(self.frame, text="-", command=lambda: self.input("-"))
        self.btn_minus.pack(side=LEFT)
        self.btn_times = Button(self.frame, text="*", command=lambda: self.input("*"))
        self.btn_times.pack(side=LEFT)
        self.btn_divide = Button(self.frame, text="/", command=lambda: self.input("/"))
        self.btn_divide.pack(side=LEFT)

        self.btn_equals = Button(self.frame, text="=", command=self.calculate)
        self.btn_equals.pack(side=LEFT)

        self.btn_clear = Button(self.frame, text="C", command=self.clear)
        self.btn_clear.pack(side=RIGHT)

    def input(self, n):
        self.var.set(self.var.get() + str(n))

    def clear(self):
        self.var.set("")

    def calculate(self):
        try:
            result = eval(self.var.get())
            self.var.set(result)
        except Exception as e:
            self.var.set("Error")


if __name__ == "__main__":
    root = Tk()
    Calculator(root)
    root.mainloop()


#Funcion para area del triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2
#Funcion para area del circulo
def area_circulo(radio):
    return math.pi*radio*radio
#Funcion para area de la elipse
def area_elipse(a, b):
    return math.pi*(a*b)/4
    