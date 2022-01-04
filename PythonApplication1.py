from tkinter import *
clik=0
def clikerrr(event):
    global clik
    clik+=1
    if clik==10:
        clik=0
    lbl.configure(text=clik)
def clikerrr_rev(event):
    global clik
    clik-=1
    if clik==-10:
        clik=0
    lbl.configure(text=clik)
def txt_to_lbl(event):
    #pass
    text_to_lbl=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END)
def valik():
    #pass
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
def txt_to_lbl1(event):
    #pass
    text_to_lbl1=txt1.get()#From Entry to text
    lbl1.configure(text=text_to_lbl1)
    txt1.delete(0,END)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x600")
nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 12",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE,)#relief=GROOVE,RAISED,SUNKEN
nupp.bind("<Button-1>",clikerrr)#LMB
nupp.bind("<Button-3>",clikerrr_rev)#RMB
lbl=Label(aken,text="",height=4,width=20,font="Arial, 12",fg="black",bg="pink")
txt=Entry(aken,width=20,font="Calibri, 16",fg="black",bg="grey",justify=CENTER)#Однострочный, сделать двустрочным - невозможно, justify=CENTER
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")
var=StringVar()
var.set("uks")
r1=Radiobutton(aken,image=i1,variable=var,value="uks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="kolm",command=valik)

lbl1=Label(aken,text="",height=4,width=20,font="Arial, 12",fg="white",bg="grey")
txt1=Entry(aken,width=20,font="Calibri, 16",fg="black",bg="grey",justify=CENTER, show="*")#Однострочный, сделать двустрочным - невозможно, justify=CENTER
txt1.bind("<Return>",txt_to_lbl1)#Enter

lbl.pack(side=LEFT)
nupp.pack(side=LEFT)#side=LEFT,TOP(по умолчанию),RIGHT
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=RIGHT)
r3.pack(side=BOTTOM)
lbl1.pack(side=BOTTOM)
txt1.pack(side=LEFT)

aken.mainloop()
