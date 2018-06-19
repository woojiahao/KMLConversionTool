from tkinter import messagebox

class Logger:
	def err(self, msg: str):
		messagebox.showerror(message = msg)
	def suc(self, msg: str):
		messagebox.showinfo(message = msg)
	def info(self, msg: str):
		messagebox.showinfo(message = msg)