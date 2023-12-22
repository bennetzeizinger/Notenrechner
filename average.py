import tkinter as tk
from tkinter import ttk


def calculaqte(event=None):
    subjects_input = subjects_show.get()

    subjects_input_cleaned = subjects_input.replace(" ", "").replace(",", ".")

    try:
        subjects = [float(x) for x in subjects_input_cleaned.split(".")]
        number = len(subjects)
        summe = sum(subjects)
        result = summe / number

        result_label.config(text=str(result).replace(".", ","))
    except ValueError:
        result_label.config(
            text="Ungültige Eingabe! Bitte Zahlen mit Komma oder Leerzeichen trennen."
        )



root = tk.Tk()
root.title("Notenrechner")
root.geometry("475x225")

head = ttk.Label(root, text="Notenrechner", font=("Arial", 25, "bold"))
head.pack()

fill1 = ttk.Label(root, text="")
fill1.pack()

question2 = ttk.Label(root, text="Gib hier deine Noten ein!")
question2.pack()

subjects_show = ttk.Entry(root, width=50)
subjects_show.pack()

fill3 = ttk.Label(root, text="")
fill3.pack()

go = ttk.Button(root, text="Berechnen!", command=calculate)
go.pack()

fill4 = ttk.Label(root, text="")
fill4.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.bind("<Return>", calculate)

root.mainloop()