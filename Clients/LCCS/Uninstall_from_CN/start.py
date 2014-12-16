from root import *
from choose_cn import *
from add_deployment import *

choose_cn_button = Button(menu, text='Choose CN')
choose_cn_button.pack()

add_deployment_button = Button(menu, text='Add deployment')
add_deployment_button.pack()

finalize_button = Button(menu, text='Finalize')
finalize_button.pack()

export_script_button = Button(menu, text='Export script')
export_script_button.pack()



choose_cn_frame.pack_forget()


root.mainloop()