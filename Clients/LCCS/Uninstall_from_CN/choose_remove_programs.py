from tkinter import *
from root_window import *

choose_remove_programs_frame = Frame(content)

Label(choose_remove_programs_frame, text='Remove programs').pack() #"CN List" label on top
cn_list = Listbox(choose_remove_programs_frame, width=30) #list of CN
cn_list.pack(side=LEFT) #packed LEFT
add_cn = Button(choose_remove_programs_frame, text='Add', width=10) #add button to add to CN
remove_cn = Button(choose_remove_programs_frame, text='Remove', width=10) #remove from list
query_cn = Button(choose_remove_programs_frame, text='Query CN', width=10) #query CN for product names
add_cn.pack() #packed
remove_cn.pack() #packed
query_cn.pack() #packed