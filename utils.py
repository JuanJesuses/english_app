import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import csv

def eliminar_registro(tabla, tree):
    item = tree.selection()
    if item:
        valores = tree.item(item, "values")
        id_registro = valores[0]

        conn = sqlite3.connect('english_store.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {tabla} WHERE id = ?", (id_registro,))
        conn.commit()
        conn.close()

        tree.delete(item)

def editar_registro(tabla, tree):
    item = tree.selection()
    if not item:
        return

    valores = tree.item(item, "values")
    id_registro, campo_ing, campo_esp = valores

    ventana_edicion = tk.Toplevel()
    ventana_edicion.title("Editar registro")
    ventana_edicion.geometry("300x200")

    tk.Label(ventana_edicion, text="Inglés:").pack(pady=5)
    entrada_ing = tk.Entry(ventana_edicion)
    entrada_ing.insert(0, campo_ing)
    entrada_ing.pack()

    tk.Label(ventana_edicion, text="Español:").pack(pady=5)
    entrada_esp = tk.Entry(ventana_edicion)
    entrada_esp.insert(0, campo_esp)
    entrada_esp.pack()

    def guardar_cambios():
        nuevo_ing = entrada_ing.get()
        nuevo_esp = entrada_esp.get()

        conn = sqlite3.connect('english_store.db')
        cursor = conn.cursor()

        campos = {
            "palabras": ("palabra_ing", "palabra_esp"),
            "phrasales": ("phrasal_ing", "phrasal_esp"),
            "expresiones": ("exp_ing", "exp_esp")
        }

        cursor.execute(f'''
            UPDATE {tabla}
            SET {campos[tabla][0]} = ?, {campos[tabla][1]} = ?
            WHERE id = ?
        ''', (nuevo_ing, nuevo_esp, id_registro))
        conn.commit()
        conn.close()

        tree.item(item, values=(id_registro, nuevo_ing, nuevo_esp))
        ventana_edicion.destroy()

    tk.Button(ventana_edicion, text="Guardar", command=guardar_cambios).pack(pady=10)

def filtrar_datos(tabla, tree, filtro):
    conn = sqlite3.connect('english_store.db')
    cursor = conn.cursor()

    campos = {
        "palabras": ("palabra_ing", "palabra_esp"),
        "phrasales": ("phrasal_ing", "phrasal_esp"),
        "expresiones": ("exp_ing", "exp_esp")
    }

    consulta = f"""
        SELECT * FROM {tabla}
        WHERE {campos[tabla][0]} LIKE ? OR {campos[tabla][1]} LIKE ?
    """
    cursor.execute(consulta, (f"%{filtro}%", f"%{filtro}%"))
    resultados = cursor.fetchall()
    conn.close()

    tree.delete(*tree.get_children())
    for fila in resultados:
        tree.insert("", "end", values=fila)

def exportar_a_csv(tabla):
    conn = sqlite3.connect('english_store.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    conn.close()

    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not archivo:
        return

    try:
        with open(archivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            encabezados = {
                "palabras": ["ID", "Inglés", "Español"],
                "phrasales": ["ID", "Phrasal Verb", "Traducción"],
                "expresiones": ["ID", "Expresión", "Traducción"]
            }
            writer.writerow(encabezados[tabla])
            for fila in datos:
                writer.writerow(fila)

        messagebox.showinfo("Exportación exitosa", f"Datos exportados a:\n{archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo exportar:\n{e}")

def mostrar_datos_tabla(tabla, parent):
    ventana = tk.Toplevel(parent)
    ventana.title(f"Datos de {tabla.capitalize()}")
    ventana.geometry("700x500")
    ventana.configure(bg="#f9f9f9")

    frame_busqueda = ttk.Frame(ventana)
    frame_busqueda.pack(pady=10)

    ttk.Label(frame_busqueda, text="Buscar:").pack(side="left", padx=5)
    entrada_busqueda = ttk.Entry(frame_busqueda, width=40)
    entrada_busqueda.pack(side="left", padx=5)

    columnas = {
        "palabras": ("ID", "Inglés", "Español"),
        "phrasales": ("ID", "Phrasal Verb", "Traducción"),
        "expresiones": ("ID", "Expresión", "Traducción")
    }

    tree = ttk.Treeview(ventana, columns=columnas[tabla], show="headings")
    for col in columnas[tabla]:
        tree.heading(col, text=col)
        tree.column(col, width=200)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=10)

    ttk.Button(frame_botones, text="Eliminar", command=lambda: eliminar_registro(tabla, tree)).pack(side="left", padx=5)
    ttk.Button(frame_botones, text="Editar", command=lambda: editar_registro(tabla, tree)).pack(side="left", padx=5)
    ttk.Button(frame_botones, text="Exportar a CSV", command=lambda: exportar_a_csv(tabla)).pack(side="left", padx=5)
    ttk.Button(frame_botones, text="Cerrar", command=ventana.destroy).pack(side="left", padx=5)

    conn = sqlite3.connect('english_store.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    conn.close()

    for fila in datos:
        tree.insert("", "end", values=fila)

    entrada_busqueda.bind("<KeyRelease>", lambda e: filtrar_datos(tabla, tree, entrada_busqueda.get()))

