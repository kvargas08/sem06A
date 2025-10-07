import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Básica con Tkinter")
        self.geometry("350x250")

        frame1 = tk.Frame(self)
        tk.Label(frame1, text="Nombre:", width=9).grid(row=0, column=0, pady=5)
        self.entry1 = tk.Entry(frame1)
        self.entry1.grid(row=0, column=1, pady=5)
        frame1.pack(pady=10)

        frame2 = tk.Frame(self)
        tk.Label(frame2, text="Telefono:").grid(row=0, column=0, pady=5)
        self.entry2 = tk.Entry(frame2)
        self.entry2.grid(row=0, column=1, pady=5)
        frame2.pack(pady=10)
    
        frame3 = tk.Frame(self)
        tk.Button(frame3, text="Guardar", command=self.guardar_datos).grid(row=0, column=0,  padx=10, pady=5)
        tk.Button(frame3, text="Eliminar", command=self.eliminar_datos).grid(row=0, column=1, pady=5)
        frame3.pack(pady=10)

        self.lista = tk.Listbox(self, width=50, height=5)
        self.lista.pack(pady=10)

    def eliminar_datos(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)
            messagebox.showinfo("Información", "Elemento eliminado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un elemento para eliminar.")

    def guardar_datos(self):
        nombre = self.entry1.get()
        telefono = self.entry2.get()
        # Validaciones
        if nombre and telefono:
            self.lista.insert(tk.END, f"Nombre: {nombre}, Teléfono: {telefono}")
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
            messagebox.showinfo("Información", "Datos guardados correctamente:\n" + f"Nombre: {nombre}, Teléfono: {telefono}")
            # Limpiar los campos después de guardar
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete ambos campos.")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
