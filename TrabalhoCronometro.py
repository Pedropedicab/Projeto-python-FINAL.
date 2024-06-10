import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.is_running = False

        self.time_label = tk.Label(root, text="00:10:00.00", font=("Helvetica", 36))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT)

    def start_stopwatch(self):
        self.is_running = True
        self.update_time()

    def stop_stopwatch(self):
        self.is_running = False

    def reset_stopwatch(self):
        self.is_running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.update_display()

    def update_time(self):
        if self.is_running:
            self.milliseconds += 1
            if self.milliseconds >= 100:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
            self.update_display()
            self.root.after(10, self.update_time)

    def update_display(self):
        time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}.{self.milliseconds:02d}"
        self.time_label.config(text=time_string)

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
