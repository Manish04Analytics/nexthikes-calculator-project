from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

Entry(root, textvariable=equation, font=("Arial",20)).grid(row=0,column=0,columnspan=4)

Button(root,text="7",width=8,height=3,command=lambda:press("7")).grid(row=1,column=0)
Button(root,text="8",width=8,height=3,command=lambda:press("8")).grid(row=1,column=1)
Button(root,text="9",width=8,height=3,command=lambda:press("9")).grid(row=1,column=2)
Button(root,text="+",width=8,height=3,command=lambda:press("+")).grid(row=1,column=3)

Button(root,text="4",width=8,height=3,command=lambda:press("4")).grid(row=2,column=0)
Button(root,text="5",width=8,height=3,command=lambda:press("5")).grid(row=2,column=1)
Button(root,text="6",width=8,height=3,command=lambda:press("6")).grid(row=2,column=2)
Button(root,text="-",width=8,height=3,command=lambda:press("-")).grid(row=2,column=3)

Button(root,text="1",width=8,height=3,command=lambda:press("1")).grid(row=3,column=0)
Button(root,text="2",width=8,height=3,command=lambda:press("2")).grid(row=3,column=1)
Button(root,text="3",width=8,height=3,command=lambda:press("3")).grid(row=3,column=2)
Button(root,text="*",width=8,height=3,command=lambda:press("*")).grid(row=3,column=3)

Button(root,text="C",width=8,height=3,command=clear).grid(row=4,column=0)
Button(root,text="0",width=8,height=3,command=lambda:press("0")).grid(row=4,column=1)
Button(root,text="=",width=8,height=3,command=equal).grid(row=4,column=2)
Button(root,text="/",width=8,height=3,command=lambda:press("/")).grid(row=4,column=3)

root.mainloop()