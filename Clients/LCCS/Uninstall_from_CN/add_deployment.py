from tkinter import *
from root import content, root

add_deployment_frame = Frame(content)
add_deployment_frame.pack()

dep_options_frame = Frame(add_deployment_frame)
dep_values_frame = Frame(add_deployment_frame)
dep_options_frame.pack()
dep_values_frame.pack()

deployment_var = StringVar()
deployment_var.set('test')

deployment_menu = OptionMenu(dep_options_frame, deployment_var, 
							'test', 'test2')
deployment_menu.pack()

def show_dep_options(*args):
	print(deployment_var.get())
	return

deployment_var.trace('w', show_dep_options)

 '''
cn_list = Listbox(choose_cn_frame)
choose_cn_frame.pack()
cn_list.pack(side=LEFT)

add_button = Button(choose_cn_frame, text='Add')
remove_button = Button(choose_cn_frame, text='Remove')
import_button = Button(choose_cn_frame, text='Import')

add_button.pack()
remove_button.pack()
import_button.pack()
'''