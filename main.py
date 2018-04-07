
from Tkinter import *

top = Tk()
#top.geometry("1590x900")
top.configure(bg="lightblue")
import tkMessageBox

#******************************************************************************************************************
pin_main=0     
def helloCallBack():
     global pin_main
     print(pin_main)
     top1=Tk()
     top1.configure(bg="aqua")
     top1.geometry("1590x900")
     label1=Label(top1,text="\n\n\n\n\n\n\n\n\n\n",bg="aqua")
     label1.grid(row=0,column=0)
     label2=Label(top1,text="\t"*18,bg="aqua")
     label2.grid(row=1,column=1)
     B2=Button(top1,text="BALANCE ENQIRY",bg="white",font=("arial",20,"bold"),command=showbalance)
     B2.grid(row=1,column=0)

     B3=Button(top1,text="CASH WITHDRAWL",bg="white",font=("arial",20,"bold"),command=cashwithdrawl)
     B3.grid(row=1,column=2)

     label3=Label(top1,text="\n\n\n\n\n\n",bg="aqua")
     label3.grid(row=2,column=0)
     label4=Label(top1,text="\t"*18,bg="aqua")
     label4.grid(row=3,column=1)

     B4=Button(top1,text="PIN CHANGE",bg="white",font=("arial",20,"bold"),command=pinchange)
     B4.grid(row=3,column=0)

     B5=Button(top1,text="DEPOSIT",bg="white",font=("arial",20,"bold"),command=deposit)
     B5.grid(row=3,column=2)
     #top.destroy()
     top1.mainloop()
#***************************************************************************************************************    
label1=Label(top,text="\n\n\n\n\n\n\n\n\n\n",bg="lightblue")
label1.grid(row=0,column=0)

label2=Label(top,text="enter 4 digit pin\t\t\t",bg="lightblue",font=("arial",20,"bold"))
label2.grid(row=1,column=0)
E1 = Entry(top, bd =5,show="*")
E1.grid(row=1,column=1)

label3=Label(top,text="\n\n\n\n\n\n\n\n\n\n",bg="lightblue")
label3.grid(row=0,column=0)


#**************************************************************************************************************

def checkpin():
     global pin_main
     pin=E1.get()
     if pin=="":
          tkMessageBox.showerror("error","please enter the pin")
          return
     num=int(pin)
     f1=open("pack.txt","r+")
     flag=1
     for i in f1:
          if(num==int(i[:4])):
               pin_main=num
               top.destroy()
               helloCallBack()
               flag=0
     f1.close()
     if flag:
          tkMessageBox.showerror("failed","incorrect pin")
B =Button(top, text ="submit", command = checkpin)
B.grid(row=2,column=0,columnspan=2)
#*****************************************************************************************************************
number_pins=3
def showbalance():
     global pin_main,number_pins
     f1=open("pack.txt","r")
     amount=""
     for j in range(number_pins):
          i=f1.readline()
          if (int(i[:4])==pin_main):
               amount=i[5:]
     tkMessageBox.showinfo("balance","your current balance is "+amount)
     f1.close()
       
#****************************************************************************************************************

def deposit():
     def dep():
          global pin_main
          pins=[]
          amounts=[]
          f1=open("pack.txt","r")
          for i in f1:
               pins.append(i[:4])
               amounts.append(i[5:])
          f1.close()
          new_money=int(E2.get())
          index1=pins.index(str(pin_main))
          new_amount=int(amounts[index1])+new_money
          amounts[index1]=str(new_amount)
          f2=open("pack.txt","w")
          for i in range(len(pins)):
               f2.write(pins[i]+" "+amounts[i])
          f2.close()
          successful()
          
     top2=Tk()
     #top2.geometry("1390x900")

     top2.configure(bg="grey")
     label1=Label(top2,text="\n\n\n\n\n\n\n\n\n\n",bg="grey")
     label1.grid(row=0,column=0)
     label2=Label(top2,text="enter the amount you want to deposit\t\t\t",bg="lightblue",font=("arial",16,"bold"))
     label2.grid(row=1,column=0)
     
     E2 = Entry(top2, bd =5)
     E2.grid(row=1,column=1)
     B1 =Button(top2, text ="submit", command = dep)
     B1.grid(row=2,column=0,columnspan=2)
     top2.mainloop()
     
#*******************************************************************************************************************
def  successful():
   
    tkMessageBox.showinfo("result","money deposited")
#******************************************************************************************************************
def pinchange():
    def pin_change():
          global pin_main
          pins=[]
          amounts=[]
          f1=open("pack.txt","r")
          for i in f1:
               if i=="\n":
                    continue
               pins.append(i[:4])
               amounts.append(i[5:])
          f1.close()
          index1=pins.index(str(pin_main))
          passw=E2.get()
          conf_passw=E3.get()
          old_passw=E1.get()
          if not old_passw==str(pin_main):
               tkMessageBox.showerror("error","CURRENT PIN DOES'NT MATCH")
          elif not passw==conf_passw:
               tkMessageBox.showerror("error","PLEASE ENTER THE SAME PIN")
          else:
               pins[index1]=passw
               pin_main=int(passw)
               f2=open("pack.txt","w")
               for i in range(len(pins)):
                    f2.write(pins[i]+" "+amounts[i])
               f2.close()
               tkMessageBox.showinfo("success","pin updated")
    top4 = Tk()
    top4.geometry("1590x900")
    top4.configure(bg="lightblue")

    label1=Label(top4,text="\n\n\n",bg="lightblue")
    label1.grid(row=0,column=0)
    label2=Label(top4,text="OLD PIN",bg="lightblue",font=("arial",20,"bold"))
    label2.grid(row=1,column=0)
    E1 = Entry(top4, bd =5,show="*")
    E1.grid(row=1,column=1)


    label3=Label(top4,text="\n\n",bg="lightblue")
    label3.grid(row=2,column=0)
    label4=Label(top4,text="NEW PIN",bg="lightblue",font=("arial",20,"bold"))
    label4.grid(row=3,column=0)
    E2 = Entry(top4, bd =5,show="*")
    E2.grid(row=3,column=1)

    label4=Label(top4,text="\n\n",bg="lightblue")
    label4.grid(row=4,column=0)
    label5=Label(top4,text="CONFIRM PIN",bg="lightblue",font=("arial",20,"bold"))
    label5.grid(row=4,column=0)
    E3 = Entry(top4, bd =5,show="*")
    E3.grid(row=4,column=1)
    submit=Button(top4,text="submit",command=pin_change)
    submit.grid(row=5,column=0,columnspan=2)
    top4.mainloop()
     
#*******************************************************************************************************************
    
def cashwithdrawl():
    top5 = Tk()
    top5.geometry("1590x900")
    top5.configure(bg="lightblue")
    label1=Label(top5,text="\n\n\n\n\n\n\n\n\n\n",bg="lightblue")
    label1.grid(row=0,column=0)

    label2=Label(top5,text="enter the amount\t\t\t",bg="lightblue",font=("arial",20,"bold"))
    label2.grid(row=1,column=0)
    E1 = Entry(top5, bd =5)
    E1.grid(row=1,column=1)
    B =Button(top5, text ="submit", command = trans)
    B.grid(row=2,column=0,columnspan=2)
    top5.mainloop()
#*******************************************************************************************************************
def trans():
         tkMessageBox.showinfo("proceesing","please collect the amount")
#******************************************************************************************************************         
top.mainloop()

