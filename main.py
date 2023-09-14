from tkinter import messagebox
import customtkinter
from tkcalendar import DateEntry
import calendar

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("icon.ico")
        self.title("Calculadora de despidos | Inicio")
        self.geometry("400x160")
        
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
        self.new_window.geometry("400x190")
        
        self.new_window.salary = customtkinter.CTkEntry(master=self.new_window, placeholder_text="Salary")

        self.new_window.startCalender = DateEntry(master=self.new_window, width=12, background='gray', 
                                        foreground='white', borderwidth=2)

        self.new_window.endCalender = DateEntry(master=self.new_window, width=12, background='gray', 
                                        foreground='white')

        self.new_window.button_calculate = customtkinter.CTkButton(master=self.new_window, text="Calcular", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.calculateIndeterminado)

        self.new_window.result = customtkinter.CTkLabel(master=self.new_window, text="", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.new_window.salary.pack(padx=10, pady=10)
        self.new_window.startCalender.pack(padx=10, pady=10)
        self.new_window.endCalender.pack(padx=10, pady=10)
        self.new_window.button_calculate.pack(pady=10, padx=10)
        self.new_window.result.pack(padx=10, pady=10)

        self.new_window.mainloop()
    
    def button_plazofijo(self):
        self.new_window = customtkinter.CTk()
        self.new_window.iconbitmap("icon.ico")
        self.new_window.title("Calculadora de despidos | Plazo Fijo")
        self.new_window.geometry("400x190")

        self.new_window.salary = customtkinter.CTkEntry(master=self.new_window, placeholder_text="Salary")

        self.new_window.startCalender = DateEntry(master=self.new_window, width=12, background='gray', 
                                        foreground='white', borderwidth=2)

        self.new_window.endCalender = DateEntry(master=self.new_window, width=12, background='gray', 
                                        foreground='white', borderwidth=2)

        self.new_window.button_calculate = customtkinter.CTkButton(master=self.new_window, text="Calcular", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.calculatePlazoFijo)
        self.new_window.result = customtkinter.CTkLabel(master=self.new_window, text="", font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.new_window.salary.pack(padx=10, pady=10)
        self.new_window.startCalender.pack(padx=10, pady=10)
        self.new_window.endCalender.pack(padx=10, pady=10)
        self.new_window.button_calculate.pack(pady=10, padx=10)
        self.new_window.result.pack(padx=10, pady=10)

        self.new_window.mainloop()
    
    def calculateIndeterminado(self):
        salaryText = self.new_window.salary.get()
        if salaryText == "":
            messagebox.showinfo("Alerta", "No has ingresado tu salario")
            return
        
        if not salaryText.isdigit():
            messagebox.showinfo("Alerta", "Necesitas ingresar un número")
            return

        salary = int(salaryText)
        startDate = self.new_window.startCalender.get_date()
        endDate = self.new_window.endCalender.get_date()

        if endDate < startDate:
            messagebox.showinfo("Alerta", "La fecha de finalización no puede ser anterior a la de inicio")
            return

        daysDifference = (endDate - startDate).days + 1

        if calendar.isleap(startDate.year):
            divisor = 366
        else:
            divisor = 365

        result = round(salary * 1.5 * (daysDifference / divisor))
        
        if daysDifference <= 91:
            messagebox.showinfo("Alerta", "No tienes derecho a una remuneración")
            self.new_window.result.configure(text=f"Tu remuneración es de: S/. {result}")
            return
        

        if result > salary * 12:
            messagebox.showinfo("Alerta", "Tu remuneración pasó el límite")  
            return
        else:
            self.new_window.result.configure(text=f"Tu remuneración es de: S/. {result}")

    def calculatePlazoFijo(self):
        salaryText = self.new_window.salary.get()
        if salaryText == "":
            messagebox.showinfo("Alerta", f"No has ingresado tu salario")
            return
        
        if not salaryText.isdigit():
            messagebox.showinfo("Alerta", "Necesitas ingresar un número")
            return

        salary = int(salaryText)

        startDate = self.new_window.startCalender.get_date()
        endDate = self.new_window.endCalender.get_date()

        if endDate < startDate:
            messagebox.showinfo("Alerta", f"La fecha de finalización no puede ser anterior a la de inicio")
            return

        daysDifference = (endDate - startDate).days + 1

        if daysDifference > 365:
            messagebox.showinfo("Alerta", f"No puedes calcular cuando pase más de 1 año")
            return

        result = round(salary * 1.5 * (daysDifference / 12))

        if result > salary * 12:
            messagebox.showinfo("Alerta", f"Tu remuneración pasó el límite")  
            return
        else:
            self.new_window.result.configure(text=f"Tu remuneración es de: S/. {result}")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()