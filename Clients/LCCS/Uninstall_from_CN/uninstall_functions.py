from uninstall_ui import *
from tkinter import filedialog

def set_file_path_entry(entry):
	file_path = filedialog.askopenfile(mode='r')
	if file_path == None: return
	else: file_path = file_path.name
	entry.delete(0, END)
	entry.insert(0, file_path)

def create_file(entry):
	file_path = filedialog.asksaveasfilename(\
		filetypes=[('text files', '.txt'), ('all files', '.*')],\
		defaultextension='.txt')
	if file_path == None: return
	entry.delete(0, END)
	entry.insert(0, file_path)	

#browse_button_text_file.config(command=lambda: set_file_path_entry(text_file))
browse_button_install_file.config(command=lambda: set_file_path_entry(install_file))
browse_button_log_file.config(command=lambda: create_file(log_file))

root.mainloop()