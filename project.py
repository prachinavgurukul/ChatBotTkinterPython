from tkinter import *
from tkinter import*
r=Tk()
r.configure(background="green")

# print(r)

def send():
    send = "Sweety->"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=='Hii' or e.get()=='Hello' or e.get()=="Hi"):
        txt.insert(END,'\n'+'\t'+"Prachi-> Hello!")
    elif (e.get()=='How are you?'):
        txt.insert(END,"\n"+'\t'+"Prachi-> Great! ")
    elif (e.get()=='And you?'):
        txt.insert(END,"\n"+'\t'+"Prachi-> Same as you !")
    elif (e.get()=='I want to see your jewellery collection'):
        txt.insert(END,"\n"+'\t'+"Prachi-> Yes,I'll send you on whatsapp")
    elif (e.get()=='Thank you!'):
        txt.insert(END,"\n"+'\t'+"Prachi-> Please do visit my shop once.")
    elif (e.get()=='Sure! I will.'):
        txt.insert(END,"\n"+'\t'+"Prachi-> Pleasure!")
    else:
        txt.insert(END,"\n"+'\t'"Prachi-> Sorry I didn't get you?")
    e.delete(0,END)
txt = Text(r)
txt.grid(row=0,column=0)
e=Entry(r,width=80,bg="yellow",fg="red")
send=Button(r,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
r.title("CHATBOT")
r.mainloop()

