import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from mainGUI import *
import random as rand


def actualizarEntradas(entradas):
    for i in range(len(entradas)):
        entradas[i] = entradas[i].get()
    return entradas


def validarEntradasVacias(entradas):
    if entradas is not None:
        for entrada in entradas:
            if len(entrada) == 0:
                tk.messagebox.showwarning(
                    title="Penguin Classification", message="Faltan completar algunas entradas.")
                return None
        return entradas


# def validarEntradasNumericas(entradas):
#     if entradas is not None:
#         for i in range(1, 5):
#             try:
#                 entradas[i] = float(entradas[i])
#             except:
#                 tk.messagebox.showerror(
#                     title="Penguin Classification", message="Entrada numérica no válida: %s" % entradas[i])
#                 return None
#         return entradas


def obtenerEspecie(inputs, outputs):
    entradas = inputs[:]
    entradas = actualizarEntradas(entradas)
    entradas = validarEntradasVacias(entradas)
    # entradas = validarEntradasNumericas(entradas)
    salidas = outputs[:]
    if entradas is not None:
        # *
        # * EJECUTAR ALGORITMO, LOS VALORES DE ENTRADA YA SE ENCUENTRAN VALIDADOS
        # *
        print("Entradas:", end="")
        print(entradas)
        especie = process_all_input(entradas)
        # print(entradas)
        # *
        # * PROBANDO CON RESULTADO DE ESPECIE ADELIE
        # *
        # especie = rand.randint(1, 3)
        if especie == 1:
            image = Image.open("./imgs/p_adelie.png")
            image = image.resize((225, 225), Image.ANTIALIAS)
            imageTk = ImageTk.PhotoImage(image)
            salidas[0].configure(image=imageTk)
            salidas[0].image = imageTk
            salidas[1]["text"] = "La especie del pingüino es Adelie"
        if especie == 2:
            image = Image.open("./imgs/p_chinstrap.png")
            image = image.resize((225, 225), Image.ANTIALIAS)
            imageTk = ImageTk.PhotoImage(image)
            salidas[0].configure(image=imageTk)
            salidas[0].image = imageTk
            salidas[1]["text"] = "La especie del pingüino es Chinstrap"
        if especie == 3:
            image = Image.open("./imgs/p_gentoo.png")
            image = image.resize((225, 225), Image.ANTIALIAS)
            imageTk = ImageTk.PhotoImage(image)
            salidas[0].configure(image=imageTk)
            salidas[0].image = imageTk
            salidas[1]["text"] = "La especie del pingüino es Gentoo"


def run():
    root = tk.Tk()
    # root.geometry("300x300")
    root.title("Clasificación de Pinguinos")
    root.configure(bg="white")
    root.resizable(width=True, height=True)
    root.iconbitmap('./imgs/icono.ico')

    content = tk.StringVar()

    # ---------- ENTRADAS
    fontStyle = tkFont.Font(family="Candara", size=12)
    secondaryFontStyle = tkFont.Font(family="Calibri Light", size=12)
    thirdFontStyle = tkFont.Font(family="Candara", size=12)
    tk.Label(root, text="Hábitat", bg="white",
             font=fontStyle).grid(row=0, sticky='W')
    tk.Label(root, text="Longitud del Pico", bg="white",
             font=fontStyle).grid(row=1, sticky='W')
    tk.Label(root, text="Profundidad del Pico", bg="white",
             font=fontStyle).grid(row=2, sticky='W')
    tk.Label(root, text="Longitud de la Aleta", bg="white",
             font=fontStyle).grid(row=3, sticky='W')
    tk.Label(root, text="Masa Corporal", bg="white",
             font=fontStyle).grid(row=4, sticky='W')
    tk.Label(root, text="Sexo", bg="white",
             font=fontStyle).grid(row=5, sticky='W')

    island = ttk.Combobox(root, font=secondaryFontStyle)
    island["values"] = ["Torgersen", "Biscoe", "Dream"]
    island.grid(row=0, column=1, sticky='E')

    bill_length_mm = ttk.Entry(
        root, font=secondaryFontStyle, textvariable=content, width=22)
    bill_length_mm.grid(row=1, column=1, sticky='E')

    bill_depth_mm = ttk.Entry(root, font=secondaryFontStyle, width=22)
    bill_depth_mm.grid(row=2, column=1, sticky='E')

    flipper_length_mm = ttk.Entry(root, font=secondaryFontStyle, width=22)
    flipper_length_mm.grid(row=3, column=1, sticky='E')

    body_mass_g = ttk.Entry(root, font=secondaryFontStyle, width=22)
    body_mass_g.grid(row=4, column=1, sticky='E')

    sex = ttk.Combobox(root, font=secondaryFontStyle)
    sex["values"] = ["Masculino", "Femenino"]
    sex.grid(row=5, column=1)

    entradas = [island, bill_length_mm, bill_depth_mm,
                flipper_length_mm, body_mass_g, sex]

    tk.Label(root, text="mm", bg="white", font=fontStyle).grid(
        row=1, column=2, sticky='W')
    tk.Label(root, text="mm", bg="white", font=fontStyle).grid(
        row=2, column=2, sticky='W')
    tk.Label(root, text="mm", bg="white", font=fontStyle).grid(
        row=3, column=2, sticky='W')
    tk.Label(root, text="g", bg="white", font=fontStyle).grid(
        row=4, column=2, sticky='W')

    # ---------- SALIDAS
    image = Image.open("./imgs/p_default.png")
    image = image.resize((225, 225), Image.ANTIALIAS)
    imageTk = ImageTk.PhotoImage(image)
    imageOutput = tk.Label(root, image=imageTk, bg="white", font=fontStyle)
    imageOutput.grid(row=6, column=0, columnspan=2,
                     rowspan=2, sticky="WENS", padx=5, pady=5)

    textOutput = tk.Label(
        root, text="No se ha determinado ninguna especie", bg="white", font=thirdFontStyle)
    textOutput.grid(row=10, column=0, columnspan=3)
    salidas = [imageOutput, textOutput]

    tk.Button(root, text="Predecir Especie", command=lambda: obtenerEspecie(entradas, salidas), bd=1,
              bg="#EB984E", relief="raised", width=20, font=thirdFontStyle).grid(row=9, column=0, columnspan=3)

    root.mainloop()


if __name__ == "__main__":
    run()
