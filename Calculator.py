from tkinter import *
import tkinter.messagebox 
root = Tk()

root.geometry("470x400")
root.resizable(False,False)
root.title("Calculator")

####   Output Screen 
out_value = StringVar()
out_value.set("")
out_screen = Entry(root,textvariable=out_value,font="ariel 30 bold")
out_screen.pack(fill=X,padx=10,pady=10,ipadx=10) 

all_buttons = ['(',')','00','/','C','7','8','9','*','0','4','5','6','-','.','1','2','3','+','=']

### Functions 
def click(event):
    
    global out_value
    try:
        text = event.widget.cget("text")

        if text == '=': 
            if out_value.get().isdigit():
                value = int(out_value.get())
            else:
                value = eval(out_value.get())
            out_value.set(value)
        elif text == 'C':
            out_value.set("")
            out_screen.update() 
        else:
            out_value.set(out_value.get()+text)
            out_screen.update() 
    except:
        tkinter.messagebox.showinfo("Invalid Syntax","Invalid Expression.")
k = 0
for i in range(4):
    f1 = Frame(root,bg='pink')
    for j in range(5):
        b = Button(f1,text=all_buttons[k],font="ariel 20 bold",padx=20,pady=10)
        b.pack(side=LEFT,padx=10,pady=5)
        b.bind('<Button-1>',click)
        k+=1
    f1.pack()

root.mainloop()