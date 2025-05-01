# Import tkinter lib
import tkinter as tk

# Import datetime to get the current time
import datetime

# Create a class for the clock screen
# This class will create a window with the current time
class TelaRelogio:
    def __init__(self, master):
        self.tela = master
        self.hora = tk.Label(
            self.tela, font=("Arial", 26), fg="black")
        self.hora.pack(pady=30, padx=30)
        self.alteracao()
    # This method will update the time every second
    # It will get the current time and update the label
    def alteracao(self):
        now = datetime.datetime.now()
        self.hora['text'] = now.strftime("%H:%M:%S")
        self.tela.after(1000, self.alteracao)

# This method will create the window
janela = tk.Tk()
TelaRelogio(janela)
janela.mainloop()
