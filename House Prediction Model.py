import pickle

from tkinter import *
import tkinter.font
from tkinter import messagebox

windows=Tk()
windows.title("House Price Prediction")
windows.geometry('600x300')
myfont=tkinter.font.Font(family='Helvetica',size=15,weight='bold')
with open("aarush","rb") as file:
    mdl=pickle.load(file)

def predict():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
        messagebox.showerror('Error',"Fill in all entires before submitting!")
    elif a.isnumeric()==False or b.isnumeric()==False or c.isnumeric()==False or d.isnumeric()==False or e.isnumeric()==False:
        messagebox.showerror('Error',"Only Numeric Values are Allowed!")
        if a.isnumeric()==False:
            e1.delete(0,END)
        if b.isnumeric()==False:
            e2.delete(0,END)
        if c.isnumeric()==False:
            e3.delete(0,END)
        if d.isnumeric()==False:
            e4.delete(0,END)
        if e.isnumeric()==False:
            e5.delete(0,END)
    else:
        price=str(mdl.predict([[a,b,c,d,e]]))[1:-1]
        result="The price of your home is $",round(float(price)/73.45,2),"USD"
        messagebox.showinfo("Info",result)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)

l1=Label(windows,font=myfont,text='Area Income: ')
l1.grid(row=0,column=0)
l2=Label(windows,font=myfont,text='House Age (Yrs): ')
l2.grid(row=1,column=0)
l3=Label(windows,font=myfont,text='Number of Rooms: ')
l3.grid(row=2,column=0)
l4=Label(windows,font=myfont,text='Number of Bedrooms: ')
l4.grid(row=3,column=0)
l5=Label(windows,font=myfont,text='Population of Area: ')
l5.grid(row=4,column=0)
e1=Entry(windows,font=myfont,width=15)
e1.grid(row=0,column=1)
e2=Entry(windows,font=myfont,width=15)
e2.grid(row=1,column=1)
e3=Entry(windows,font=myfont,width=15)
e3.grid(row=2,column=1)
e4=Entry(windows,font=myfont,width=15)
e4.grid(row=3,column=1)
e5=Entry(windows,font=myfont,width=15)
e5.grid(row=4,column=1)
b1=Button(windows,font=myfont,text="Submit",command=predict)
b1.grid(row=5,column=0)
windows.mainloop()




