#Creando una app dinamica de terminal para simular un logIn, un signUp y un CRUD.
#Ocuparemos ArrayLists como almacenamiento, reemplazando una base de datos.

id = 0
lista = [{ #Ya habra un usuario creado por defecto para probar el inicio de sesión
    "id": id,
    "nombre": "Oscar",
    "apellido": "Palma",
    "correo": "opalma@gmail.com",
    "contrasena": "patitofeo"
}]

idEventos = 0
listaEventos = []

# Funciones del usuario
def crearUsuario(var1, var2, var3, var4):
    global id
    id += 1
    lista.append({
        "id": id,
        "nombre": var1,
        "apellido": var2,
        "correo": var3,
        "contrasena": var4
    })

def crearEvento(var1, var2, var3, var4):
    global idEventos
    listaEventos.append({
        "id": idEventos,
        "evento": var1,
        "origen": var2,
        "destino": var3,
        "precio": var4
    })
    idEventos += 1

print()
print("Bienvenido a nuestra Aplicación")
print("Por favor ingrese las siguientes opciones \n")

while True:
    print("-" * 30)
    print("1.Ingresar sesión")
    print("2.Crear usuario")
    print("3.Salir de la aplicación \n")
    menu = int(input("Ingrese una opción: "))
    print()
    
    if menu == 1:
        correo = input("Ingrese su correo para iniciar sesión: ")
        pasw = input("Ingrese su contraseña: ")
        print()
        
        usuarioEncontrado = None
        for check in lista:
            if correo == check["correo"] and pasw == check["contrasena"]:
                usuarioEncontrado = check
                break

        if usuarioEncontrado:
            print(f"Bienvenido de vuelta {usuarioEncontrado['nombre']} {usuarioEncontrado['apellido']}")
            print()
            while True:
                print("¿Qué desea hacer?")
                print("1.Crear evento")
                print("2.Listar los eventos")
                print("3.Buscar evento")
                print("4.Actualizar un evento")
                print("5.Eliminar un evento")
                print("6.Salir sesión \n")
                evento = int(input("Ingresar opción: "))
                print()

                if evento == 1: #Listo
                    print("Creando evento \n")
                    nameEvento = input("Ingresar nombre del evento: ")
                    direccOrigen = input("Ingresar ciudad de origen: ")
                    direccDestino = input("Ingresar ciudad de destino: ")
                    precio = int(input("Ingrese el precio del transporte: "))
                    print()

                    if not nameEvento or not direccDestino or not direccOrigen or not precio:
                        print("Error! No pueden haber datos vacíos \n")
                    else:
                        crearEvento(nameEvento.capitalize(), direccOrigen.capitalize(), direccDestino.capitalize(), precio)
                        print("Evento creado exitosamente!")

                elif evento == 2: #Listo

                    if len(listaEventos) > 0:
                        print("Mostrando los eventos \n")
                        print("Eventos \n")
                        for evento in listaEventos:

                            print(f"Id: {evento["id"]}")
                            print(f"Evento: {evento["evento"]}")
                            print(f"Origen: {evento["origen"]}")
                            print(f"Destino: {evento["destino"]}")
                            print(f"Precio: ${evento["precio"]} \n")
                    else:
                        print("No hay eventos registrados \n")
                            


                elif evento == 3: #Listo
                    codEvento = int(input("Ingrese codigo de evento para visualizar: "))
                    eventoEncontrado = None
                    for evento in listaEventos:
                        if codEvento == evento["id"]:
                            eventoEncontrado = evento
                            break
                        
                    if eventoEncontrado:
                        print("Listando evento por ID \n")
                        print(f"Evento: {eventoEncontrado["evento"]}")
                        print(f"origen: {eventoEncontrado["origen"]}")
                        print(f"destino: {eventoEncontrado["destino"]}")
                        print(f"Precio: ${eventoEncontrado["precio"]} \n")
                    else:
                        print("¡No se han encontrado el evento!")

                elif evento == 4:
                    print("Actualizando un evento")

                    codEvento_actualizar = int(input("Ingresar codigo del evento a actualizar: "))
                    eventoEncontrado_actualizar = None
                    eventoActualizado = False

                    for evento in listaEventos:
                        if codEvento_actualizar == evento["id"]:
                            eventoEncontrado_actualizar = evento
                            break
                    
                    if eventoEncontrado_actualizar:
                        eventoActualizar = input("Ingrese evento: ")
                        origenActualizar = input("Ingrese origen: ")
                        destinoActualizar = input("Ingrese destino: ")
                        precioActualizar = int(input("Ingrese precio: "))

                        eventoEncontrado_actualizar["evento"] = eventoActualizar.capitalize()
                        eventoEncontrado_actualizar["origen"] = origenActualizar
                        eventoEncontrado_actualizar["destino"] = destinoActualizar
                        eventoEncontrado_actualizar["precio"] = precioActualizar
                        eventoActualizado = True

                    if eventoEncontrado == True:
                        print("Evento actualizado con exito!")
                    else:
                        print("Error! No se pudo actualizar el evento.")



                elif evento == 5: #Listo
                    print("Eliminando un evento")

                    codEvento_eliminar = int(input("Ingrese el codigo del evento a Eliminar: "))
                    print()
                    eventoEliminado = False
                    for idx, evento in enumerate(listaEventos): #Se usa para obtener el indice y el evento
                        if codEvento_eliminar == evento["id"]:
                            listaEventos.pop(idx) #Elimina usando el indice
                            eventoEliminado = True#Si fue encontrado el id, entonces la variable cambia a true
                            break
                        
                    if eventoEliminado:
                        print("Se ah eliminado con exito el evento \n")
                    else:
                        print("Error, no se ah encontrado el evento a eliminar \n")
                elif evento == 6: #Listo
                    print("Saliendo de la sesión")
                    break

        else:
            print("Error! Correo y/o Contraseña erróneos")

    elif menu == 2:
        print("Creando usuario \n")
        name = input("Ingrese su nombre principal: ")
        lastname = input("Ingrese su primer apellido: ")
        email = input("Ingrese su correo: ")
        psw = input("Ingrese su contraseña: ")
        print()

        if not name or not lastname or not email or not psw:
            print("Error! No se aceptan datos vacíos.")
        else:
            # Validar si el correo ya existe en la lista
            validarCorreo = True
            for validar in lista:
                if email == validar["correo"]:
                    validarCorreo = False
                    break

            if validarCorreo:
                crearUsuario(name.capitalize(), lastname.capitalize(), email, psw)
                print("Usuario creado con éxito \n")
            else:
                print("Error! Correo electrónico ya está creado \n")

    elif menu == 3:
        print("Hasta luego! :) \n")
        break

print("Programa finalizado con éxito!")
