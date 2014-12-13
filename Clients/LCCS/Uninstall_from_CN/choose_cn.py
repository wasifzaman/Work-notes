from tkinter import *
from root_window import *

choose_cn_frame = Frame(content)

Label(choose_cn_frame, text='CN List').pack() #"CN List" label on top
cn_list = Listbox(choose_cn_frame, width=30) #list of CN
cn_list.pack(side=LEFT) #packed LEFT
add_cn = Button(choose_cn_frame, text='Add', width=10) #add button to add to CN
remove_cn = Button(choose_cn_frame, text='Remove', width=10) #remove from list
import_cn = Button(choose_cn_frame, text='Import', width=10) #import CN from file
export_cn = Button(choose_cn_frame, text='Export', width=10) #export CN to file
add_cn.pack() #packed
remove_cn.pack() #packed
import_cn.pack() #packed
export_cn.pack() #packed