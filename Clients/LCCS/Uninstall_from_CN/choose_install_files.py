from tkinter import *
from root_window import *

choose_install_files_frame = Frame(content)

Label(choose_install_files_frame, text='Install File List').pack() #"CN List" label on top
cn_list = Listbox(choose_install_files_frame, width=30) #list of CN
cn_list.pack(side=LEFT) #packed LEFT
add_cn = Button(choose_install_files_frame, text='Add', width=10) #add button to add to CN
remove_cn = Button(choose_install_files_frame, text='Remove', width=10) #remove from list
add_cn.pack() #packed
remove_cn.pack() #packed