import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox

def actualizarEntradas(entradas):
    for i in range(len(entradas)):
        entradas[i] = entradas[i].get()
    return entradas

def validarEntradasVacias(entradas):
    if entradas != None:
        for entrada in entradas:
            if len(entrada) == 0:
                tk.messagebox.showwarning(title="Penguin Classification",message="Faltan completar algunas entradas.")
                return None
        return entradas

def valiarEntradasNumericas(entradas):
    if entradas != None:
        for i in range(1,5):
            try:
                entradas[i] = float(entradas[i])
            except:
                tk.messagebox.showerror(title="Penguin Classification",message="Entrada numérica no válida: %s"%entradas[i])
                return None
        return entradas

def obtenerEspecie(inputs):
    entradas = inputs[:]
    entradas = actualizarEntradas(entradas)
    entradas = validarEntradasVacias(entradas)
    entradas = valiarEntradasNumericas(entradas)
    if entradas != None:
        # *
        # * EJECUTAR ALGORITMO, LOS VALORES DE ENTRADA YA SE ENCUENTRAN VALIDADOS
        # *
        print(entradas)

def run():
    root = tk.Tk()
    #root.geometry("300x300")
    root.title("Penguin Classification")
    root.configure(bg="white")
    root.resizable(width=True,height=True)
    root.iconbitmap('icono.ico')

    content = tk.StringVar()

    # ---------- ENTRADAS
    fontStyle = tkFont.Font(family="Candara", size=12)
    secondaryFontStyle = tkFont.Font(family="Calibri Light", size=12)
    thirdFontStyle = tkFont.Font(family="Candara", size=12)
    tk.Label(root,text="Hábitat",bg="white",font=fontStyle).grid(row=0,sticky='W')
    tk.Label(root,text="Longitud del Pico",bg="white",font=fontStyle).grid(row=1,sticky='W')
    tk.Label(root,text="Profundidad del Pico",bg="white",font=fontStyle).grid(row=2,sticky='W')
    tk.Label(root,text="Longitud de la Aleta",bg="white",font=fontStyle).grid(row=3,sticky='W')
    tk.Label(root,text="Masa Corporal",bg="white",font=fontStyle).grid(row=4,sticky='W')
    tk.Label(root,text="Sexo",bg="white",font=fontStyle).grid(row=5,sticky='W')

    island = ttk.Combobox(root,font=secondaryFontStyle)
    island["values"] = ["Torgersen","Biscoe","Dream"]
    island.grid(row=0,column=1,sticky='E')

    bill_length_mm = ttk.Entry(root,font=secondaryFontStyle,textvariable=content)
    bill_length_mm.grid(row=1,column=1,sticky='E')

    bill_depth_mm = ttk.Entry(root,font=secondaryFontStyle)
    bill_depth_mm.grid(row=2,column=1,sticky='E')

    flipper_length_mm = ttk.Entry(root,font=secondaryFontStyle)
    flipper_length_mm.grid(row=3,column=1,sticky='E')

    body_mass_g = ttk.Entry(root,font=secondaryFontStyle)
    body_mass_g.grid(row=4,column=1,sticky='E')

    sex = ttk.Combobox(root,font=secondaryFontStyle)
    sex["values"] = ["Masculino","Femenino"]
    sex.grid(row=5,column=1)

    entradas = [island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex]

    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=1,column=2,sticky='W')
    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=2,column=2,sticky='W')
    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=3,column=2,sticky='W')
    tk.Label(root,text="g",bg="white",font=fontStyle).grid(row=4,column=2,sticky='W')

    # ---------- IMAGEN
    image = tk.PhotoImage(file="penguin.png")
    tk.Label(root,image=image,bg="white",font=fontStyle).grid(row=6,column=0,columnspan=2,rowspan=2,sticky="WENS",padx=5,pady=5)
    
    # ---------- SALIDAS
    tk.Button(root,text="Especie",command=lambda:obtenerEspecie(entradas),bd=1,bg="#EB984E",relief="raised",width=20,font=thirdFontStyle).grid(row=9,column=0,columnspan=3)
    tk.Label(root,text="La especie del pingüino es Adelie",bg="white",font=thirdFontStyle).grid(row=10,column=0,columnspan=3)
    root.mainloop()

if __name__ == "__main__":
    run()