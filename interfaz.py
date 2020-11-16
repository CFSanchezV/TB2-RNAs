import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

def run():
    root = tk.Tk()
    #root.geometry("300x300")
    root.title("Penguin Classification")
    root.configure(bg="white")
    root.resizable(width=True,height=True)

    # ---------- ENTRADAS
    fontStyle = tkFont.Font(family="Verdana", size=12)
    secondayFontStyle = tkFont.Font(family="Calibri Light", size=12)
    tk.Label(root,text="Hábitat",bg="white",font=fontStyle).grid(row=0,sticky='W')
    tk.Label(root,text="Longitud del Pico",bg="white",font=fontStyle).grid(row=1,sticky='W')
    tk.Label(root,text="Profundidad del Pico",bg="white",font=fontStyle).grid(row=2,sticky='W')
    tk.Label(root,text="Longitud de la Aleta",bg="white",font=fontStyle).grid(row=3,sticky='W')
    tk.Label(root,text="Masa Corporal",bg="white",font=fontStyle).grid(row=4,sticky='W')
    tk.Label(root,text="Sexo",bg="white",font=fontStyle).grid(row=5,sticky='W')

    # island = tk.Entry(root).grid(row=0,column=1)
    island = ttk.Combobox(root,font=secondayFontStyle)
    island["values"] = ["Torgersen","Biscoe","Dream"]
    island.grid(row=0,column=1)
    bill_length_mm = tk.Entry(root,font=secondayFontStyle).grid(row=1,column=1)
    bill_depth_mm = tk.Entry(root,font=secondayFontStyle).grid(row=2,column=1)
    flipper_length_mm = tk.Entry(root,font=secondayFontStyle).grid(row=3,column=1)
    body_mass_g = tk.Entry(root,font=secondayFontStyle).grid(row=4,column=1)
    # sex = tk.Entry(root).grid(row=5,column=1)
    island = ttk.Combobox(root,font=secondayFontStyle)
    island["values"] = ["Masculino","Femenino"]
    island.grid(row=5,column=1)

    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=1,column=2)
    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=2,column=2)
    tk.Label(root,text="mm",bg="white",font=fontStyle).grid(row=3,column=2)
    tk.Label(root,text="g",bg="white",font=fontStyle).grid(row=4,column=2)

    # ---------- IMAGEN
    image = tk.PhotoImage(file="penguin.png")
    tk.Label(root,image=image,bg="white",font=fontStyle).grid(row=6,column=0,columnspan=3,rowspan=2,sticky="WENS",padx=5,pady=5)
    
    # ---------- SALIDAS
    tk.Button(root,text="Especie",bd=1,bg="#EB984E",relief="raised",width=20,font=fontStyle).grid(row=9,column=0,columnspan=3)
    tk.Label(root,text="La especie del pingüino es Adelie",bg="white",font=fontStyle).grid(row=10,column=0,columnspan=3)
    root.mainloop()

if __name__ == "__main__":
    run()