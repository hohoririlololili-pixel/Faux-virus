import tkinter as tk
from tkinter import messagebox
import threading
import winsound

# -------------------------------
# Créer la fenêtre principale
# -------------------------------
root = tk.Tk()
root.title("SÉCURITÉ COMPROMISE")
root.configure(bg='black')
root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", lambda: None) # Empêche la fermeture

# -------------------------------
# Taille écran
# -------------------------------
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
scale = min(w / 1920, h / 1080)

# -------------------------------
# Titre clignotant
# -------------------------------
title = tk.Label(
    root,
    text="ON VOUS A HACKER",
    font=("Courier", int(70 * scale), "bold"),
    fg="red",
    bg="black"
)
title.place(relx=0.5, rely=0.15, anchor='center')

def blink():
    current = title.cget("fg")
    title.config(fg="yellow" if current == "red" else "red")
    root.after(500, blink)

# -------------------------------
# Message explicatif
# -------------------------------
msg = tk.Label(
    root,
    text=(
        "ALERTE MAXIMUM\n\n"
        "Vos données volées par un pirate à dos de licorne.\n"
        "Il a vendu votre Netflix aux aliens.\n"
        "Envoyez 3 bitcoins-meme à : 1Troll420XxX.\n\n"
        "Sinon, votre clavier va danser la carioca.\n"
        "10 secondes. Tic-tac."
    ),
    font=("Helvetica", int(22 * scale)),
    fg="#00FF00",
    bg="black",
    justify="center",
    wraplength=int(1400 * scale)
)
msg.place(relx=0.5, rely=0.5, anchor='center')

# -------------------------------
# Bouton OK – BIEN VISIBLE
# -------------------------------
def on_ok():
    # Son troll
    def play():
        try:
            for _ in range(5):
                winsound.Beep(800, 100)
            winsound.Beep(1200, 800)
        except:
            pass
    threading.Thread(target=play, daemon=True).start()

    # Cacher + afficher messagebox + fermer
    root.withdraw()
    messagebox.showinfo(
        "TROLL RÉUSSI",
        "TU T'ES FAIT TROLL !!!\n\n"
        "😂😂😂\n\n"
        "T'AS CRU QU'ON T'AVAIT HACKÉ ?\n"
        "T'ES TOMBÉ DEDANS COMME UN GROS NOOB !\n\n"
        "😂😂😂\n\n"
        "Appuie sur OK pour t'enfuir..."
    )
    root.destroy()

ok_btn = tk.Button(
    root,
    text="OK (je panique)",
    font=("Helvetica", int(28 * scale), "bold"),
    bg="red",
    fg="white",
    activebackground="orange",
    activeforeground="black",
    relief="raised",
    bd=8,
    command=on_ok
)
ok_btn.place(relx=0.5, rely=0.78, anchor='center', width=int(350*scale), height=int(80*scale))

# -------------------------------
# Flash de fond
# -------------------------------
import itertools
colors = itertools.cycle(["#8B0000", "#FF0000", "#8B0000", "#000000"])
def flash():
    root.configure(bg=next(colors))
    root.after(100, flash)

# -------------------------------
# Lancer les effets APRÈS affichage
# -------------------------------
root.after(0, flash)
root.after(0, blink) # Démarre le clignotement
root.after(1200, lambda: root.configure(bg='black'))

# -------------------------------
# Lancement
# -------------------------------
root.mainloop()
