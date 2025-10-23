import tkinter as tk
from tkinter import messagebox
import database
from utils import mostrar_datos_tabla


def abrir_ventana_exps(parent):
    ventana_c = tk.Toplevel(parent)
    ventana_c.title("Palabras")
    ventana_c.geometry("600x400")

    etiqueta_exp = tk.Label(ventana_c, text="Agrega Expresiones")
    etiqueta_exp.pack(side="top", pady=10)

    etiqueta_exp_eng = tk.Label(ventana_c, text="English")
    etiqueta_exp_eng.pack(pady=15)

    entrada_exp_eng = tk.Entry(ventana_c)
    entrada_exp_eng.pack()

    etiqueta_exp_esp = tk.Label(ventana_c, text="Spanish")
    etiqueta_exp_esp.pack(pady=15)

    entrada_exp_esp = tk.Entry(ventana_c)
    entrada_exp_esp.pack()

    # Función grabar definida antes del botón
    def grabar():
        exito = database.crear_tabla_exps(entrada_exp_eng.get(), entrada_exp_esp.get())
        if not exito:
            messagebox.showerror("ERROR", "La expresión ya existe!!", parent=ventana_c)
            entrada_exp_eng.delete(0, tk.END)
            entrada_exp_esp.delete(0, tk.END)
        else:
            entrada_exp_eng.delete(0, tk.END)
            entrada_exp_esp.delete(0, tk.END)

    # Botón que llama a la función grabar
    boton_phrasal = tk.Button(ventana_c, text="Grabar Expresión", command=grabar)
    boton_phrasal.pack(pady=25)

    # Botón que muestra los datos de la tabla expresiones
    boton_mostrar = tk.Button(ventana_c, text="Ver Expresiones Guardadas", command=lambda: mostrar_datos_tabla("expresiones", ventana_c))
    boton_mostrar.pack(pady=10)

    boton_volver = tk.Button(ventana_c, text="Volver a Incio", command=ventana_c.destroy)
    boton_volver.pack(pady=10)