import matplotlib.pyplot as plt
import os
import csv
ARCHIVO_SERVICIOS="servicios.txt"

def ingresar_cliente():
    print("Ingreso de cliente nuevo:")
    rut = input("RUT:   ")
    nombre = input("Nombre: ")
    apellido_p = input("Apellido paterno:   ")
    apellido_m = input("Apellido materno:   ")
    presupuesto = int(input("Presupuesto disponible:    "))
    cliente = [rut, nombre, apellido_p, apellido_m, "9999","correo@gmail.com", "Empresa SPA", presupuesto]

    return cliente

def ingresar_servicio():
    #pasaremos a que el usuario ingrese los datos del servicio menos el costo y observaciones, para el final
    cod = input("Ingrese su código:  ")
    nombre_serv = input("Ingrese el nombre del servicio: ")
    area_con=input("Ingrese el área de consultoria: ")
    consultor=input("Ingrese su consultor responsable: ")
    duracion=input("Ingrese su duración del servicio:")
    #hacer un codigo que verifique si el usuario realizo el paso 1
    
    while True:
        costo=int(input("Ingrese el costo (ej: 50000):")) #devemos ver si el costo es numero entero por eso usaremos .isdigit que es una forma de verificar que solo escribio numeros
        if costo.isdigit()
            costo=float(costo)
            break
        else:
            print("ERROR. Ingrese un numero valido (ej:50000)")
    observacion="ingrese sus observaciones: "
    #ahora pasaremos a verificar si el presupuesto es mayor o igual al costo de servicio, al ser este el caso return provocara que se salte el if y en caso de no ser asi se realizara la funcion de if
    if "presupuesto" < costo #presupuesto debe escribirse igual arriba
        print(f"El cliente {nombre} no puede contratar el servicio, el costo supera al presupuesto disponible ({"presupuesto"}).")
        return
    servicio = {
        "Rut":rut,"Código del servicio":cod,
        "":,"":,
        "":,"":,
        "":
    }
    #debemos guardar la biblioteca servicio
    return servicio

def visualizar_cliente(lista_clientes):
    print("\n--- VISUALIZACIÓN DE CLIENTES ---")
    if len(lista_clientes) == 0:
        print("No hay clientes registrados aún.")
    else:
        for c in lista_clientes:
            print(f"Rut: {c[0]} | Nombre: {c[1]} {c[2]} | Presupuesto: ${c[7]}")

def visualizar_servicios(lista_servicios):
    print("\n--- VISUALIZACIÓN DE SERVICIOS ---")
    if len(lista_servicios) == 0:
        print("No hay servicios registrados aún.")
    else:
        for s in lista_servicios:
            print(f"Código: {s[0]} | Servicio: {s[1]} | Costo: ${s[5]}")

def mostrar_grafico(clientes):
    ejex_nombres = []
    ejey_presp = []

    for cliente in clientes:
        nombre = f"{cliente[1]} {cliente[2]}"
        ejex_nombres.append(nombre)
        ejey_presp.append(cliente[7])

    plt.figure(figsize = (10,6))
    plt.bar(ejex_nombres, ejey_presp, color = "steelblue")
    plt.title("Grafico de Barras")
    plt.ylabel("Presupuesto disponible")
    plt.xlabel("Clientes")
    plt.tight_layout()
    plt.show()

def main():
    clientes = []
    servicios = []
    while True:
        print("\tSISTEMA DE CONSULTORIA GENERAL")
        print("1. Ingresar datos de clientes")
        print("2. Ingresar servicios de consultoria")
        print("3. Visualizar datos de clientes")
        print("4. Visualizar servicios registrados")
        print("5. Visualizar gráfico del presupuesto disponible de los clientes")
        print("6. Salir del programa")

        try:
            op = int(input("Seleccione una opción:  "))
            
            if op ==1:
                clientes.append(ingresar_cliente())

            elif op ==2:
                servicios.append(ingresar_servicio())

            elif op ==3:
                if len(clientes) != 0:
                    visualizar_cliente(clientes)
                else:
                    print("Falta ingresar datos de clientes.")

            elif op ==4: 
                if len(servicios) != 0:
                    visualizar_servicios(servicios)
                else:
                    print("Faltan servicios por ingresar.")

            elif op ==5:
                mostrar_grafico(clientes)

            elif op ==6:
                print("Saliendo del programa...")
                break

            else:
                print("Ingrese una opción valida (1-6).")

        except ValueError:
            print("Opcion no valida, intente otra vez con un numero entero (1-6).")
        
main()
