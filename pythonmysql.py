# import mysql.connector
# conn=mysql.connector.connect(host='localhost',username='root',password='Pass@1234',database='firstdb')
# my_cursor=conn.cursor()

# conn.commit()
# conn.close()

# print("connection succesfully created  ")
from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HotelMangementSystem")
        self.root.geometry("1550x800+0+0")

        img1=Image.open("hotel.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

        #====================logo========================
        img2=Image.open("logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)

        #=============title==============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"))
        lbl_title.place(x=0,y=140,width=1500,height=50)

        #===================frame-===================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #====================menu========================

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250)

        #===================btn frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
#35
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",      command=self.roombooking,        width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

#-===========================right side image===================
        img3=Image.open("bad.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=225,y=0,width=1310,height=590)

#=======================down image======================
        img4=Image.open("om.jpg")
        img4=img4.resize((230,350),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=240,width=230,height=350)
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
 

        

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

# a=[1,1]
# c=0
# l=[]
# while(a):
#     i=0
    
#     li=[]
#     for j in range(1,len(a)):
#         if a[i]==a[j]:
            
#             li.append(a[:j+1])
#             l.append(a[:j+1])
#             break
#     i=i+1
#     try:
#         for i in range(len(li[0])):
#             a.pop(0)
#     except:
#         li.append(a[:])
#         a.pop(0)
#     print(l)
#     print(li)
# print(len(l))
        
    





