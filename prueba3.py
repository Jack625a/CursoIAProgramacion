from tkinter import Tk, Entry, Button

class Calculadora:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        
        self.caja_entrada = Entry(self.ventana)
        self.caja_entrada.grid(row=0, column=0, columnspan=4)
        
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        fila = 1
        columna = 0
        for boton in botones:
            Button(self.ventana, text=boton, width=5).grid(row=fila, column=columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
        
        self.ventana.mainloop()

calculadora = Calculadora()
