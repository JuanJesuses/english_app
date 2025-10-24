import tkinter as tk
from tkinter import ttk, messagebox
import database
from utils import mostrar_datos_tabla

# palabras.py
def abrir_ventana_words(parent):
    ventana_a = tk.Toplevel(parent)
    ventana_a.title("Gestión de Palabras")
    ventana_a.geometry("500x300")
    ventana_a.configure(bg="#f5f5f5")

    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 10), padding=6)
    style.configure("TEntry", padding=4)

    # Frame principal
    frame = ttk.Frame(ventana_a, padding=20)
    frame.pack(expand=True)

    # Etiqueta de título
    ttk.Label(frame, text="Añadir nueva palabra", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Campo inglés
    ttk.Label(frame, text="Inglés:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_palabras_eng = ttk.Entry(frame, width=30)
    entrada_palabras_eng.grid(row=1, column=1, padx=5, pady=5)

    # Campo español
    ttk.Label(frame, text="Español:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entrada_palabras_esp = ttk.Entry(frame, width=30)
    entrada_palabras_esp.grid(row=2, column=1, padx=5, pady=5)

    # Función para grabar
    def grabar():
        ing = entrada_palabras_eng.get().strip()
        esp = entrada_palabras_esp.get().strip()
        if not ing or not esp:
            messagebox.showwarning("Campos vacíos", "Por favor, completa ambos campos.", parent=ventana_a)
            return

        exito = database.crear_tabla_palabras(ing, esp)
        if not exito:
            messagebox.showerror("Duplicado", "La palabra ya existe.", parent=ventana_a)
            entrada_palabras_eng.delete(0, tk.END)
            entrada_palabras_esp.delete(0, tk.END)
        else:
            entrada_palabras_eng.delete(0, tk.END)
            entrada_palabras_esp.delete(0, tk.END)

    # Botón para guardar palabra
    ttk.Button(frame, text="Guardar palabra", command=grabar).grid(row=3, column=1, sticky="w", pady=15)

    # Botón para ver palabras guardadas
    ttk.Button(frame, text="Ver palabras guardadas", command=lambda: mostrar_datos_tabla("palabras", ventana_a)).grid(
        row=4, column=1, sticky="w", pady=5)

    # Botón para volver al inicio
    ttk.Button(frame, text="Volver al inicio", command=ventana_a.destroy).grid(row=5, column=1, sticky="w", pady=10)

    """
    # Botones
    ttk.Button(frame, text="Guardar palabra", command=grabar).grid(row=3, column=0, columnspan=2, pady=15)
    ttk.Button(frame, text="Ver palabras guardadas", command=lambda: mostrar_datos_tabla("palabras", ventana_a)).grid(row=4, column=0, columnspan=10)
    #ttk.Button(frame, text="Ver palabras Guardadas", command=lambda : mostrar_datos_tabla("palabras", ventana_a).grid(row=2, column=0, columnspan=10))
    ttk.Button(frame, text="Volver al inicio", command=ventana_a.destroy).grid(row=5, column=0, columnspan=2)"""




"""
import tkinter as tk
from tkinter import ttk, messagebox
import database
from utils import mostrar_datos_tabla

def abrir_ventana_words(parent):

    ventana_a = tk.Toplevel(parent)
    ventana_a.title("Palabras")
    ventana_a.geometry("600x400")

    etiqueta_palabras = tk.Label(ventana_a, text="Agrega palabras")
    etiqueta_palabras.pack(side="top", pady=10)

    etiqueta_palabras_eng = tk.Label(ventana_a, text="English")
    etiqueta_palabras_eng.pack(pady=15)

    entrada_palabras_eng = tk.Entry(ventana_a)
    entrada_palabras_eng.pack()

    etiqueta_palabras_esp = tk.Label(ventana_a, text="Spanish")
    etiqueta_palabras_esp.pack(pady=15)

    entrada_palabras_esp = tk.Entry(ventana_a)
    entrada_palabras_esp.pack()

    # Función grabar definida antes del botón
    def grabar():
        exito = database.crear_tabla_palabras(entrada_palabras_eng.get(), entrada_palabras_esp.get())
        if not exito:
            messagebox.showerror("ERROR", "La palabra ya existe!!", parent=ventana_a)
            entrada_palabras_eng.delete(0, tk.END)
            entrada_palabras_esp.delete(0, tk.END)
        else:
            entrada_palabras_eng.delete(0, tk.END)
            entrada_palabras_esp.delete(0, tk.END)

    # Botón que llama a la función grabar
    boton_palabras = tk.Button(ventana_a, text="Grabar Palabras", command=grabar)
    boton_palabras.pack(pady=25)

    # Botón que muestra los datos de la tabla palabras
    boton_mostrar = tk.Button(ventana_a, text="Ver Palabras Guardadas", command=lambda: mostrar_datos_tabla("palabras", ventana_a))
    boton_mostrar.pack(pady=10)

    boton_volver = tk.Button(ventana_a, text="Volver a Incio", command=ventana_a.destroy)
    boton_volver.pack(pady=10) """