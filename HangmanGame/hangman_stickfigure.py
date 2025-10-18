#Hangman: Implement the word guessing game with visual progress and hints.
import tkinter as tk
import random

WORDS = {
    "python": "A popular programming language.",
    "banana": "A long yellow fruit.",
    "elephant": "A very large land animal with a trunk.",
    "computer": "Device used to process data.",
    "river": "Natural flowing watercourse.",
    "hangman": "This guessing game you are playing.",
    "notebook": "You are using it now!"
}

MAX_WRONG = 6

def start_game():
    global word, hint, guessed_letters, wrong_guesses, score
    word, hint = random.choice(list(WORDS.items()))
    word = word.lower()
    guessed_letters = set()
    wrong_guesses = 0
    score = 0
    canvas.delete("all")
    draw_gallows()
    update_display("Game started! Good luck!")
    guessed_label.config(text="Guessed Letters: None")
    score_label.config(text=f"Score: {score}")
    entry_guess.config(state="normal")
    btn_guess.config(state="normal")

def update_display(message=""):
    masked = " ".join([c if c in guessed_letters else "_" for c in word])
    word_label.config(text=f"Word: {masked}")
    message_label.config(text=message)
    guessed_label.config(text=f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    score_label.config(text=f"Score: {score}")
    draw_stick_figure()

def guess_letter():
    global wrong_guesses, score
    g = entry_guess.get().lower().strip()
    entry_guess.delete(0, tk.END)
    if not g:
        return
    if g == word:
        guessed_letters.update(set(word))
        score += len(set(word))
        update_display(f"🎉 Congratulations! You guessed the word '{word}'")
        entry_guess.config(state="disabled")
        btn_guess.config(state="disabled")
        return
    if len(g) == 1:
        if g in guessed_letters:
            update_display("You already guessed that letter.")
        elif g in word:
            guessed_letters.add(g)
            score += 1
            if all(c in guessed_letters for c in word):
                update_display(f"🎉 You won! The word was '{word}'")
                entry_guess.config(state="disabled")
                btn_guess.config(state="disabled")
            else:
                update_display(f"✅ Good guess: '{g}'")
        else:
            wrong_guesses += 1
            score -= 1
            guessed_letters.add(g)
            update_display(f"❌ Wrong guess: '{g}'")
    else:
        if g == word:
            guessed_letters.update(set(word))
            score += len(set(word))
            update_display(f"🎉 You guessed the word '{word}'")
            entry_guess.config(state="disabled")
            btn_guess.config(state="disabled")
        else:
            wrong_guesses += 1
            score -= 1
            update_display(f"❌ Wrong word guess.")
    if wrong_guesses >= MAX_WRONG:
        update_display(f"💀 Game over! The word was '{word}'")
        entry_guess.config(state="disabled")
        btn_guess.config(state="disabled")

def show_hint():
    update_display(f"💡 Hint: {hint}")

def draw_gallows():
    canvas.create_line(50, 250, 150, 250, width=3)
    canvas.create_line(100, 250, 100, 50, width=3)
    canvas.create_line(100, 50, 200, 50, width=3)
    canvas.create_line(200, 50, 200, 80, width=3)

def draw_stick_figure():
    canvas.delete("figure")
    if wrong_guesses >= 1:
        canvas.create_oval(180, 80, 220, 120, width=2, tag="figure")
    if wrong_guesses >= 2:
        canvas.create_line(200, 120, 200, 180, width=2, tag="figure")
    if wrong_guesses >= 3:
        canvas.create_line(200, 130, 170, 160, width=2, tag="figure")
    if wrong_guesses >= 4:
        canvas.create_line(200, 130, 230, 160, width=2, tag="figure")
    if wrong_guesses >= 5:
        canvas.create_line(200, 180, 170, 220, width=2, tag="figure")
    if wrong_guesses >= 6:
        canvas.create_line(200, 180, 230, 220, width=2, tag="figure")

root = tk.Tk()
root.title("Hangman Game - Stick Figure Version")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

word_label = tk.Label(root, text="", font=("Helvetica", 18))
word_label.pack()

entry_guess = tk.Entry(root, font=("Helvetica", 16))
entry_guess.pack()

btn_guess = tk.Button(root, text="Guess", command=guess_letter)
btn_guess.pack()

btn_hint = tk.Button(root, text="Hint 💡", command=show_hint)
btn_hint.pack()

btn_restart = tk.Button(root, text="Restart 🔁", command=start_game)
btn_restart.pack()

guessed_label = tk.Label(root, text="", font=("Helvetica", 14))
guessed_label.pack()

score_label = tk.Label(root, text="", font=("Helvetica", 14))
score_label.pack()

message_label = tk.Label(root, text="", font=("Helvetica", 14))
message_label.pack()

start_game()
root.mainloop()
