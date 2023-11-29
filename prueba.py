import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        #master.geometry("300x300")
        self.pantalla = tk.Entry(master, width=30, font=('Calibri',20))
        self.pantalla.grid(row=0, column=0, columnspan=4)


        botones=[
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0","C","=","+"
        ]
        fila=1
        columna=0
        for botonTexto in botones:
            if botonTexto == "=":
                tk.Button(master, text=botonTexto, width=5, command=self.calcular).grid(row=fila, column=columna)
            elif botonTexto == "C":
                tk.Button(master, text=botonTexto, width=5, command=self.borrar).grid(row=fila, column=columna)
            else:
                tk.Button(master, text=botonTexto, width=5, command=lambda boton=botonTexto: self.agregar_numero(boton)).grid(row=fila, column=columna)
            columna += 1
            #columna=columna+1
            if columna > 3:
                fila += 1
                columna = 0

    #Funcion para agregar numero y operadores a la pantalla
    def agregar_numero(self, numero):
        curret=self.pantalla.get()
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, curret+numero)
    
    def calcular(self):
        try:
            expresion=self.pantalla.get()
            resultado=eval(expresion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error")

    def borrar(self):
        self.pantalla.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk() #Creacion de la ventana
    calculadora = Calculadora(root)
    root.mainloop() #Bucle de la ventana