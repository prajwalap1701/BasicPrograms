from tkinter import *
from tkinter import filedialog, messagebox

def browseFiles():
    try:
        filename = filedialog.askopenfilename(initialdir="/", title="Select a DBC File",
                                              filetypes=(("DBC files", "*.dbc*"), ("all files", "*.*")))

    except:
        messagebox.showerror("Error", "Unable to load File")

master = Tk()
master.title("DBC to Excel Converter")
master.minsize(width=400, height=200)

l1=Label(master, text="Input CAN DBC File").grid(row=0)
l2=Label(master, text="Message CSV File").grid(row=1)
l3=Label(master, text="Signals CSV File").grid(row=2)
l4=Label(master, text="Output File Name").grid(row=3)

e1 = Entry(master, width=50)
e2 = Entry(master, width=50)
e3 = Entry(master, width=50)
e4 = Entry(master, width=50)

button_explore = Button(master, text="Browse File", command= browseFiles).grid(row=0, column=2)
# browse_msg_csv = Button(master, text="Browse File", command= browse_msg_csv).grid(row=1, column=2)
# browse_sig_csv = Button(master, text="Browse File", command= browse_sig_csv).grid(row=2, column=2)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

Button(master, text='Convert',command='').grid(row=4, column=1,pady=4)
# Button(master, text='Reset', command=resetTextInput).grid(row=4, column=1, sticky=W,pady=4)
password = "zaCEhgf"
mainloop()
