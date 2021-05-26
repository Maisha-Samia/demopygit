from tkinter import Tk , Label , Frame , Entry , Button , GROOVE , X , Y , LabelFrame, Scrollbar, VERTICAL, Text, \
    RIGHT,BOTH,SUNKEN, IntVar, StringVar, END
# Checkbutton ,
import random
def bg_color(args):
    pass

class Bill_App:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Clothing Billing.Software")
        bg_color = "#074463"
        title = Label(self.root , text="Clothing Billing Software" , bd=12 , relief=GROOVE , bg=bg_color , fg="white" ,
                      font=("times new roman" , 30 , "bold") , pady=2).pack(fill=X)
        #=======variables========
        #=======Women's shirt clothes=======
        self.product_no=IntVar()
        self.Sh_s=IntVar()
        self.Sh_m = IntVar()
        self.Sh_l = IntVar()
        self.Sh_xl = IntVar()
        self.Sh_xxl = IntVar()
        #=======Women's pants clothes=======
        self.product_no = IntVar()
        self.Pan_s = IntVar()
        self.Pan_m = IntVar()
        self.Pan_l = IntVar()
        self.Pan_xl = IntVar()
        self.Pan_xxl = IntVar()
        # =======Women's necessary=======
        self.product_no = IntVar()
        self.saree = IntVar()
        self.tops = IntVar()
        self.kurti = IntVar()
        self.shalwar_kameez = IntVar()
        self.suits = IntVar()
        self.shoes = IntVar()
        # =======Kid's clothes=======
        self.product_no = IntVar()
        self.newborngirls = IntVar()
        self.newbornboys = IntVar()
        self.juniorgirls = IntVar()
        self.juniorboys = IntVar()
        # =======Total Product Price & Tax Variable=======
        self.shirts_price=StringVar()
        self.pants_price = StringVar()
        self.women_necessary_price = StringVar()
        self.kids_clothes_price = StringVar()
        self.total_tax=StringVar()
        ## =====Customer=====
        self.c_name=StringVar()
        self.c_phn = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # =====Customer Detail Frame=====
        F1 = LabelFrame(self.root , bd=10 , relief=GROOVE , text="Customer Details" ,
                        font=("times new roman" , 18 , "bold") , fg="#D2B700" , bg=bg_color)
        F1.place(x=0 , y=80 , relwidth=1)

        cname_lbl = Label(F1 , text="Customer Name" , bg=bg_color , fg="white" ,
                          font=("times new roman" , 18 , "bold")).grid(row=0 , column=0 , padx=8 , pady=5)
        cname_txt = Entry(F1 , width=30 ,textvariable=self.c_name, font="arial 15" , bd=7).grid(row=0 , column=1 , padx=8 , pady=5)

        cphn_lbl = Label(F1 , text="Customer Phone No." , bg=bg_color , fg="white" ,
                         font=("times new roman" , 18 , "bold")).grid(row=0 , column=2 , padx=8 , pady=5)
        cphn_txt = Entry(F1 , width=25 ,textvariable=self.c_phn, font="arial 15" , bd=7).grid(row=0 , column=3 , padx=8 , pady=5)

        cbill_lbl = Label(F1 , text="Bill No." , bg=bg_color , fg="white" ,
                           font=("times new roman" , 18 , "bold")).grid(row=0 , column=4 , padx=8 , pady=5)
        cbill_txt = Entry(F1 , width=15 ,textvariable=self.search_bill, font="arial 15" , bd=7).grid(row=0 , column=5 , padx=8 , pady=5)

        bill_btn = Button(F1 , text="Search" , width=7 , bd=7 , font="arial 12 bold").grid(row=0 , column=6 , padx=15 ,
                                                                                           pady=5)


        # =====Women's clothes Frame======
        F2 = LabelFrame(self.root , bd=10 , relief=GROOVE , text="Women's Clothes" ,
                        font=("times new eoman" , 18 , "bold") ,
                        fg="#D2B700" , bg=bg_color)
        F2.place(x=0 , y=170 , width=260 , height=455)

        shirts_lbl = Label(F2 , text="Product NO:" , bg=bg_color , fg="#000D24" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(
            row=0 , column=0 , padx=5 , pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.product_no, font=("times new roman" , 16 , "bold") , bd=5).grid(row=0 , column=1 ,
                                                                                               padx=5 ,
                                                                                               pady=5)

        # =====shirts_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5).grid(row=4, column=1, padx=10,pady=10)

        shirts_lbl = Label(F2, text="S" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=2 , column=0 , padx=5 , pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.Sh_s, font=("times new roman" , 16 , "bold") , bd=5).grid(row=2 , column=1 ,
                                                                                               padx=5 ,
                                                                                               pady=5)
        shirts_lbl = Label(F2 , text="Shirts Size" , bg=bg_color , fg="silver" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=0 , padx=5 , pady=5)
        shirts_lbl = Label(F2 , text="Quantity" , bg=bg_color , fg="silver" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=1 , padx=5 , pady=5)


        # =====shirts_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5).grid(row=6, column=1, padx=10,pady=10)


        shirts_lbl = Label(F2 , text="M" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=4 , column=0 , padx=5 , pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.Sh_m, font=("times new roman" , 16 , "bold") , bd=5).grid(row=4 , column=1 ,
                                                                                               padx=5 , pady=5)
        shirts_lbl = Label(F2 , text="L" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=5 , column=0 , padx=5 , pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.Sh_l, font=("times new roman" , 16 , "bold") , bd=5).grid(row=5 , column=1 ,
                                                                                               padx=5 ,
                                                                                               pady=5)
        shirts_lbl = Label(F2 , text="XL" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=6 , column=0 , padx=5 , pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.Sh_xl, font=("times new roman" , 16 , "bold") , bd=5).grid(row=6, column=1 ,
                                                                                               padx=5 ,
                                                                                               pady=5)
        shirts_lbl = Label(F2 , text="XXL" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=7, column=0 , padx=5, pady=5)
        shirts_txt = Entry(F2 , width=6 ,textvariable=self.Sh_xxl, font=("times new roman" , 16 , "bold") , bd=5).grid(row=7 , column=1 ,
                                                                                               padx=5 ,
                                                                                               pady=5)

        # ======Women's pants clothes Frame======
        F3 = LabelFrame(self.root , bd=10 , relief=GROOVE , text=" " , font=("times new roman" , 18 , "bold") ,
                        fg="#D2B700" , bg=bg_color)
        F3.place(x=260 , y=170 , width=260 , height=455)

        pants_lbl = Label(F3, text="Product NO:" , bg=bg_color , fg="#000D24" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(
            row=0 , column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.product_no, font=("times new roman" , 16 , "bold") , bd=5).grid(row=0 , column=1 ,
                                                                                              padx=5 ,
                                                                                              pady=5)
        pants_lbl = Label(F3 , text="S" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=2 , column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.Pan_s, font=("times new roman" , 16 , "bold") , bd=5).grid(row=2 , column=1 ,
                                                                                             padx=5 , pady=5)
        pants_lbl = Label(F3 , text="Pants Size" , bg=bg_color , fg="silver" ,
                          font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=0 , padx=5 , pady=5)
        pants_lbl = Label(F3 , text="Quantity" , bg=bg_color , fg="silver" ,
                          font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=1 , padx=5 , pady=5)


        # =====pants_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5).grid(row=6, column=1, padx=10,pady=10)


        pants_lbl = Label(F3 , text="M" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=3 , column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.Pan_m, font=("times new roman" , 16 , "bold") , bd=5).grid(row=3 , column=1 ,
                                                                                              padx=5 , pady=5)
        pants_lbl = Label(F3 , text="L" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=4 , column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.Pan_l, font=("times new roman" , 16 , "bold") , bd=5).grid(row=4, column=1 ,
                                                                                              padx=5 ,
                                                                                              pady=5)
        pants_lbl = Label(F3 , text="XL" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=5, column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.Pan_xl, font=("times new roman" , 16 , "bold") , bd=5).grid(row=5, column=1 ,
                                                                                              padx=5 ,
                                                                                              pady=5)
        pants_lbl = Label(F3 , text="XXL" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=6 , column=0 , padx=5 , pady=5)
        pants_txt = Entry(F3 , width=6 ,textvariable=self.Pan_xxl, font=("times new roman" , 16 , "bold") , bd=5).grid(row=6, column=1 ,padx=5,pady=5)

        # ======Women's necessary Frame======
        F4 = LabelFrame(self.root , bd=10 , relief=GROOVE , text="Women's necessary" ,
                        font=("times new roman" , 18 , "bold") , fg="#D2B700" ,
                        bg=bg_color)
        F4.place(x=520 , y=170 , width=300 , height=455)
        necessary_lbl = Label(F4 , text="Product NO:" , bg=bg_color , fg="#000D24" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(
            row=0 , column=0 , padx=5 , pady=5)
        necessary_txt = Entry(F4 , width=6 ,textvariable=self.product_no, font=("times new roman" , 16 , "bold") , bd=5).grid(row=0 , column=1 ,
                                                                                              padx=5 ,
                                                                                              pady=5)

        saree_lbl = Label(F4 , text="Saree" , bg=bg_color , fg="#000D24" ,
                          font=("times new roman" , 16 , "bold" ,)).grid(row=2 , column=0 , padx=5 , pady=5)

        saree_txt = Entry(F4 , width=8 ,textvariable=self.saree, font=("times new roman" , 16 , "bold") , bd=5).grid(row=2 , column=1 ,
                                                                                             padx=5 , pady=5)

        necessary_lbl = Label(F4 , text="Quantity" , bg=bg_color , fg="silver" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=1 , padx=5 , pady=5)

        tops_lbl = Label(F4, text="Tops" , bg=bg_color , fg="#000D24" , font=("times new roman" , 16 , "bold" ,)).grid(
            row=3 , column=0 , padx=5 , pady=5)
        tops_txt = Entry(F4 , width=8 ,textvariable=self.tops, font=("times new roman" , 16 , "bold") , bd=5).grid(row=3 , column=1 ,padx=5,
                                                                                             pady=5)

        kurtis_lbl = Label(F4 , text="Kurti" , bg=bg_color , fg="#000D24" ,
                           font=("times new roman" , 16 , "bold" ,)).grid(
            row=4 , column=0 , padx=5, pady=5)
        kurtis_txt = Entry(F4 , width=8,textvariable=self.kurti, font=("times new roman" , 16 , "bold") , bd=5).grid(row=4 , column=1 ,padx=5 ,
                                                                                               pady=5)
        shalwarkameez_lbl = Label(F4 , text="Shalwar kameez" , bg=bg_color , fg="#000D24" ,
                                  font=("times new roman" , 16 , "bold" ,)).grid(row=5 , column=0 , padx=5, pady=5)
        shalwarkameez_txt = Entry(F4 , width=8,textvariable=self.shalwar_kameez, font=("times new roman" , 16 , "bold") , bd=5).grid(row=5, column=1 ,padx=5 ,
                                                                                                      pady=5)
        suits_lbl = Label(F4 , text="Suits" , bg=bg_color , fg="#000D24" ,
                          font=("times new roman" , 16 , "bold" ,)).grid(
            row=6 , column=0 , padx=5, pady=5)
        suits_txt = Entry(F4 , width=8 ,textvariable=self.suits, font=("times new roman" , 16 , "bold") , bd=5).grid(row=6 , column=1 ,
                                                                                              padx=5,
                                                                                              pady=5)
        shoes_lbl = Label(F4 , text="Shoes" , bg=bg_color , fg="#000D24" ,
                          font=("times new roman" , 16 , "bold" ,)).grid(
            row=7, column=0 , padx=5, pady=5)
        shoes_txt = Entry(F4 , width=8 ,textvariable=self.shoes, font=("times new roman" , 16 , "bold") , bd=5).grid(row=7 , column=1 ,padx=5 ,
                                                                                              pady=5)
        # =====Kid's clothes Frame======
        F5 = LabelFrame(self.root , bd=10 , relief=GROOVE , text="Kid's Clothes" ,
                        font=("times new eoman" , 18 , "bold") ,
                        fg="#D2B700" , bg=bg_color)
        F5.place(x=820 , y=170 , width=300 , height=455)

        necessary_lbl = Label(F5 , text="Product NO:" , bg=bg_color , fg="#000D24" ,
                              font=("times new roman" , 16 , "bold" ,)).grid(
            row=0 , column=0 , padx=5 , pady=5)
        necessary_txt = Entry(F5 , width=6 ,textvariable=self.product_no, font=("times new roman" , 16 , "bold") , bd=5).grid(row=0 , column=1 ,
                                                                                                 padx=5 ,
                                                                                                 pady=5)

        newborngirls_lbl = Label(F5 , text="Newborn Girls" , bg=bg_color , fg="#000D24" ,
                                 font=("times new roman" , 16 , "bold" ,)).grid(row=2 , column=0 , padx=5 , pady=5)

        newborngirls_txt = Entry(F5 , width=8 ,textvariable=self.newborngirls, font=("times new roman" , 16 , "bold") , bd=5).grid(row=2 , column=1 ,
                                                                                                    padx=5 , pady=5)

        necessary_lbl = Label(F5, text="Quantity" , bg=bg_color , fg="silver" ,
                              font=("times new roman" , 16 , "bold" ,)).grid(row=1 , column=1 , padx=5 , pady=5)


        newbornboys_lbl = Label(F5 , text="Newborn boys" , bg=bg_color , fg="#000D24" ,
                                font=("times new roman" , 16 , "bold" ,)).grid(
            row=3 , column=0 , padx=5, pady=5)
        newbornboys_txt = Entry(F5 , width=8 ,textvariable=self.newbornboys, font=("times new roman" , 16 , "bold") , bd=5).grid(row=3 , column=1 ,
                                                                                                    padx=5 ,
                                                                                                    pady=5)

        juniorgirls_lbl = Label(F5 , text="Junior Girls" , bg=bg_color , fg="#000D24" ,
                                font=("times new roman" , 16 , "bold" ,)).grid(
            row=4 , column=0 , padx=5 , pady=5)
        juniorgirls_txt = Entry(F5 , width=8 ,textvariable=self.juniorgirls, font=("times new roman" , 16 , "bold") , bd=5).grid(row=4 , column=1,padx=5 ,
                                                                                                    pady=5)
        juniorboys_lbl = Label(F5, text="Junior Boys" , bg=bg_color , fg="#000D24" ,
                               font=("times new roman" , 16 , "bold" ,)).grid(
            row=5 , column=0 , padx=5, pady=5)
        juniorboys_txt = Entry(F5 , width=8,textvariable=self.juniorboys, font=("times new roman" , 16 , "bold") , bd=5).grid(row=5 , column=1 ,padx=5,
                                                                                                   pady=5)


        # =====Bill Area======
        F6 = Frame(self.root , bd=10 , relief=GROOVE)
        F6.place(x=1120 , y=170 , width=420 , height=455)

        bill_title = Label(F6 , text="Bill Area" , font="arial 15 bold" , bd=7 , relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F6 , orient=VERTICAL)
        self.txtarea = Text(F6 , yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT , fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH , expand=1)

        #====ButtonFrame========

        F7=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",18,"bold"),fg="#D2B700",bg=bg_color,)
        F7.place(x=0,y=625,relwidth=1,height=200)
        m1_lbl=Label(F7,text="Total Shirts Price",bg=bg_color,fg="#000D24",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=7,pady=1,sticky="w")
        m1_txt=Entry(F7,width=16,textvariable=self.shirts_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=1)
        m2_lbl = Label(F7,text="Total Pants Price",bg=bg_color,fg="#000D24",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=7,pady=1,sticky="w")
        m2_txt = Entry(F7,width=16 ,textvariable=self.pants_price, font="arial 10 bold" , bd=7 , relief=SUNKEN).grid(row=1 , column=1 , padx=5 ,
                                                                                         pady=1)
        m3_lbl = Label(F7 , text="Total Women's necessary Price" , bg=bg_color , fg="#000D24" ,
                       font=("times new roman" , 16 , "bold")).grid(row=2 , column=0 , padx=7 , pady=1 , sticky="w")
        m3_txt = Entry(F7 , width=16 ,textvariable=self.women_necessary_price, font="arial 10 bold" , bd=7 , relief=SUNKEN).grid(row=2 , column=1 , padx=5 ,
                                                                                         pady=1)
        m4_lbl = Label(F7 , text="Total Kid's Clothes Price" , bg=bg_color , fg="#000D24" ,
                       font=("times new roman" , 16 , "bold")).grid(row=3 , column=0 , padx=7 , pady=1 , sticky="w")
        m4_txt = Entry(F7 , width=16 ,textvariable=self.kids_clothes_price, font="arial 10 bold" , bd=7 , relief=SUNKEN).grid(row=3 , column=1 , padx=5 ,
                                                                                         pady=1)

        c1_lbl = Label(F7 , text="Total Tax" , bg=bg_color , fg="#000D24" ,
                       font=("times new roman" , 16 , "bold")).grid(row=0 , column=2 , padx=7 , pady=1 , sticky="w")
        c1_txt = Entry(F7 , width=16 ,textvariable=self.total_tax, font="arial 10 bold" , bd=7 , relief=SUNKEN).grid(row=0 , column=3 , padx=5 ,
                                                                                         pady=1)


        btn_F=Frame(F7,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=700,height=135)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="#000D24",fg="white",bd=6,pady=15,width=8,font="arial 15 bold").grid(row=0,column=0,padx=25,pady=20)
        GBill_btn = Button(btn_F , text="Genrate Bill",command=self.bill_area, bg="#000D24" , fg="white" , bd=6 , pady=15 , width=10 ,
                           font="arial 15 bold").grid(row=0 , column=1 , padx=25 , pady=20)
        Clear_btn = Button(btn_F , text="Clear" , bg="#000D24" , fg="white" , bd=6 , pady=15 , width=8 ,
                           font="arial 15 bold").grid(row=0 , column=2 , padx=25 , pady=20)
        Exit_btn = Button(btn_F , text="Exit" , bg="#000D24" , fg="white" , bd=6 , pady=15 , width=8 ,
                           font="arial 15 bold").grid(row=0 , column=3 , padx=25, pady=20)
        self.welcome_bill()

    def total(self):
        self.s_s_p=self.Sh_s.get()*700
        self.s_m_p = self.Sh_m.get() * 700
        self.s_l_p = self.Sh_l.get() * 700
        self.s_xl_p = self.Sh_xl.get() * 700
        self.s_xxl_p = self.Sh_xxl.get() * 700

        self.total_shirts_price=float (
                                  self.s_s_p+
                                  self.s_m_p+
                                  self.s_l_p+
                                  self.s_xl_p+
                                  self.s_xxl_p
                                )
        self.shirts_price.set("Rs. "+str(self.total_shirts_price))

        self.p_s_p = self.Pan_s.get() * 800
        self.p_m_p = self.Pan_m.get() * 800
        self.p_l_p = self.Pan_l.get() * 800
        self.p_xl_p = self.Pan_xl.get() * 800
        self.p_xxl_p = self.Pan_xxl.get() * 800

        self.total_pants_price = float(
                                self.p_s_p+
                                self.p_m_p+
                                self.p_l_p+
                                self.p_xl_p+
                                self.p_xxl_p
        )
        self.pants_price.set("Rs. "+str(self.total_pants_price))

        self.wn_s_p = self.saree.get() * 1200
        self.wn_t_p = self.tops.get() * 800
        self.wn_k_p = self.kurti.get() * 1900
        self.wn_sk_p = self.shalwar_kameez.get() * 2000
        self.wn_su_p = self.suits.get() * 1000
        self.wn_sh_p = self.shoes.get() * 1500

        self.total_women_necessary_price = float(
            self.wn_s_p+
            self.wn_t_p+
            self.wn_k_p+
            self.wn_sk_p+
            self.wn_su_p+
            self.wn_sh_p
        )
        self.women_necessary_price.set("Rs. "+str(self.total_women_necessary_price))

        self.k_nbg_p = self.newborngirls.get() * 500
        self.k_nbb_p = self.newbornboys.get() * 500
        self.k_jg_p = self.juniorgirls.get() * 700
        self.k_jb_p = self.juniorboys.get() * 700

        self.total_kids_clothes_price = float(
            self.k_nbg_p+
            self.k_nbb_p+
            self.k_jg_p+
            self.k_jb_p
        )
        self.kids_clothes_price.set("Rs. " + str(self.total_kids_clothes_price))

        self.total_tax.set("Rs. "+str(round((self.total_tax*0.05),2)))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t     Welcome Webcode Reatil\n")
        self.txtarea.insert(END,f"\n\n  Bill Number  : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n  Customer Name  : {self.c_name.get()}")
        self.txtarea.insert(END , f"\n  Phone Number  : {self.c_phn.get()}")
        self.txtarea.insert(END , f"\n  ============================================")
        self.txtarea.insert(END , f"\n  Products\t\t\tQTY\t     Price")
        self.txtarea.insert(END , f"\n  ============================================")
    def bill_area(self):
        self.welcome_bill()
        #======shirts=========
        if self.Sh_s.get()!=0:
            self.txtarea.insert(END,f"\n  Sh_S\t\t         {self.Sh_s.get()}\t\t      {self.s_s_p}")
        if self.Sh_m.get()!=0:
            self.txtarea.insert(END,f"\n  Sh_M\t\t         {self.Sh_m.get()}\t\t      {self.s_m_p}")
        if self.Sh_l.get() != 0:
            self.txtarea.insert(END , f"\n  Sh_L\t\t         {self.Sh_l.get()}\t\t      {self.s_l_p}")
        if self.Sh_xl.get() != 0:
            self.txtarea.insert(END , f"\n  Sh_XL\t\t         {self.Sh_xl.get()}\t\t      {self.s_xl_p}")
        if self.Sh_xxl.get() != 0:
            self.txtarea.insert(END , f"\n  Sh_XXL\t\t         {self.Sh_xxl.get()}\t\t      {self.s_xxl_p}")

        # ======pants=========
        if self.Pan_s.get() != 0:
            self.txtarea.insert(END , f"\n  Pan_S\t\t         {self.Pan_s.get()}\t\t      {self.p_s_p}")
        if self.Pan_m.get() != 0:
            self.txtarea.insert(END , f"\n  Pan_M\t\t         {self.Pan_m.get()}\t\t      {self.p_m_p}")
        if self.Pan_l.get() != 0:
            self.txtarea.insert(END , f"\n  Pan_L\t\t         {self.Pan_l.get()}\t\t      {self.p_l_p}")
        if self.Pan_xl.get() != 0:
            self.txtarea.insert(END , f"\n  Pan_XL\t\t         {self.Pan_xl.get()}\t\t      {self.p_xl_p}")
        if self.Pan_xxl.get() != 0:
            self.txtarea.insert(END , f"\n  Pan_XXL\t\t         {self.Pan_xxl.get()}\t\t      {self.p_xxl_p}")

        # ======Women's necessary========
        if self.saree.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_SAREE\t\t         {self.saree.get()}\t\t      {self.wn_s_p}")
        if self.tops.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_TOPS\t\t         {self.tops.get()}\t\t      {self.wn_t_p}")
        if self.kurti.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_KURTI\t\t         {self.kurti.get()}\t\t      {self.wn_k_p}")
        if self.shalwar_kameez.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_SHALWAR KAMEEZ\t\t    {self.shalwar_kameez.get()}\t           {self.wn_sk_p}")
        if self.suits.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_SUITS\t\t         {self.suits.get()}\t\t      {self.wn_su_p}")
        if self.shoes.get() != 0:
            self.txtarea.insert(END , f"\n  Wn_SHOES\t\t         {self.shoes.get()}\t\t      {self.wn_sh_p}")

        # ======Kid's clothes========
        if self.newborngirls.get() != 0:
            self.txtarea.insert(END , f"\n  K_newborngirls\t\t       {self.newborngirls.get()}\t\t       {self.k_nbg_p}")
        if self.newbornboys.get() != 0:
            self.txtarea.insert(END , f"\n  K_newbornboys\t\t        {self.newbornboys.get()}\t\t       {self.k_nbb_p}")
        if self.juniorgirls.get() != 0:
            self.txtarea.insert(END , f"\n  K_juniorgirls\t\t        {self.juniorgirls.get()}\t\t       {self.k_jg_p}")
        if self.juniorboys.get() != 0:
            self.txtarea.insert(END , f"\n  K_juniorboys\t\t         {self.juniorboys.get()}\t\t       {self.k_jb_p}")


root = Tk()
obj = Bill_App(root)
root.mainloop()
