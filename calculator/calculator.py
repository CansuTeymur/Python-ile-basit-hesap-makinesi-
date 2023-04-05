import tkinter as tk


frame=tk.Tk()
frame.title("Calculator")
frame.geometry("350x330")
frame.resizable(False,False)


def addition():
    entry_result.delete(0,"end")
    n1=int(entry_number1.get())
    n2=int(entry_number2.get())
    result=n1+n2
    entry_result.insert(0,result)
    entry_number1.delete(0,"end")
    entry_number2.delete(0,"end")
    
def subtraction():
    entry_result.delete(0,"end")
    n1=int(entry_number1.get())
    n2=int(entry_number2.get())
    result=n1-n2
    entry_result.insert(0,result)
    entry_number1.delete(0,"end")
    entry_number2.delete(0,"end")

def multiplication():
    entry_result.delete(0,"end")
    n1=int(entry_number1.get())
    n2=int(entry_number2.get())
    result=n1*n2
    entry_result.insert(0,result)
    entry_number1.delete(0,"end")
    entry_number2.delete(0,"end")

def division():
    entry_result.delete(0,"end")
    n1=int(entry_number1.get())
    n2=int(entry_number2.get())
    result=float(n1/n2)
    entry_result.insert(0,result)
    entry_number1.delete(0,"end")
    entry_number2.delete(0,"end")


entry_number1=tk.Entry(frame,width=27)
entry_number1.place(x=110,y=82)
entry_number2=tk.Entry(frame,width=27)
entry_number2.place(x=110,y=112)
entry_result=tk.Entry(frame,width=18,font="9")
entry_result.place(x=110,y=140)


label=tk.Label(frame,text="Calculator",fg="green",width=11,font="Vergana 17 bold").place(x=100,y=20)

lbl_number1=tk.Label(frame,text="number 1 : ",font="8")
lbl_number1.place(x=20,y=80)
lbl_number2=tk.Label(frame,text="number 2 : ",font="8")
lbl_number2.place(x=20,y=110)
lbl_result=tk.Label(frame,text="result : ",font="9")
lbl_result.place(x=20,y=140)



button_1=tk.Button(frame,text="+",width=6,bg="orange",font="15",command=addition)
button_1.place(x=30,y=200)
button_2=tk.Button(frame,text="-",width=6,bg="orange",font="15",command=subtraction)
button_2.place(x=100,y=200)
button_3=tk.Button(frame,text="*",width=6,bg="orange",font="15",command=multiplication)
button_3.place(x=170,y=200)
button_4=tk.Button(frame,text="/",width=6,bg="orange",font="15",command=division)
button_4.place(x=240,y=200)


frame.mainloop()
