'''
'''

from tkinter import *

root = Tk()

#container frames
text_entry_frame = Frame(root) #~1. holds CN list filepath and CN list browse button
cn_list_frame = Frame(root) #~2. holds CN list and add and remove to CN list button
install_file_frame = Frame(root) #~3. holds install filepath and installer browse button
log_file_frame = Frame(root) #~4. holds log filepath and log file browse button
finalize_frame = Frame(root) #~5. holds run and exit buttons


#pack container frames vertically
text_entry_frame.pack(pady=2)
cn_list_frame.pack(pady=2)
install_file_frame.pack(pady=2)
log_file_frame.pack(pady=2)
finalize_frame.pack()

#~1. text_entry_frame widgets
Label(text_entry_frame, text='CN list file', width=10).pack(side=LEFT) #"CN list file" label next to text_entry packed LEFT
text_file = Entry(text_entry_frame, width=36) #text file entry
text_file.pack(side=LEFT, padx=5) #packed LEFT
browse_button_text_file = Button(text_entry_frame, text='Browse', width=10) #button to select CN list file
browse_button_text_file.pack(side=LEFT) #packed LEFT

#~2. cn_list_frame widgets
Label(cn_list_frame, text='CN List').pack() #"CN List" label on top
Label(cn_list_frame, text='', width=10).pack(side=LEFT) #for alignment
cn_list = Listbox(cn_list_frame, width=30) #list of CN
cn_list.pack(side=LEFT) #packed LEFT
add_cn = Button(cn_list_frame, text='Add', width=10) #add button to add to CN
remove_cn = Button(cn_list_frame, text='Remove', width=10) #remove from list
add_cn.pack() #packed
remove_cn.pack() #packed

#~3. install_file_frame widgets
Label(install_file_frame, text='Install file', width=10).pack(side=LEFT) #"Install file" label next to install_file packed LEFT
install_file = Entry(install_file_frame, width=36) #install file entry
install_file.pack(side=LEFT, padx=5) #packed LEFT
browse_button_install_file = Button(install_file_frame, text='Browse', width=10) #button to select install file
browse_button_install_file.pack(side=LEFT) #packed LEFT

#~4. log_file_frame widgets
Label(log_file_frame, text='Log file', width=10).pack(side=LEFT) #"Log file" label next to log_file packed LEFT
log_file = Entry(log_file_frame, width=36) #install file entry
log_file.pack(side=LEFT, padx=5) #packed LEFT
browse_button_log_file = Button(log_file_frame, text='Browse', width=10) #button to select install file
browse_button_log_file.pack(side=LEFT) #packed LEFT

#~5. finalize_frame widgets
run_script = Button(finalize_frame, text='Run script', width=60) #button to run script
run_script.pack() #packed
exit = Button(finalize_frame, text='Exit', width=60) #button to exit
exit.pack() #packed