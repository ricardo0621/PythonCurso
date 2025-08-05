import tkinter as tk
from tkinter import messagebox
import random


# --- Lógica del Juego (similar a la versión de consola) ---

def get_random_word():
    """Selecciona una palabra aleatoria de una lista predefinida."""
    words = ["python", "programming", "computer", "keyboard", "monitor", "developer", "algorithm", "variable",
             "function", "software", "interface", "tkinter", "graphic", "application"]
    return random.choice(words)


def update_word_display(word, guessed_letters):
    """Actualiza la cadena de texto que se muestra con las letras adivinadas."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


# --- Funcionalidad de la Interfaz Gráfica ---

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Juego del Ahorcado")
        master.geometry("600x700")
        master.resizable(False, False)

        self.word_to_guess = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 7  # Puedes ajustar esto para la dificultad

        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        """Configura los elementos de la interfaz de usuario."""
        # Frame para la palabra y el estado del juego
        self.game_frame = tk.Frame(self.master, padx=20, pady=20)
        self.game_frame.pack(pady=10)

        self.word_label = tk.Label(self.game_frame, text="", font=("Arial", 36, "bold"))
        self.word_label.pack(pady=20)

        self.status_label = tk.Label(self.game_frame, text="Adivina la palabra:", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.guesses_left_label = tk.Label(self.game_frame, text="", font=("Arial", 12))
        self.guesses_left_label.pack()

        # Canvas para dibujar el ahorcado
        self.canvas = tk.Canvas(self.master, width=200, height=250, bg="white", highlightbackground="black",
                                highlightthickness=1)
        self.canvas.pack(pady=20)
        self.draw_gallows()  # Dibuja la horca inicial

        # Frame para las letras (teclado virtual)
        self.letters_frame = tk.Frame(self.master)
        self.letters_frame.pack(pady=10)

        self.letter_buttons = {}
        row = 0
        col = 0
        # Crea botones para cada letra del abecedario
        for char_code in range(ord('a'), ord('z') + 1):
            letter = chr(char_code)
            button = tk.Button(self.letters_frame, text=letter.upper(), width=4, height=2,
                               command=lambda l=letter: self.make_guess(l), font=("Arial", 10))
            button.grid(row=row, column=col, padx=2, pady=2)
            self.letter_buttons[letter] = button
            col += 1
            if col > 8:  # 9 botones por fila
                col = 0
                row += 1

        # Botón para reiniciar el juego
        self.reset_button = tk.Button(self.master, text="Reiniciar Juego", command=self.start_new_game,
                                      font=("Arial", 12), bg="#4CAF50", fg="white")
        self.reset_button.pack(pady=10)

    def draw_gallows(self):
        """Dibuja la estructura base del ahorcado."""
        self.canvas.delete("all")
        # Base
        self.canvas.create_line(10, 240, 190, 240, width=2)
        # Poste vertical
        self.canvas.create_line(50, 240, 50, 30, width=2)
        # Poste horizontal
        self.canvas.create_line(50, 30, 150, 30, width=2)
        # Cuerda
        self.canvas.create_line(150, 30, 150, 60, width=2)

    def draw_hangman_part(self):
        """Dibuja una parte del hombre ahorcado según los intentos fallidos."""
        parts = [
            lambda: self.canvas.create_oval(135, 60, 165, 90, width=2),  # Cabeza
            lambda: self.canvas.create_line(150, 90, 150, 150, width=2),  # Cuerpo
            lambda: self.canvas.create_line(150, 100, 120, 130, width=2),  # Brazo izquierdo
            lambda: self.canvas.create_line(150, 100, 180, 130, width=2),  # Brazo derecho
            lambda: self.canvas.create_line(150, 150, 120, 190, width=2),  # Pierna izquierda
            lambda: self.canvas.create_line(150, 150, 180, 190, width=2),  # Pierna derecha
            lambda: self.canvas.create_line(140, 75, 145, 80, width=2),  # Ojo izquierdo
            lambda: self.canvas.create_line(155, 75, 160, 80, width=2)
            # Ojo derecho (último intento, para completar la expresión)
        ]
        if self.incorrect_guesses <= len(parts):
            parts[self.incorrect_guesses - 1]()  # Dibuja la parte correspondiente al intento fallido actual

    def start_new_game(self):
        """Reinicia el juego y selecciona una nueva palabra."""
        self.word_to_guess = get_random_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0

        self.draw_gallows()  # Vuelve a dibujar la horca vacía
        self.update_display()
        self.enable_all_buttons()
        self.status_label.config(text="Adivina la palabra:")

    def update_display(self):
        """Actualiza la interfaz con el estado actual del juego."""
        current_display = update_word_display(self.word_to_guess, self.guessed_letters)
        self.word_label.config(text=current_display)
        self.guesses_left_label.config(
            text=f"Intentos incorrectos restantes: {self.max_incorrect_guesses - self.incorrect_guesses}")

    def make_guess(self, letter):
        """Maneja la lógica cuando el usuario adivina una letra."""
        if letter in self.guessed_letters:
            messagebox.showinfo("Ahorcado", "Ya adivinaste esa letra. ¡Intenta con otra!")
            return

        self.guessed_letters.append(letter)
        self.letter_buttons[letter].config(state=tk.DISABLED, bg="#D3D3D3")  # Deshabilita el botón

        if letter in self.word_to_guess:
            self.status_label.config(text=f"¡Bien! '{letter.upper()}' está en la palabra.")
        else:
            self.incorrect_guesses += 1
            self.status_label.config(text=f"Lo siento, '{letter.upper()}' NO está en la palabra.")
            self.draw_hangman_part()  # Dibuja una parte del ahorcado

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        """Verifica si el juego ha terminado (victoria o derrota)."""
        current_display_no_spaces = update_word_display(self.word_to_guess, self.guessed_letters).replace(" ", "")

        if "_" not in current_display_no_spaces:
            messagebox.showinfo("Ahorcado", f"¡Felicidades! Adivinaste la palabra: '{self.word_to_guess.upper()}'")
            self.disable_all_buttons()
        elif self.incorrect_guesses >= self.max_incorrect_guesses:
            messagebox.showinfo("Ahorcado",
                                f"¡Juego Terminado! Te quedaste sin intentos. La palabra era: '{self.word_to_guess.upper()}'")
            self.disable_all_buttons()

    def disable_all_buttons(self):
        """Deshabilita todos los botones de letras."""
        for letter, button in self.letter_buttons.items():
            button.config(state=tk.DISABLED)

    def enable_all_buttons(self):
        """Habilita todos los botones de letras."""
        for letter, button in self.letter_buttons.items():
            button.config(state=tk.NORMAL, bg="SystemButtonFace")  # Vuelve al color por defecto


# --- Ejecución de la Aplicación ---

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()