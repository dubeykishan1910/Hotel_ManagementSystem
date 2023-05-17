from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector



class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1299x560+230+220")


        #variables for database entry
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_curst_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_adderss=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()



        ##############Title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"))
        lbl_title.place(x=0,y=0,width=1300,height=50)
        

        #######################lableFrame###################
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatils",font=("times new roman",12,"bold"),padx=2)
        Labelframeleft.place(x=5,y=60,width=425,height=490)

        ###############labels and entrys############
        # custRef
        lbl_cust_ref=Label(Labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(Labelframeleft,      textvariable=self.var_ref     ,width=29,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)


        # cust name
        cname=Label(Labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(Labelframeleft,     textvariable=self.var_curst_name     ,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # mother name
        lblmname=Label(Labelframeleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtcname=ttk.Entry(Labelframeleft,       textvariable=self.var_mother       ,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(Labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(Labelframeleft,       textvariable=self.var_gender                     ,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        #postcode
        lblPostCode=Label(Labelframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode=ttk.Entry(Labelframeleft,    textvariable=self.var_post                     ,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        # mobilenumber
        lblMobile=Label(Labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(Labelframeleft,     textvariable=self.var_mobile                         ,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)


        #email
        lblEmail=Label(Labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtPostCode=ttk.Entry(Labelframeleft,      textvariable=self.var_email                  , font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=6,column=1)

        #nationality
        lblNationality=Label(Labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(Labelframeleft,      textvariable=self.var_nationality        , font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


        #idproof type combobox
        lblIdproof=Label(Labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(Labelframeleft,      textvariable=self.var_id_proof            ,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("AdharCard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #id Number
        lblIdNUMBER=Label(Labelframeleft,font=("arial",12,"bold"),text="ID Number:",padx=2,pady=6)
        lblIdNUMBER.grid(row=9,column=0,sticky=W)

        txtIdnumber=ttk.Entry(Labelframeleft,     textvariable=self.var_id_number         ,font=("arial",13,"bold"),width=29)
        txtIdnumber.grid(row=9,column=1)



        #Address
        lblAddress=Label(Labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress=ttk.Entry(Labelframeleft,        textvariable=self.var_adderss                     ,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)



        #######buttons

        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        #ADD Btn
        btnAdd=Button(btn_frame,text="Add",                     command=self.add_data                 ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupadate=Button(btn_frame,text="Update",               command=self.update                 ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupadate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",                 command=self.Delete                 ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnRest=Button(btn_frame,text="Reset",                     command=self.reset                 ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnRest.grid(row=0,column=3,padx=1)


        #table frame
        Labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("times new roman",12,"bold"),padx=2)
        Labelframeright.place(x=435,y=60,width=860,height=490)

        lblSearchBy=Label(Labelframeright,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Labelframeright,                textvariable=self.search_var,                 font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Labelframeright,                      textvariable=self.txt_search,        font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        #search button
        btnsearch=Button(Labelframeright,text="search",           command=self.search         ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)


        btnshowall=Button(Labelframeright,text="Show All",            command=self.fetch_data,                   font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)




        #########show data table
        details_table=Frame(Labelframeright,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=400)


        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post",
                                                                    "mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,
                                                                    yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")


        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)



        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_curst_name.get(),
                                                                                        self.var_mother.get()    ,
                                                                                        self.var_gender.get()    ,
                                                                                        self.var_post.get()      ,
                                                                                        self.var_mobile.get()    ,
                                                                                        self.var_email.get()     ,
                                                                                        self.var_nationality.get() ,
                                                                                        self.var_id_proof.get()  ,
                                                                                        self.var_id_number.get()  ,
                                                                                        self.var_adderss.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
    

    ##print data on frendside
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_curst_name.set(row[1]),
        self.var_mother.set(row[2])    ,
        self.var_gender.set(row[3])    ,
        self.var_post.set(row[4])      ,
        self.var_mobile.set(row[5])    ,
        self.var_email.set(row[6])     ,
        self.var_nationality.set(row[7]) ,
        self.var_id_proof.set(row[8])  ,
        self.var_id_number.set(row[9])  ,
        self.var_adderss.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Errow","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                            
                                                                                                                                                                            self.var_curst_name.get(),
                                                                                                                                                                            self.var_mother.get()    ,
                                                                                                                                                                            self.var_gender.get()    ,
                                                                                                                                                                            self.var_post.get()      ,
                                                                                                                                                                            self.var_mobile.get()    ,
                                                                                                                                                                            self.var_email.get()     ,
                                                                                                                                                                            self.var_nationality.get() ,
                                                                                                                                                                            self.var_id_proof.get()  ,
                                                                                                                                                                            self.var_id_number.get()  ,
                                                                                                                                                                            self.var_adderss.get(),
                                                                                                                                                                            self.var_ref.get()
                                                                                                                                                                            
                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","customer details has been upadated successfully",parent=self.root)
    


    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System"," Do you want to delete this customer details",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_curst_name.set(""),
        self.var_mother.set("")    ,
        #self.var_gender.set("")    ,
        self.var_post.set("")      ,
        self.var_mobile.set("")    ,
        self.var_email.set("")     ,
        # self.var_nationality.set("") ,
        # self.var_id_proof.set("")  ,
        self.var_id_number.set("")  ,
        self.var_adderss.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@1234",database="firstdb")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where " +str(self.search_var.get()) +" LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.close()




if __name__=="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()