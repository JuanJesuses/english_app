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

    messagebox.showinfo("✅ Eliminado", "El registro ha sido eliminado correctamente.")


def editar_registro(tabla, tree):
    item = tree.selection()
    if not item:
        return

    valores = tree.item(item, "values")
    id_registro, campo_ing, campo_esp = valores

    ventana_edicion = tk.Toplevel()
    ventana_edicion.title("✏️ Editar registro")
    ventana_edicion.geometry("340x240")
    ventana_edicion.configure(bg="#f0f4ff")

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TLabel", background="#f0f4ff", font=("Segoe UI", 11))
    style.configure("TEntry", font=("Segoe UI", 10))
    style.configure("Guardar.TButton", background="#4F46E5", foreground="white", font=("Segoe UI", 10, "bold"), padding=6)
    style.map("Guardar.TButton",
              background=[("active", "#6366F1")],
              foreground=[("active", "white")])

    ttk.Label(ventana_edicion, text="🗣 Inglés:").pack(pady=(10, 2))
    entrada_ing = ttk.Entry(ventana_edicion, width=30)
    entrada_ing.insert(0, campo_ing)
    entrada_ing.pack(pady=(0, 10))

    ttk.Label(ventana_edicion, text="📝 Español:").pack(pady=(0, 2))
    entrada_esp = ttk.Entry(ventana_edicion, width=30)
    entrada_esp.insert(0, campo_esp)
    entrada_esp.pack(pady=(0, 10))

    def guardar_cambios():
        nuevo_ing = entrada_ing.get().strip()
        nuevo_esp = entrada_esp.get().strip()

        if not nuevo_ing or not nuevo_esp:
            messagebox.showwarning("⚠️ Campos vacíos", "Por favor, completa ambos campos antes de guardar.")
            return

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

        # Simulación de animación con ventana emergente
        confirm = tk.Toplevel()
        confirm.title("✅ Cambios guardados")
        confirm.geometry("250x100")
        confirm.configure(bg="#e0f7e9")

        ttk.Label(confirm, text="🎉 ¡Registro actualizado!", font=("Segoe UI", 11), background="#e0f7e9").pack(pady=20)
        confirm.after(1500, confirm.destroy)

    ttk.Button(ventana_edicion, text="💾 Guardar", command=guardar_cambios, style="Guardar.TButton").pack(pady=10)



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
                "palabras": ["Inglés", "Español"],
                "phrasales": ["Phrasal Verb", "Traducción"],
                "expresiones": ["Expresión", "Traducción"]
            }
            writer.writerow(encabezados[tabla])

            for fila in datos:
                writer.writerow(fila[1:])  # Ignora el ID

        messagebox.showinfo("✅ Exportación exitosa", f"Datos exportados a:\n{archivo}")
    except Exception as e:
        messagebox.showerror("❌ Error", f"No se pudo exportar:\n{e}")



def mostrar_datos_tabla(tabla, parent):
    ventana = tk.Toplevel(parent)
    ventana.title(f"Datos de {tabla.capitalize()}")
    ventana.geometry("750x550")
    ventana.configure(bg="#f0f4ff")  # Fondo suave azul

    style = ttk.Style()
    style.theme_use("clam")

    # Estilos personalizados
    style.configure("TLabel", background="#f0f4ff", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)
    style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#d0e0ff")

    # Título
    ttk.Label(ventana, text="📘 Diccionario de Inglés", font=("Segoe UI", 16, "bold")).pack(pady=15)

    # Campo de búsqueda
    frame_busqueda = ttk.Frame(ventana)
    frame_busqueda.pack(pady=10)

    ttk.Label(frame_busqueda, text="Buscar:").pack(side="left", padx=5)
    entrada_busqueda = ttk.Entry(frame_busqueda, width=40)
    entrada_busqueda.pack(side="left", padx=5)

    # Columnas dinámicas
    columnas = {
        "palabras": ("ID", "Inglés", "Español"),
        "phrasales": ("ID", "Phrasal Verb", "Traducción"),
        "expresiones": ("ID", "Expresión", "Traducción")
    }

    tree = ttk.Treeview(ventana, columns=columnas[tabla], show="headings")

    for col in columnas[tabla]:
        tree.heading(col, text=col)
        if col == "ID":
            tree.column(col, width=0, stretch=False)  # Oculta visualmente el ID
        else:
            tree.column(col, width=220)

    tree.pack(fill="both", expand=True, padx=20, pady=10)

    # Botones con colores
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=15)

    colores = {
        "Eliminar": "#ff6b6b",
        "Editar": "#ffa94d",
        "Exportar": "#69db7c",
        "Cerrar": "#74c0fc"
    }

    acciones = {
        "Eliminar": lambda: eliminar_registro(tabla, tree),
        "Editar": lambda: editar_registro(tabla, tree),
        "Exportar": lambda: exportar_a_csv(tabla),
        "Cerrar": ventana.destroy
    }

    for texto, color in colores.items():
        btn_style = f"{texto}.TButton"
        style.configure(btn_style, background=color, foreground="black")
        ttk.Button(frame_botones, text=texto, command=acciones[texto], style=btn_style).pack(side="left", padx=10)

    # Cargar datos
    conn = sqlite3.connect('english_store.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    conn.close()

    for fila in datos:
        tree.insert("", "end", values=fila)

    entrada_busqueda.bind("<KeyRelease>", lambda e: filtrar_datos(tabla, tree, entrada_busqueda.get()))



"""
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

    entrada_busqueda.bind("<KeyRelease>", lambda e: filtrar_datos(tabla, tree, entrada_busqueda.get()))"""

