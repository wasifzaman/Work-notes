from tkinter import *
from root import content, root

choose_cn_frame = Frame(content)
cn_list = Listbox(choose_cn_frame)
choose_cn_frame.pack()
cn_list.pack(side=LEFT)

add_button = Button(choose_cn_frame, text='Add')
remove_button = Button(choose_cn_frame, text='Remove')
import_button = Button(choose_cn_frame, text='Import')

add_button.pack()
remove_button.pack()
import_button.pack()

