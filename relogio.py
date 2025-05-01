import tkinter as tk

import datetime

class TelaRelogio:
    def __init__(self, master):
        self.tela = master
        self.hora = tk.Label(
            self.tela, font=("Arial", 26), fg="black")
        self.hora.pack(pady=30, padx=30)
        self.alteracao()
    
    def alteracao(self):
        now = datetime.datetime.now()
        self.hora['text'] = now.strftime("%H:%M:%S")
        self.tela.after(1000, self.alteracao)

janela = tk.Tk()
TelaRelogio(janela)
janela.mainloop()