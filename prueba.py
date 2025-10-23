import tkinter as tk
from tkinter import messagebox


# Función para manejar el clic del botón
def al_hacer_clic():
    # Obtener el texto de ambos campos Entry
    texto_entry1 = entry1.get()
    texto_entry2 = entry2.get()

    # Realizar la acción deseada con los textos de los Entry
    # Por ejemplo, mostrarlos en un mensaje
    mensaje = f"Texto del primer campo: {texto_entry1}\nTexto del segundo campo: {texto_entry2}"
    messagebox.showinfo("Información", mensaje)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Entry y Botón")

# Crear los campos Entry
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

# Crear el botón y vincularlo a la función
# El comando llama a la función al_hacer_clic() cuando se presiona el botón
boton = tk.Button(ventana, text="Procesar", command=al_hacer_clic)
boton.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()