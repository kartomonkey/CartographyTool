from tkinter import ttk
from tkinter import *
import tkinter as tk


root = Tk()
root.title("Delete BaseCamp Cache")
root.state('zoomed')
# root.iconphoto(True,PhotoImage(file='Icon.png'))


# ____________________________________________________________
# FRAMES
#
photoHome = PhotoImage(file='J:\Sources\OSM\Dokumentation\Images\CartoTool\Home_40x40.png')
photoOSM = PhotoImage(file='J:\Sources\OSM\Dokumentation\Images\CartoTool\OSM_144x144.gif')
photoTrashcan = PhotoImage(file='J:\Sources\OSM\Dokumentation\Images\CartoTool\Trashcan.png').subsample(10, 10)
#photoTrashcan2 = photoTrashcan.subsample(10, 10)
vartext='Home'

s = ttk.Style()
s.configure('TLabelframe', background='gray22', borderwith=20, labelanchor='center')
s.configure('TLabelframe.Label', background='gray22', foreground='gray99', font=('Helvetica', 15))

mainframe = ttk.LabelFrame(root, text=vartext)
mainframe.grid(row=1, column=1,columnspan=3, ipadx=500, ipady=500)
lframe1 = ttk.LabelFrame(mainframe, text='OSM Importer', style='TLabelframe')
lframe1.grid(row=1, column=2, sticky=(N, W), pady=20, padx=50)

lframe2 = ttk.LabelFrame(mainframe, text='Others', style='TLabelframe')
lframe2.grid(row=2, column=2, sticky=(N, W), pady=20, padx=50)

buttonHome = tk.Button(mainframe, image=photoHome, bg='gray22', relief="flat",activebackground='gray18')
buttonHome.grid(column=0, row=1, sticky=(N))

buttonTA = tk.Button(mainframe, text='TopoActive')
buttonTA.grid(column=0, row=1, sticky=(N), pady= 50)

buttonOSM = tk.Button(lframe1, text="OSM Importer", font=('Helvetica', 12),  compound= 'top',image=photoOSM, bg='gray22', fg='gray99', relief="flat", activebackground='gray18', activeforeground='gray99')
buttonOSM.grid(column=1, row=2, ipadx=5, ipady=5, padx=10)

buttonOSM2 = tk.Button(lframe1, text='OSM Importer v2', font=('Helvetica', 12),  compound= 'top',image=photoOSM, bg='gray22', fg='gray99', relief="flat", activebackground='gray18', activeforeground='gray99')
buttonOSM2.grid(column=2, row=2, ipadx=5, ipady=5, padx=10)

buttonBcmp = tk.Button(lframe2, text='Delete BaseCamp Cache', font=('Helvetica', 10),  compound= 'top',image=photoTrashcan, bg='gray22', fg='gray99', relief="flat", activebackground='gray18', activeforeground='gray99')
buttonBcmp.grid(column=1, row=1, ipadx=5, ipady=5, padx=10)


root.mainloop()
