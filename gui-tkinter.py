# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:07:20 2021
@author: anna_eunbi
"""

#import module
from tkinter import *
	
root = Tk()

#widget 1 - Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
runningmenu = Menu(menu)
menu.add_cascade(label='Run', menu=runningmenu)
runningmenu.add_command(label='Debugging w/ running')
runningmenu.add_command(label='Running w/o running')

#widget 2 - Label
w = Label(root, text='Anna Eunbi Seo - 301098222')
w.pack()

#widget 3 - Listbox
Lb = Listbox(root, width=50)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C#')
Lb.insert(4, 'JS')
Lb.pack()

#widget 4 - Radiobutton
v = IntVar()
Radiobutton(root, text='Female', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Male', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='Prefer not to say', variable=v, value=3).pack(anchor=W)

#execute
mainloop()
