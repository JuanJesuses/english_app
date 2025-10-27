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
# Comentario de prueba

# Ejecutar la aplicación
ventana_principal.mainloop()
