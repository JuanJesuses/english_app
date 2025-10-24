import tkinter as tk
from tkinter import ttk, messagebox
import database
from utils import mostrar_datos_tabla


def abrir_ventana_exps(parent):

    ventana_c = tk.Toplevel(parent)
    ventana_c.title("Palabras")
    ventana_c.geometry("600x400")
    ventana_c.configure(bg="#f5f5f5")

    # Parámetros de configuración de estilo de botones etiquetas y entradas
    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 11), padding=6)
    style.configure("TEntry", padding=4)

    # Frame principal
    frame = ttk.Frame(ventana_c, padding=20)
    frame.pack(expand=True)

    # Etiqueta de título
    ttk.Label(frame, text="Añadir Nueva Expresión", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Campo Inglés
    ttk.Label(frame, text="Inglés:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_exp_eng = ttk.Entry(frame, width=30)
    entrada_exp_eng.grid(row=1, column=1, padx=5, pady=5)

    # Campo Español
    ttk.Label(frame, text="Español:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entrada_exp_esp = ttk.Entry(frame, width=30)
    entrada_exp_esp.grid(row=2, column=1, padx=5, pady=5)

    # Función grabar definida antes del botón
    def grabar():
        exp_ing = entrada_exp_eng.get().strip()
        exp_esp = entrada_exp_esp.get().strip()
        if not exp_ing or not exp_esp:
            messagebox.showwarning("Campos vacíos", "Por favor, completa ambos campos", parent=ventana_c)

        exito = database.crear_tabla_exps(exp_ing, exp_esp)
        if not exito:
            messagebox.showerror("ERROR!", "La expresión ya existe!!", parent=ventana_c)
            entrada_exp_eng.delete(0, tk.END)
            entrada_exp_esp.delete(0, tk.END)
        else:
            entrada_exp_eng.delete(0, tk.END)
            entrada_exp_esp.delete(0, tk.END)

    # Botón para guardar expresión
    ttk.Button(frame, text="Guardar Expresión", command=grabar).grid(row=3, column=1, sticky="w", pady=15)

    # Botón para ver expresiones guardadas
    ttk.Button(frame,text="Ver Expresiones Guardadas", command=lambda : mostrar_datos_tabla("expresiones", ventana_c)).grid(row=4, column=1, sticky="w", pady=5)

    # Botón para vovler al inicio
    ttk.Button(frame, text="Volver al Inicio", command=ventana_c.destroy).grid(row=5, column=1, sticky="w", pady=10)

    """
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

    # Botón que llama a la función grabar
    boton_phrasal = tk.Button(ventana_c, text="Grabar Expresión", command=grabar)
    boton_phrasal.pack(pady=25)

    # Botón que muestra los datos de la tabla expresiones
    boton_mostrar = tk.Button(ventana_c, text="Ver Expresiones Guardadas", command=lambda: mostrar_datos_tabla("expresiones", ventana_c))
    boton_mostrar.pack(pady=10)

    boton_volver = tk.Button(ventana_c, text="Volver a Incio", command=ventana_c.destroy)
    boton_volver.pack(pady=10) """