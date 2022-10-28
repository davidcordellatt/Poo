import payment
import os
from car import Car
from user import User
from route import Route

if __name__ == '__main__':

    os.system('clear')
    user = input("\n" "Eres un usuario o un conductor?: ").strip().capitalize()

    # Camino del conductor
    if user == "Conductor":
                
        os.system('clear')
        print("\n" "Por favor llena el cuestionario: ")

        worker = Car(

        input("Nombre: ").strip().capitalize(),
        input("Apellido: ").strip().capitalize(),
        input("Cedula: ").strip(), 
        input("""6 caracteres entre letras y numeros UserId: """).strip().upper(), 
        input("Marca del coche: "),
        input("""7 caracteres entre letras y numeros
Placa del coche: """).strip().upper(), 
        int(input("Pasajeros: "))
        
        )
    

    # Camino del pasajero
    else:
        os.system('clear')
        print("\n" "Por favor llena el cuestionario: ")
        new_user = User(
        input("Nombre: ").strip().capitalize(),
        input("Apellido: ").strip().capitalize(),
        input("Cedula: ").strip(), 
        input("""6 caracteres entre letras y numeros 
UserId: """).strip().upper(), 
        input("Correo: "),
        input("""Contraseña: """).strip().upper()
        
        )

        #Ruta del viaje
        os.system('clear')
        print(f"\n{new_user.name}, Llena los datos del viaje: ")

        route = Route(
        input("Donde comienza el viaje: "),
        input("Donde finaliza el viaje: "),
        int(input("Acompañantes: "))
        
    
        )
        print("")
        cont = input("""
¿Desea continuar?: 
1.- Si
2.- No        
R: """).strip().lower()
        
        if cont == "1" or cont == "si":
            #Forma de pago
            os.system('clear')
            print("\n" "Por favor indica la forma de pago: ")
            method = input("""
1.- Paypal
2.- Tarjeta
3.- Efectivo
R: """).strip().capitalize()

            #Paypal
            if method == "Paypal" or method == "1":
                os.system('clear')
                print("\n" "Por favor indica los datos necesarios:")
                pay = payment.Paypal(
                input("""Repite el Id que colocaste anteriormente.
UserId: """).strip().upper(),
                input("""Ingresa el email del pago. 
UserId: """).strip().lower()
                )
            
                os.system('clear')
                print("Gracias por viajar con nosotros")
                
            #Card
            elif method == "Tarjeta" or method == "2":
                os.system('clear')
                print("\n" "Por favor indica los datos necesarios:")
                pay = payment.Card(
                input("""Repite el Id que colocaste anteriormente 
UserId: """).strip().upper(),
                int(input("Ingresa el numero de la tarjeta: ")),
                int(input("Clave: ")),
                input("Tipo de cuenta: ")
                )

                os.system('clear')
                print("Gracias por viajar con nosotros")

            #Cash
            elif method == "Cash" or method == "3":
                os.system('clear')
                pay = payment.Cash(
                input("""Repite el Id que colocaste anteriormente 
UserId: """).strip().upper(),
                int(input("Ingresa el monto a cancelar: ")),
                )
                print("\n" "Por favor indica los datos necesarios:")
                
                os.system('clear')
                print("Gracias por viajar con nosotros")
        else:
            os.system('clear')
            print("\n" "Hasta la proxima")

        

    
    



