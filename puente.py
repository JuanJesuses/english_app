import tkinter as tk
from tkinter import ttk, messagebox
import database

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

        exito = database.crear_tabla(ing, esp)
        if not exito:
            messagebox.showerror("Duplicado", "La palabra ya existe.", parent=ventana_a)
        else:
            entrada_palabras_eng.delete(0, tk.END)
            entrada_palabras_esp.delete(0, tk.END)

    # Botones
    ttk.Button(frame, text="Guardar palabra", command=grabar).grid(row=3, column=0, columnspan=2, pady=15)
    ttk.Button(frame, text="Volver al inicio", command=ventana_a.destroy).grid(row=4, column=0, columnspan=2)


# main.py
import tkinter as tk
from tkinter import ttk
from palabras import abrir_ventana_words
from expresiones import abrir_ventana_exps
from phrasal import abrir_ventana_phrasal

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("English Store")
ventana_principal.geometry("400x300")
ventana_principal.configure(bg="#f0f0f0")

# Estilo moderno
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 14, "bold"))

# Frame central
frame = ttk.Frame(ventana_principal, padding=30)
frame.pack(expand=True)

# Título
ttk.Label(frame, text="English Store", anchor="center").grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Botones de navegación
ttk.Button(frame, text="Words", command=lambda: abrir_ventana_words(ventana_principal)).grid(row=1, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Expressions", command=lambda: abrir_ventana_exps(ventana_principal)).grid(row=2, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Phrasal Verbs", command=lambda: abrir_ventana_phrasal(ventana_principal)).grid(row=3, column=0, columnspan=2, pady=5)

# Botón de salida
ttk.Button(frame, text="Salir", command=ventana_principal.destroy).grid(row=4, column=0, columnspan=2, pady=(20, 0))

# Ejecutar la aplicación
ventana_principal.mainloop()

