import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("325x225")

        self.create_widgets()

    def create_widgets(self):
        self.label_altura = tk.Label(self.root, text="Altura (m):")
        self.label_altura.grid(row=0, column=0, padx=10, pady=10)
        self.entry_altura = tk.Entry(self.root)
        self.entry_altura.grid(row=0, column=1, padx=10, pady=10)

        self.label_peso = tk.Label(self.root, text="Peso (kg):")
        self.label_peso.grid(row=1, column=0, padx=10, pady=10)
        self.entry_peso = tk.Entry(self.root)
        self.entry_peso.grid(row=1, column=1, padx=10, pady=10)

        self.button_calcular_IMC = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calcular_IMC.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.label_category = tk.Label(self.root, text="")
        self.label_category.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            altura = float(self.entry_altura.get())
            peso = float(self.entry_peso.get())

            if altura <= 0 or peso <= 0:
                raise ValueError("Altura e peso devem ser valores positivos.")

            bmi = peso / (altura ** 2)
            self.label_resultado.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif bmi <= 24.99:
            category = "Peso normal"
        elif bmi <= 29.99:
            category = "Sobrepeso"
        else:
            category = "Obeso"

        self.label_category.config(text=f"Você está na categoria: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
