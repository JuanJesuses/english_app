import tkinter as tk
from tkinter import ttk, messagebox
import database
from utils import mostrar_datos_tabla

def abrir_ventana_phrasal(parent):

    ventana_b = tk.Toplevel(parent)
    ventana_b.title("Palabras")
    ventana_b.geometry("600x400")
    ventana_b.configure(bg="#f5f5f5")

    # Parámetros de configuración de estilo de botones etiquetas y entradas
    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 11), padding=6)
    style.configure("TEntry", padding=4)

    # Frame principal
    frame = ttk.Frame(ventana_b, padding=20)
    frame.pack(expand=True)

    # Etiqueta de título
    ttk.Label(frame, text="Añadir Nuevo Phrasal Verb", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Campo Inglés
    ttk.Label(frame, text="Inglés:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_phrasal_eng = ttk.Entry(frame, width=30)
    entrada_phrasal_eng.grid(row=1, column=1, padx=5, pady=5)

    # Campo Español
    ttk.Label(frame, text="Español:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entrada_phrasal_esp = ttk.Entry(frame, width=30)
    entrada_phrasal_esp.grid(row=2, column=1, padx=5, pady=5)

    # Función grabar definida antes del botón
    def grabar():

        phr_ing = entrada_phrasal_eng.get().strip()
        phr_esp = entrada_phrasal_esp.get().strip()
        if not phr_ing or not phr_esp:
            messagebox.showwarning("Campos Vacíos", "por favor, completa ambos campos", parent=ventana_b)

        exito = database.crear_tabla_phrasal(phr_ing, phr_esp)
        if not exito:
            messagebox.showerror("ERROR!", "El phrasal verb ya existe!!", parent=ventana_b)
            entrada_phrasal_eng.delete(0, tk.END)
            entrada_phrasal_esp.delete(0, tk.END)
        else:
            entrada_phrasal_eng.delete(0, tk.END)
            entrada_phrasal_esp.delete(0, tk.END)

    # Botón para guardar expresión
    ttk.Button(frame, text="Guardar Phrasal Verb", command=grabar).grid(row=3, column=1, sticky="w", pady=15)

    # Botón para ver expresiones guardadas
    ttk.Button(frame, text="Ver Phrasales Guardados", command=lambda: mostrar_datos_tabla("phrasales", ventana_b)).grid(row=4, column=1, sticky="w", pady=5)

    # Botón para vovler al inicio
    ttk.Button(frame, text="Volver al Inicio", command=ventana_b.destroy).grid(row=5, column=1, sticky="w", pady=10)


"""
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

    # Botón que llama a la función grabar
    boton_phrasal = tk.Button(ventana_b, text="Grabar Phrasal Verb", command=grabar)
    boton_phrasal.pack(pady=25)

    # Botón que muestra los datos de la tabla phrasales
    boton_mostrar = tk.Button(ventana_b, text="Ver Phrasales Guardados", command=lambda: mostrar_datos_tabla("phrasales", ventana_b))
    boton_mostrar.pack(pady=10)

    boton_volver = tk.Button(ventana_b, text="Volver a Incio", command=ventana_b.destroy)
    boton_volver.pack(pady=10) """