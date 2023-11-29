#CREAR UN CAJERO AUTOMATICO POR CONSOLA

class CajeroAutomatico:
    def __init__(self):
        self.usuarios={
            'usuario1':{
                'contraseña':'1234',
                'saldo':5200
            },
            'usuario2':{
                'contraseña':'89562',
               'saldo':10000
            }
        }
        self.usuarioActual=None

  
    #Metodo para el inicio  de sesion
    def iniciar_sesion(self,usuario,contraseña):
        if usuario in self.usuarios and self.usuarios[usuario]['contraseña']==contraseña:
            self.usuarioActual=usuario
            print(f"Bienvenido {usuario}")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
    
    #Metodo para ver saldo
    def ver_saldo(self):
        if self.usuarioActual:
            print(f"El saldo de {self.usuarioActual} es {self.usuarios[self.usuarioActual]['saldo']}")
        else:
            print("No se ha iniciado sesion")

    #Metodo para depositar
    def depositar(self,monto):
        if self.usuarioActual:
            self.usuarios[self.usuarioActual]['saldo']+=monto
            print(f"Se deposito {monto}Bs")
        else:
            print("Debe iniciar sesion para continuar")
    
    #Metodo para retirar
    def retirar(self, monto):
        if self.usuarioActual:
            saldo_actual = self.usuarios[self.usuarioActual]['saldo']
            if monto <= saldo_actual:
                self.usuarios[self.usuarioActual]['saldo'] -= monto
                print(f"Se retiró {monto}Bs")
            else:
                print("Saldo insuficiente")
        else:
            print("Debe iniciar sesión para continuar")
    def mostrar_menu(self):
        while True:
            print("Menú principal:")
            print("1. Ver saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_saldo()
            elif opcion == "2":
                monto = float(input("Ingrese el monto a depositar: "))
                self.depositar(monto)
            elif opcion == "3":
                monto = float(input("Ingrese el monto a retirar: "))
                self.retirar(monto)
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")


#Instancia del objeto de la clase CajeroAutomatico
cajero = CajeroAutomatico()
user=input("Ingrese su nombre de usuario: ")
password=input("Ingrese su contraseña: ")
#cajero.iniciar_sesion(user, password)
if cajero.iniciar_sesion(user,password):
    cajero.mostrar_menu()
else: 
    print("Error al iniciar sesión")


        

