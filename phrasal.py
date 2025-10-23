import tkinter as tk
from tkinter import messagebox
import database
from utils import mostrar_datos_tabla

def abrir_ventana_phrasal(parent):

    ventana_b = tk.Toplevel(parent)
    ventana_b.title("Palabras")
    ventana_b.geometry("600x400")

    etiqueta_phrasal = tk.Label(ventana_b, text="Agrega Phrasal Verbs")
    etiqueta_phrasal.pack(side="top", pady=10)

    etiqueta_phrasal_eng = tk.Label(ventana_b, text="English")
    etiqueta_phrasal_eng.pack(pady=15)

    entrada_phrasal_eng = tk.Entry(ventana_b)
    entrada_phrasal_eng.pack()

    etiqueta_phrasal_esp = tk.Label(ventana_b, text="Spanish")
    etiqueta_phrasal_esp.pack(pady=15)

    entrada_phrasal_esp = tk.Entry(ventana_b)
    entrada_phrasal_esp.pack()

    # Función grabar definida antes del botón
    def grabar():
        exito = database.crear_tabla_phrasal(entrada_phrasal_eng.get(), entrada_phrasal_esp.get())
        if not exito:
            messagebox.showerror("ERROR", "El phrasal verb ya existe!!", parent=ventana_b)
            entrada_phrasal_eng.delete(0, tk.END)
            entrada_phrasal_esp.delete(0, tk.END)
        else:
            entrada_phrasal_eng.delete(0, tk.END)
            entrada_phrasal_esp.delete(0, tk.END)

    # Botón que llama a la función grabar
    boton_phrasal = tk.Button(ventana_b, text="Grabar Phrasal Verb", command=grabar)
    boton_phrasal.pack(pady=25)

    # Botón que muestra los datos de la tabla phrasales
    boton_mostrar = tk.Button(ventana_b, text="Ver Phrasales Guardados", command=lambda: mostrar_datos_tabla("phrasales", ventana_b))
    boton_mostrar.pack(pady=10)

    boton_volver = tk.Button(ventana_b, text="Volver a Incio", command=ventana_b.destroy)
    boton_volver.pack(pady=10)