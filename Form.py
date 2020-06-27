import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Registration Form")


l=tk.Label(window,text="First Name",width=10).grid(row=0,column=0)
e1=tk.Entry(window,width=40,borderwidth=6)
e1.grid(row=0,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="Last Name",width=10).grid(row=1,column=0)
e2=tk.Entry(window,width=40,borderwidth=6)
e2.grid(row=1,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="Address",width=10).grid(row=2,column=0)
e3=tk.Entry(window,width=40,borderwidth=6)
e3.grid(row=2,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="School",width=10).grid(row=3,column=0)
e4=tk.Entry(window,width=40,borderwidth=6)
e4.grid(row=3,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="Date of birth",width=10).grid(row=4,column=0)
e5=tk.Entry(window,width=40,borderwidth=6)
e5.grid(row=4,column=1,columnspan=5,padx=5,pady=5)


c1=tk.IntVar()
c2=tk.IntVar()
l=tk.Label(window,text="Gender",width=10).grid(row=5,column=0)
ch=tk.Checkbutton(window,text="Male",variable=c1,onvalue=1,offvalue=0).grid(row=5,column=1)
ch1=tk.Checkbutton(window,text="Fe Male",variable=c2,onvalue=1,offvalue=0).grid(row=5,column=2)




l=tk.Label(window,text="Email",width=10).grid(row=6,column=0)
e6=tk.Entry(window,width=40,borderwidth=6)
e6.grid(row=6,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="Phone",width=10).grid(row=7,column=0)
e7=tk.Entry(window,width=40,borderwidth=6)
e7.grid(row=7,column=1,columnspan=5,padx=5,pady=5)

l=tk.Label(window,text="Message",width=10).grid(row=8,column=0)
e8=tk.Entry(window,width=40,borderwidth=6)
e8.grid(row=8,column=1,columnspan=5,padx=5,pady=5)

def button_submit():

    messagebox.showinfo("Submit","you clicked to submit your information")

e=tk.Button(window,text="Submit",width=10,command=button_submit).grid(row=9,column=0)

def button_Reset():

    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)
    e6.delete(0,tk.END)
    e7.delete(0,tk.END)
    e8.delete(0,tk.END)
   

e=tk.Button(window,text="Reset",width=10,command=button_Reset).grid(row=9,column=4)


window.mainloop()
