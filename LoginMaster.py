# Login sencillo en Python

def login():
    usuario_correcto = "admin"
    password_correcto = "1234"
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        if usuario == usuario_correcto and password == password_correcto:
            print("\n¡Inicio de sesión exitoso!")
            print(f"Bienvenido, {usuario}.")
            return

        intentos -= 1
        if intentos > 0:
            print(f"Datos incorrectos. Te quedan {intentos} intentos.")
        else:
            print("\nNo tienes más intentos. La cuenta ha sido bloqueada.")


if __name__ == "__main__":
    login()
