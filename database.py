import sqlite3
from tkinter import messagebox


def conectar_db():
    return sqlite3.connect('english_store.db')

# Creamos la tabla palabras
def crear_tabla_palabras(ing, esp):

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS palabras(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    palabra_ing TEXT UNIQUE NOT NULL,
                    palabra_esp TEXT UNIQUE NOT NULL)
            ''')

    try:
        cursor.execute("INSERT INTO palabras (palabra_ing, palabra_esp) VALUES (?, ?)", (ing, esp,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Creamos la tabla phrasales
def crear_tabla_phrasal(ing, esp):

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS phrasales(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phrasal_ing TEXT UNIQUE NOT NULL,
                    phrasal_esp TEXT UNIQUE NOT NULL)
            ''')

    try:
        cursor.execute("INSERT INTO phrasales (phrasal_ing, phrasal_esp) VALUES (?, ?)", (ing, esp,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Creamos la tabla expresiones
def crear_tabla_exps(ing, esp):

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS expresiones(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exp_ing TEXT UNIQUE NOT NULL,
                    exp_esp TEXT UNIQUE NOT NULL)
            ''')

    try:
        cursor.execute("INSERT INTO expresiones (exp_ing, exp_esp) VALUES (?, ?)", (ing, esp,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False