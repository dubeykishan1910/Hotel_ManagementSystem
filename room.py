from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1299x560+230+220")


        #variables

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavilable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



        ##############Title
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS ",font=("times new roman",18,"bold"))
        lbl_title.place(x=0,y=0,width=1300,height=50)

        #######################lableFrame###################
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Deatils",font=("times new roman",12,"bold"),padx=2)
        Labelframeleft.place(x=5,y=60,width=425,height=490)


        ###############labels and entrys############
        # customer contact
        lbl_cust_contact=Label(Labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(Labelframeleft,  textvariable=self.var_contact,     width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

        #Featch dta button
        btnFetchData=Button(Labelframeleft,         command=self.Fetch_contact,       text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=335,y=4)

        #check_in Date
        lbl_in_date=Label(Labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #check_out Date
        lbl_out_date=Label(Labelframeleft,text="Check_out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(Labelframeleft,   textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(Labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(Labelframeleft,font=("arial",12,"bold"),   textvariable=self.var_roomtype  ,width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Laxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(Labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        txtRoomAvailable=ttk.Entry(Labelframeleft,   textvariable=self.var_roomavilable,    width=29,font=("arial",13,"bold"))
        txtRoomAvailable.grid(row=4,column=1)

        # Meal
        lblRoomAvailable=Label(Labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=5,column=0,sticky=W)

        txtcheckRoomAvailable=ttk.Entry(Labelframeleft,   textvariable=self.var_meal, width=29,font=("arial",13,"bold"))
        txtcheckRoomAvailable.grid(row=5,column=1)

        # No of Days
        lblNoOfDays=Label(Labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(Labelframeleft,   textvariable=self.var_noofdays, width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)


        # Paid Tax
        lblNoOfDays=Label(Labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(Labelframeleft,   textvariable=self.var_paidtax, width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=7,column=1)


        # Sub total
        lblNoOfDays=Label(Labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(Labelframeleft,   textvariable=self.var_actualtotal, width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=8,column=1)


        # Total cost
        lblIdNumber=Label(Labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=ttk.Entry(Labelframeleft,   textvariable=self.var_total, width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)
        



        #Bill Button
        btnBill=Button(Labelframeleft,text="Bill",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #######buttons

        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        #ADD Btn
        btnAdd=Button(btn_frame,text="Add",        font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupadate=Button(btn_frame,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupadate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",  font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnRest=Button(btn_frame,text="Reset",     font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnRest.grid(row=0,column=3,padx=1)



        #-===========================right side image===================
        img3=Image.open("bad.jpg")
        img3=img3.resize((520,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=760,y=55,width=520,height=200)


        #table frame search system
        Labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("times new roman",12,"bold"),padx=2)
        Labelframeright.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Labelframeright,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Labelframeright,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Labelframeright,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        #search button
        btnsearch=Button(Labelframeright,text="search",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)


        btnshowall=Button(Labelframeright,text="Show All",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)




        #########show data table
        details_table=Frame(Labelframeright,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=180)


        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,columns=("contact","checkinDate","checkoutDate","roomtype","roomavailable",
                                                                    "meal","noOfdays"),xscrollcommand=scroll_x.set,
                                                                    yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="Mobile")
        self.room_Table.heading("checkinDate",text="Check-in")
        self.room_Table.heading("checkoutDate",text="Check-out")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("roomavailable",text="Room No")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfdays",text="NoOfDays")
        

        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkinDate",width=100)
        self.room_Table.column("checkoutDate",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("roomavailable",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfdays",width=100)

        self.room_Table.pack(fill=BOTH,expand=1)


    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s ")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This no Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=('arial',12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=60,y=0)

################gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=('arial',12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=70,y=30)


                ####email
                conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Email:",font=('arial',12,"bold"))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=55,y=60)



if __name__== "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()