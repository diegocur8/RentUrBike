import tkinter as tk
from tkinter import messagebox

class Sistema:
    def __init__(self):
        self.bicicletas_disponibles = [10] * 24
        self.usuarios = []

    def registrar_usuario(self, nombre, apellido, telefono, correo, username, password):
        nuevo_usuario = {'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'correo': correo, 'username': username, 'password': password}
        self.usuarios.append(nuevo_usuario)
        messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito.")

    def iniciar_sesion(self, username, password):
        for usuario in self.usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                return usuario
        messagebox.showerror("Error de inicio de sesión", "Nombre de usuario o contraseña incorrectos.")
        return None

    def rentar_bici(self, hora, duracion):
        if hora < 8 or hora > 20:
            messagebox.showerror("Error en reserva", "Lo sentimos, las reservas solo están disponibles de 08:00 a 20:00.")
            return
        if self.bicicletas_disponibles[hora] > 0:
            self.bicicletas_disponibles[hora] -= 1
            messagebox.showinfo("Reserva realizada", "Ha rentado una bicicleta.")
        else:
            messagebox.showerror("Error en reserva", "Lo sentimos, no hay bicicletas disponibles en esta hora.")

    def cancelar_reserva(self, hora):
        if self.bicicletas_disponibles[hora] < 10:
            self.bicicletas_disponibles[hora] += 1
            messagebox.showinfo("Cancelar reserva", "Reserva cancelada. La bicicleta ha sido devuelta al sistema.")
        else:
            messagebox.showinfo("Cancelar reserva", "No hay reserva para cancelar en esta hora.")

class Interfaz(tk.Tk):
    def __init__(self, sistema):
        super().__init__()
        self.sistema = sistema
        self.title("Sistema de Reservas")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self, text="Nombre de usuario:")
        self.label_password = tk.Label(self, text="Contraseña:")
        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        self.button_login = tk.Button(self, text="Iniciar sesión", command=self.login)
        self.button_register = tk.Button(self, text="Registrarse", command=self.registrar_usuario)

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_login.pack()
        self.button_register.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        usuario_actual = self.sistema.iniciar_sesion(username, password)
        if usuario_actual:
            self.destroy()
            self.menu_inicio(usuario_actual)

    def registrar_usuario(self):
        ventana_registro = tk.Toplevel()
        ventana_registro.title("Registro de usuario")
        ventana_registro.geometry("400x300")

        label_nombre = tk.Label(ventana_registro, text="Nombre:")
        label_nombre.pack()
        entry_nombre = tk.Entry(ventana_registro)
        entry_nombre.pack()

        label_apellido = tk.Label(ventana_registro, text="Apellido:")
        label_apellido.pack()
        entry_apellido = tk.Entry(ventana_registro)
        entry_apellido.pack()

        label_telefono = tk.Label(ventana_registro, text="Teléfono:")
        label_telefono.pack()
        entry_telefono = tk.Entry(ventana_registro)
        entry_telefono.pack()

        label_correo = tk.Label(ventana_registro, text="Correo electrónico:")
        label_correo.pack()
        entry_correo = tk.Entry(ventana_registro)
        entry_correo.pack()

        label_username = tk.Label(ventana_registro, text="Nombre de usuario:")
        label_username.pack()
        entry_username = tk.Entry(ventana_registro)
        entry_username.pack()

        label_password = tk.Label(ventana_registro, text="Contraseña:")
        label_password.pack()
        entry_password = tk.Entry(ventana_registro, show="*")
        entry_password.pack()

        button_confirmar_registro = tk.Button(ventana_registro, text="Registrar", command=lambda: self.sistema.registrar_usuario(entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_correo.get(), entry_username.get(), entry_password.get()))
        button_confirmar_registro.pack()

        button_finalizar_registro = tk.Button(ventana_registro, text="Finalizar registro", command=ventana_registro.destroy)
        button_finalizar_registro.pack()

    def menu_inicio(self, usuario_actual):
        ventana_inicio = tk.Toplevel()
        ventana_inicio.title("Menú de inicio")
        ventana_inicio.geometry("400x300")

        label_bienvenida = tk.Label(ventana_inicio, text=f"Bienvenido, {usuario_actual['username']}!")
        label_bienvenida.pack()

        button_hacer_reserva = tk.Button(ventana_inicio, text="Hacer reserva", command=self.hacer_reserva)
        button_hacer_reserva.pack()

        button_cancelar_reserva = tk.Button(ventana_inicio, text="Cancelar reserva", command=self.cancelar_reserva)
        button_cancelar_reserva.pack()

        button_salir = tk.Button(ventana_inicio, text="Salir", command=self.salir)
        button_salir.pack()

    def hacer_reserva(self):
        ventana_reserva = tk.Toplevel()
        ventana_reserva.title("Hacer reserva")
        ventana_reserva.geometry("400x300")

        label_hora_inicio = tk.Label(ventana_reserva, text="Hora de inicio de la reserva (formato HH):")
        label_hora_inicio.pack()
        entry_hora_inicio = tk.Entry(ventana_reserva)
        entry_hora_inicio.pack()

        label_duracion = tk.Label(ventana_reserva, text="Duración de la reserva (en horas):")
        label_duracion.pack()
        entry_duracion = tk.Entry(ventana_reserva)
        entry_duracion.pack()

        button_confirmar_reserva = tk.Button(ventana_reserva, text="Confirmar reserva", command=lambda: self.sistema.rentar_bici(int(entry_hora_inicio.get()), int(entry_duracion.get())))
        button_confirmar_reserva.pack()

    def cancelar_reserva(self):
        ventana_cancelar_reserva = tk.Toplevel()
        ventana_cancelar_reserva.title("Cancelar reserva")
        ventana_cancelar_reserva.geometry("400x300")

        label_hora_cancelar = tk.Label(ventana_cancelar_reserva, text="Hora de la reserva a cancelar (formato HH):")
        label_hora_cancelar.pack()
        entry_hora_cancelar = tk.Entry(ventana_cancelar_reserva)
        entry_hora_cancelar.pack()

        button_confirmar_cancelar = tk.Button(ventana_cancelar_reserva, text="Confirmar cancelación", command=lambda: self.sistema.cancelar_reserva(int(entry_hora_cancelar.get())))
        button_confirmar_cancelar.pack()

    def salir(self):
        self.destroy()

sistema = Sistema()
app = Interfaz(sistema)
app.mainloop()
