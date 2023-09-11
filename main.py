import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("icon.ico")
        self.title("Calculadora de despidos | Inicio")
        self.geometry("400x200")
        
        self.title = customtkinter.CTkLabel(master=self, text="Calculadora de despidos", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.title.pack(pady=10, padx=10)
        
        self.button_indeterminado = customtkinter.CTkButton(master=self, text="Indeterminado", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.button_indeterminado)
        self.button_plazofijo = customtkinter.CTkButton(master=self, text="Plazo fijo", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.button_plazofijo)

        self.button_indeterminado.pack(pady=10, padx=10)
        self.button_plazofijo.pack(pady=10, padx=10)

    def button_indeterminado(self):
        self.new_window = customtkinter.CTk()
        self.new_window.iconbitmap("icon.ico")
        self.new_window.title("Calculadora de despidos | Indeterminado")
        self.new_window.geometry("500x400")

        self.new_window.mainloop()
    def button_plazofijo(self):
        self.new_window = customtkinter.CTk()
        self.new_window.iconbitmap("icon.ico")
        self.new_window.title("Calculadora de despidos | Plazo Fijo")
        self.new_window.geometry("500x400")

        self.new_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()