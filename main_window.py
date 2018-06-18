from tkinter import *
from tkinter import filedialog, messagebox

from csv_converter import CSVConverter


class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.__master = master
		self.__init_window()
		self.__selected_file: str = ''
		self.__converter = CSVConverter()

	def __init_window(self):
		self.__master.title('KML Conversion Tool')
		self.__master.geometry('300x100')
		self.pack(fill = BOTH, expand = 1)

		self.__file_name = Label(self, text = 'No file has been selected yet', font = ('Roboto', 12))
		self.__file_name.grid(padx = 20, pady = 20)
		self.__file_name.pack()

		select_file_button = Button(self, text = 'Select File', command = lambda: self.__open_file_dialog())
		select_file_button.pack(fill = X)

		convert_button = Button(self, text = 'Convert File', command = lambda: self.__convert_file())
		convert_button.pack(fill = X)

	def __open_file_dialog(self):
		self.__selected_file = filedialog.askopenfilename(initialdir = "/", title = "Select file",
														  filetypes = (("kml files", "*.kml"), ("all files", "*.*")))

		messagebox.showinfo('Selected File', 'You selected {}'.format(self.__selected_file))

		prefix = self.__selected_file.rfind('/')
		file = self.__selected_file[prefix + 1:] if prefix != -1 else self.__selected_file
		self.__file_name['text'] = file

	def __convert_file(self):
		if not self.__selected_file:
			messagebox.showwarning('Error Converting File', 'Select a file first before converting it')
		else:
			self.__converter.convert(self.__selected_file)


root = Tk()
app = Window(root)
root.mainloop()
