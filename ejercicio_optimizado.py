import random

def guess_the_number():
    # Genera un número aleatorio entre 1 y 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    # Muestra un mensaje de bienvenida
    print("Bienvenido al juego de adivinar el número.")
    print("He seleccionado un número entre 1 y 100. Intenta adivinarlo.")

    while True:
        # Solicita al usuario que ingrese su suposición
        user_guess = int(input("Ingresa tu suposición: "))
        attempts += 1

        if user_guess < number_to_guess:
            # Si la suposición es demasiado baja, muestra un mensaje
            print("¡Demasiado bajo! Inténtalo de nuevo.")
        elif user_guess > number_to_guess:
            # Si la suposición es demasiado alta, muestra otro mensaje
            print("¡Demasiado alto! Inténtalo de nuevo.")
        else:
            # Si la suposición es correcta, muestra un mensaje de felicitación y finaliza el juego
            print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")
            break

# Ejemplo de uso
guess_the_number()