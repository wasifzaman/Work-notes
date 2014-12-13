from root_window import *
from choose_cn import choose_cn_frame
from choose_install_files import choose_install_files_frame
from choose_remove_programs import choose_remove_programs_frame
from choose_run_scripts import choose_run_scripts_frame
from tkinter import *



choose_cn_frame.pack()
#choose_install_files_frame.pack()
#choose_remove_programs_frame.pack()
#choose_run_scripts_frame.pack()


choose_cn_button = Button(menu, text='Choose CN')
run_button = Button(menu, text='Run')
finalize_button = Button(menu, text='Finalize')



root.mainloop()