from importlib.metadata import entry_points
import tkinter as tk
from tkinter import Entry, filedialog
from script import start


root = tk.Tk()
root.title('XML_label_modifier')
frm=tk.Frame(root,padx=10,pady=10)
frm.grid()

def old():
    global path_to_old
    path_to_old = filedialog.askdirectory(title='Select folder to open the old XML files')
def new():
    global path_to_new
    path_to_new = filedialog.askdirectory(title='Select folder to open the old XML files')
def cont():
    start(path_to_old,path_to_new,entry.get())
    tk.messagebox.showinfo("","New files created successfully")
    root.destroy()

label = tk.Label(frm, text="Select folder that contains the old XML files").grid(row = 0, column=0)
but_open_old= tk.Button(frm,text="Open Folder",command=old).grid(row=0,column=1)
label2 = tk.Label(frm, text="Select folder to save the new XML files" ).grid(row=1,column=0)
but_open_new = tk.Button(frm, text="Open Folder", command=new).grid(row=1,column= 1)

label2 = tk.Label(frm, text="Enter the new size of the image separeted by a comma x,y" ).grid(row=2,column=0)
entry =Entry(frm)
entry.grid(row=2,column=1)

exit = tk.Button(frm, text="Exit", command=root.destroy).grid(row=3,column= 0)
conti = tk.Button(frm, text="Continue", command=cont).grid(row=3,column= 1)

root.mainloop()
