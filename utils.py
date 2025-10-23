import tkinter as tk
import sqlite3

# Mostrar los datos de la tabla palabras
def mostrar_datos_tabla(tabla, parent):
    ventana = tk.Toplevel(parent)
    ventana.title(f"Datos de {tabla}")
    ventana.geometry("500x400")

    listbox = tk.Listbox(ventana, width=60)
    listbox.pack(pady=20)

    conn = sqlite3.connect('english_store.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    conn.close()

    for fila in datos:
        listbox.insert(tk.END, " | ".join(str(campo) for campo in fila))

