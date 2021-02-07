from tkinter import *
from tkinter import messagebox
import math
import random               
import os

class System_App:
  
  def __init__(self, root):
    self.root = root
    self.root.geometry("1350x700+0+0")
    self.root.title("Computer Electronics Retail System")
    bg_color = "gray"


    # Frame : Computer Electronics Retail System 
    title = Label(self.root, text = "COMPUTER - ELECTRONICS  RETAIL  SYSTEM", bd = 12, relief = GROOVE, bg = "black", fg = "green",font = ("times new roman", 30, "bold"), pady = 2).pack(fill = X)


    # VARIABLES : Computer Parts
    self.monitor = IntVar()
    self.hdd_ssd = IntVar()
    self.ram = IntVar()
    self.l_charger = IntVar()
    self.kboard_mouse = IntVar()
    self.antivirus = IntVar()


    # VARIABLES : Electronics
    self.tv = IntVar()
    self.fridge = IntVar()
    self.air_con = IntVar()
    self.fans = IntVar()
    self.t_light = IntVar()
    self.bulbs = IntVar()


    # VARIABLES : Peripherals
    self.cables = IntVar()
    self.switches = IntVar()
    self.routers = IntVar()
    self.e_phones = IntVar()
    self.p_drives = IntVar()
    self.r_kit = IntVar()


    # Total Product Price and Tax variables
    self.com_parts_price = StringVar()
    self.electronics_price = StringVar()
    self.peripherals_price = StringVar()

    self.com_parts_tax = StringVar()
    self.electronics_tax = StringVar()
    self.peripherals_tax = StringVar()


    # CUSTOMER INFORMATION
    self.c_name = StringVar()
    self.c_phone = StringVar()

    self.bill_no = StringVar()
    x = random.randint(100000, 999999)
    self.bill_no.set(str(x))
    self.search_bill = StringVar()



    # Frame :   <<<< Customer Details  >>>>
    F1 = LabelFrame(self.root, bd = 10, relief = GROOVE ,text = "Customer Details", font = ("times new roman", 15, "bold"), fg = "maroon", bg = bg_color)
    F1.place(x=0, y=75, relwidth=1)
    
    # Label: Customer name
    cname_lbl = Label(F1, text =  "Customer Name", bg = bg_color, fg = "black", font = ("times new roman", 18, "bold")).grid(row = 0, column = 0, padx = 20, pady = 5)
    cname_txt = Entry(F1, width = 15, textvariable = self.c_name, font= "arial 15", bd = 7, relief = SUNKEN).grid(row =0, column = 1, padx = 10, pady = 5)

    # Label : Customer Phone Number
    cphn_lbl = Label(F1, text =  "Phone No.", bg = bg_color, fg = "black", font = ("times new roman", 18, "bold")).grid(row = 0, column = 2, padx = 20, pady = 5)
    cphn_txt = Entry(F1, width = 15, textvariable = self.c_phone, font= "arial 15", bd = 7, relief = SUNKEN).grid(row =0, column = 3, padx = 10, pady = 5)

    # Label : Customer Bill Number
    c_bill_lbl = Label(F1, text =  "Bill Number", bg = bg_color, fg = "black", font = ("times new roman", 18, "bold")).grid(row = 0, column = 4, padx = 20, pady = 5)
    c_bill_txt = Entry(F1, width = 15, textvariable = self.search_bill, font= "arial 15", bd = 7, relief = SUNKEN).grid(row =0, column = 5, padx = 10, pady = 5)

    # Button : Search
    bill_btn = Button(F1, text = "Search", command = self.find_bill, width = 10, bd =7, font = "arial 12 bold").grid(row = 0, column = 6, padx = 10, pady = 10)


    # FRAME :  <<<< BILL MENU >>>> 
    F6 = LabelFrame(self.root, bd = 10, relief = GROOVE ,text = "Bill Menu", font = ("times new roman", 15, "bold"), fg = "maroon", bg = bg_color)
    F6.place(x=0, y=175, relwidth = 1, height = 140)

    # m1 : Total Computer Parts Price 
    m1_lbl = Label(F6, text = "Total Computer Parts Price", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 0, column = 0, padx = 20, pady = 1, sticky = "w")

    m1_txt = Entry(F6, width = 18, textvariable = self.com_parts_price, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 0, column = 1, padx = 10, pady = 1)

    # m2 : Total Electronics Price 
    m2_lbl = Label(F6, text = "Total Electronics Price", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 1, column = 0, padx = 20, pady = 1, sticky = "w")

    m2_txt = Entry(F6, width = 18, textvariable = self.electronics_price, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 1, column = 1, padx = 10, pady = 1)

    # m3 : Total Peripherals Price
    m3_lbl = Label(F6, text = "Total Peripherals Price", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 2, column = 0, padx = 20, pady = 1, sticky = "w")

    m3_txt = Entry(F6, width = 18, textvariable = self.peripherals_price, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 2, column = 1, padx = 10, pady = 1)


    # FRAME :  <<<< TAX >>>>
    # c1 : Computer Parts Tax
    c1_lbl = Label(F6, text = "Computer Parts Tax", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 0, column = 2, padx = 20, pady = 1, sticky = "w")

    c1_txt = Entry(F6, width = 18, textvariable = self.com_parts_tax, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 0, column = 3, padx = 10, pady = 1)

    # c2 : Electronics Tax
    c2_lbl = Label(F6, text = "Electronics Tax", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 1, column = 2, padx = 20, pady = 1, sticky = "w")

    c2_txt = Entry(F6, width = 18, textvariable = self.electronics_tax, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 1, column = 3, padx = 10, pady = 1)

    # c3 : Peripherals Tax
    c3_lbl = Label(F6, text = "Peripherals Tax", bg = bg_color, fg = "black",font = ("times new roman", 14, "bold")).grid(row = 2, column = 2, padx = 20, pady = 1, sticky = "w")

    c3_txt = Entry(F6, width = 18, textvariable = self.peripherals_tax, font = "arial 10 bold", bd = 7, relief = SUNKEN).grid(row = 2, column = 3, padx = 10, pady = 1)


    # FRAME :  <<<< GREEN BUTTONS >>>> 
    btn_F = Frame(F6, bd = 7, relief = GROOVE)
    btn_F.place(x = 750, width = 580, height = 105)

    Total_btn = Button(btn_F, command = self.total, text = "Total", bg = "green", fg = "white", bd = 2, pady = 15, width = 10, font = "arial 14 bold").grid(row = 0, column = 0, padx = 5, pady = 5)

    Gen_Bill_btn = Button(btn_F, text = "Generate Bill", command = self.bill_area, bg = "green", fg = "white", bd = 2, pady = 15, width = 10, font = "arial 14 bold").grid(row = 0, column = 1, padx = 5, pady = 5)

    Clear_btn = Button(btn_F, text = "Clear", command = self.clear_data, bg = "green", fg = "white", bd = 2, pady = 15, width = 10, font = "arial 14 bold").grid(row = 0, column = 2, padx = 5, pady = 5)

    Exit_btn = Button(btn_F, text = "Exit", command = self.Exit_app, bg = "green", fg = "white", bd = 2, pady = 15, width = 10, font = "arial 14 bold").grid(row = 0, column = 3, padx = 5, pady = 5)


    # Frame :   <<<< COMPUTER PARTS >>>>
    F2 = LabelFrame(self.root, bd = 10, relief = GROOVE ,text = "Computer Parts", font = ("times new roman", 15, "bold"), fg = "maroon", bg = bg_color)
    F2.place(x = 5, y = 315, width = 330, height = 380)

    # 1 : Monitor
    bath_lbl = Label(F2, text = "Monitor", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
    bath_txt = Entry(F2, width = 10, textvariable = self.monitor, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 0, column = 1, padx = 10, pady = 10)

    # 2 : HDD/SSD
    hdd_ssd_lbl = Label(F2, text = "HDD / SSD", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
    hdd_ssd_txt = Entry(F2, width = 10, textvariable = self.hdd_ssd, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 1, column = 1, padx = 10, pady = 10)

    # 3 : RAM
    Face_w_lbl = Label(F2, text = "RAM", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
    Face_w_txt = Entry(F2, width = 10, textvariable = self.ram, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 2, column = 1, padx = 10, pady = 10)

    # 4 : Laptop Charger
    Hair_s_lbl = Label(F2, text = "Laptop Charger", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
    Hair_s_txt = Entry(F2, width = 10, textvariable = self.l_charger, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 3, column = 1, padx = 10, pady = 10)

    # 5 : Keyboard/Mouse
    Hair_g_lbl = Label(F2, text = "Keyboard/Mouse", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
    hair_g_txt = Entry(F2, width = 10, textvariable = self.kboard_mouse, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 4, column = 1, padx = 10, pady = 10)

    # 6 : Antivirus
    Body_lbl = Label(F2, text = "Antivirus", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
    BOdy_txt = Entry(F2, width = 10, textvariable = self.antivirus, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 5, column = 1, padx = 10, pady = 10)


    # Frame :   <<<< ELECTRONICS >>>>
    F3 = LabelFrame(self.root, bd = 10, relief = GROOVE ,text = "Electronics", font = ("times new roman", 15, "bold"), fg = "maroon", bg = bg_color)
    F3.place(x = 340, y = 315, width = 325, height = 380)

    # 1 : TV
    g1_lbl = Label(F3, text = "TV", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
    g1_txt = Entry(F3, width = 10, textvariable = self.tv, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 0, column = 1, padx = 10, pady = 10)

    # 2 : Refridgerator
    g2_lbl = Label(F3, text = "Refridgerator", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
    g2_txt = Entry(F3, width = 10, textvariable = self.fridge, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 1, column = 1, padx = 10, pady = 10)

    # 3 : Air Conditioner
    g3_lbl = Label(F3, text = "Air Conditioner", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
    g3_txt = Entry(F3, width = 10, textvariable = self.air_con, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 2, column = 1, padx = 10, pady = 10)

    # 4 : Fans
    g4_lbl = Label(F3, text = "Fans", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
    g4_txt = Entry(F3, width = 10, textvariable = self.fans, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 3, column = 1, padx = 10, pady = 10)

    # 5 : Tubelights
    g5_lbl = Label(F3, text = "Tubelights", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
    g5_txt = Entry(F3, width = 10, textvariable = self.t_light, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 4, column = 1, padx = 10, pady = 10)

    # 6 : Bulbs
    g6_lbl = Label(F3, text = "Bulbs", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
    g6_txt = Entry(F3, width = 10, textvariable = self.bulbs, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 5, column = 1, padx = 10, pady = 10)


    # Frame :   <<<< Peripherals >>>>
    F4 = LabelFrame(self.root, bd = 10, relief = GROOVE ,text = "Peripherals", font = ("times new roman", 15, "bold"), fg = "maroon", bg = bg_color)
    F4.place(x = 670, y = 315, width = 325, height = 380)

    # c1 : Cables
    c1_lbl = Label(F4, text = "Cables", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
    c1_txt = Entry(F4, width = 10, textvariable = self.cables, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 0, column = 1, padx = 10, pady = 10)

    # c2 : Switches
    c2_lbl = Label(F4, text = "Switches", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
    c2_txt = Entry(F4, width = 10, textvariable = self.switches, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 1, column = 1, padx = 10, pady = 10)

    # c3 : Routers
    c3_lbl = Label(F4, text = "Routers", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
    c3_txt = Entry(F4, width = 10, textvariable = self.routers, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 2, column = 1, padx = 10, pady = 10)

    # c4 : Earphones
    c4_lbl = Label(F4, text = "Earphones", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
    c4_txt = Entry(F4, width = 10, textvariable = self.e_phones, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 3, column = 1, padx = 10, pady = 10)

    # c5 : Pendrives
    c5_lbl = Label(F4, text = "Pendrives", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
    c5_txt = Entry(F4, width = 10, textvariable = self.p_drives, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 4, column = 1, padx = 10, pady = 10)

    # c6 : Repair Kit
    c6_lbl = Label(F4, text = "Repair Kit", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "black").grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
    c6_txt = Entry(F4, width = 10, textvariable = self.r_kit, font = ("times new roman", 16, "bold"), bd = 5, relief = SUNKEN).grid(row = 5, column = 1, padx = 10, pady = 10)


    # FRAME :  <<<< BILL >>>>
    F5 = Frame(self.root, bd = 10, relief = GROOVE)
    F5.place(x = 1000, y = 315, width = 350, height = 380)

    # Header Title : Bill 
    bill_title = Label(F5, text = "Bill", font = "arial 15 bold", bd = 7, relief = GROOVE).pack(fill = X)

    # ScrollBar and TextArea
    scroll_y = Scrollbar(F5, orient = VERTICAL)
    self.txtarea = Text(F5, yscrollcommand = scroll_y.set)
    scroll_y.pack(side = RIGHT, fill = Y)
    scroll_y.config(command = self.txtarea.yview)
    self.txtarea.pack(fill = BOTH, expand = 1)
  

    self.welcome()


  def total(self):

      # Total Computer Parts Pricing
      self.cp_m_p = self.monitor.get() * 3000
      self.cp_hd_p = self.hdd_ssd.get() * 6000  
      self.cp_r_p = self.ram.get() * 2500  
      self.cp_c_p = self.l_charger.get() * 500  
      self.cp_km_p = self.kboard_mouse.get() * 300  
      self.cp_a_p = self.antivirus.get() * 1450

      self.total_com_parts_price = float(  
                          self.cp_m_p +
                          self.cp_hd_p + 
                          self.cp_r_p +
                          self.cp_c_p + 
                          self.cp_km_p +
                          self.cp_a_p  
                          )
      self.com_parts_price.set("Rs. " + str(self.total_com_parts_price))

      self.cp_tax = round((self.total_com_parts_price*0.01), 2)

      self.com_parts_tax.set("Rs. " + str(self.cp_tax))


      # Total Electronics Pricing
      self.e_tv_p = self.tv.get() * 12000
      self.e_f_p = self.fridge.get() * 4500 
      self.e_ac_p = self.air_con.get() * 7000
      self.e_fs_p = self.fans.get() * 1200
      self.e_l_p = self.t_light.get() * 250
      self.e_b_p = self.bulbs.get() * 60

      self.total_electronics_price = float(  
                          self.e_tv_p + 
                          self.e_f_p + 
                          self.e_ac_p + 
                          self.e_fs_p + 
                          self.e_l_p + 
                          self.e_b_p
                          )
      self.electronics_price.set("Rs. " + str(self.total_electronics_price))

      self.e_tax = round((self.total_electronics_price*0.02), 2)

      self.electronics_tax.set("Rs. " + str(self.e_tax))


      # Total Peripherals Pricing
      self.p_c_p = self.cables.get() * 120  
      self.p_s_p = self.switches.get() * 100  
      self.p_r_p = self.routers.get() * 1500  
      self.p_e_p = self.e_phones.get() * 900  
      self.p_pd_p = self.p_drives.get() * 600 
      self.p_k_p = self.r_kit.get() * 1200 

      self.total_peripherals_price = float(  
                          self.p_c_p + 
                          self.p_s_p + 
                          self.p_r_p + 
                          self.p_e_p + 
                          self.p_pd_p + 
                          self.p_k_p 
                          )
      self.peripherals_price.set("Rs. " + str(self.total_peripherals_price))

      self.p_tax = round((self.total_peripherals_price*0.02), 2)

      self.peripherals_tax.set("Rs. " + str(self.p_tax))
  
      self.Total_bill = float(
                        self.total_com_parts_price +
                        self.total_electronics_price + 
                        self.total_peripherals_price +
                        self.cp_tax +
                        self.e_tax +
                        self.p_tax 
                        )


  def welcome(self):
      self.txtarea.delete('1.0', END)
      self.txtarea.insert(END, "  Computer Electronics Retail System\n")
      self.txtarea.insert(END, f"\n Bill Number   : {self.bill_no.get()}")
      self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
      self.txtarea.insert(END, f"\n Phone Number  : {self.c_phone.get()}")
      self.txtarea.insert(END, f"\n======================================")
      self.txtarea.insert(END, f"\n PRODUCTS\t\tQTY\t\tPRICE")
      self.txtarea.insert(END, f"\n======================================")


  def bill_area(self):

    # Customer Details Empty Error
    if self.c_name.get() == "" or self.c_phone.get() == "":
        messagebox.showerror("Error", "Cutsomer Details not filled.")

    # Bill Menu Empty Error
    elif self.com_parts_price.get() == "Rs. 0.0" and self.electronics_price.get() == "Rs. 0.0" and self.peripherals_price.get() == "Rs. 0.0" or self.com_parts_price.get() == "" and self.electronics_price.get() == "" and self.peripherals_price.get() == "":
        messagebox.showerror("Error", "Products Not Selected.")


    else:
        self.welcome()

        # Computer Parts Bill Generation
        if self.monitor.get() != 0:
          self.txtarea.insert(END, f"\n Monitor\t\t{self.monitor.get()}\t\t{self.cp_m_p}")    

        if self.hdd_ssd.get() != 0:
          self.txtarea.insert(END, f"\n HDD/SSD\t\t{self.hdd_ssd.get()}\t\t{self.cp_hd_p}")  

        if self.ram.get() != 0:
          self.txtarea.insert(END, f"\n RAM\t\t{self.ram.get()}\t\t{self.cp_r_p}") 

        if self.l_charger.get() != 0:
          self.txtarea.insert(END, f"\n Laptop Chargers\t\t{self.l_charger.get()}\t\t{self.cp_c_p}")   

        if self.kboard_mouse.get() != 0:
          self.txtarea.insert(END, f"\n Keyboard / Mouse\t\t{self.kboard_mouse.get()}\t\t{self.cp_km_p}")

        if self.antivirus.get() != 0:
          self.txtarea.insert(END, f"\n Antivirus\t\t{self.antivirus.get()}\t\t{self.cp_a_p}")              


        # Electronics Bill Generation
        if self.tv.get() != 0:
          self.txtarea.insert(END, f"\n TV\t\t{self.tv.get()}\t\t{self.e_tv_p}")    

        if self.fridge.get() != 0:
          self.txtarea.insert(END, f"\n Refridgerator\t\t{self.fridge.get()}\t\t{self.e_f_p}")  

        if self.air_con.get() != 0:
          self.txtarea.insert(END, f"\n Air Conditioner\t\t{self.air_con.get()}\t\t{self.e_ac_p}") 

        if self.fans.get() != 0:
          self.txtarea.insert(END, f"\n Fans\t\t{self.fans.get()}\t\t{self.e_fs_p}")   

        if self.t_light.get() != 0:
          self.txtarea.insert(END, f"\n Tubelight\t\t{self.t_light.get()}\t\t{self.e_l_p}")

        if self.bulbs.get() != 0:
          self.txtarea.insert(END, f"\n Bulb\t\t{self.bulbs.get()}\t\t{self.e_b_p}")   

    
        # Peripherals Bill Generation
        if self.cables.get() != 0:
          self.txtarea.insert(END, f"\n Cables\t\t{self.cables.get()}\t\t{self.p_c_p}")    

        if self.switches.get() != 0:
          self.txtarea.insert(END, f"\n Switches\t\t{self.switches.get()}\t\t{self.p_s_p}")  

        if self.routers.get() != 0:
          self.txtarea.insert(END, f"\n Routers\t\t{self.routers.get()}\t\t{self.p_r_p}") 

        if self.e_phones.get() != 0:
          self.txtarea.insert(END, f"\n Earphones\t\t{self.e_phones.get()}\t\t{self.p_e_p}")   

        if self.p_drives.get() != 0:
          self.txtarea.insert(END, f"\n Pendrive\t\t{self.p_drives.get()}\t\t{self.p_pd_p}")

        if self.r_kit.get() != 0:
          self.txtarea.insert(END, f"\n Repair Kit\t\t{self.r_kit.get()}\t\t{self.p_k_p}")   

        self.txtarea.insert(END, f"\n--------------------------------------")

        if self.com_parts_tax.get() != "Rs. 0.0":
            self.txtarea.insert(END, f"\n Computer Parts Tax\t\t\t   {self.com_parts_tax.get()}")

        if self.electronics_tax.get() != "Rs. 0.0":
            self.txtarea.insert(END, f"\n Electronics Tax\t\t\t   {self.electronics_tax.get()}")

        if self.peripherals_tax.get() != "Rs. 0.0":
            self.txtarea.insert(END, f"\n Periherals Tax\t\t\t   {self.peripherals_tax.get()}")

        self.txtarea.insert(END, f"\n\n--------------------------------------")

        # TOTAL BILL
        self.txtarea.insert(END, f"\n TOTAL BILL w/ Taxes : \t\t  Rs. {str(self.Total_bill)}")

        self.txtarea.insert(END, f"\n--------------------------------------")
        self.save_bill()


  def save_bill(self):

      s_bill = messagebox.askyesno("Save Bill ?", "Do you want to save the Bill ?")

      if s_bill > 0:
          self.bill_data = self.txtarea.get('1.0', END)
          f1 = open("Bills//" + str(self.bill_no.get()) + ".txt", "w")
          f1.write(self.bill_data)
          f1.close()
          messagebox.showinfo("Saved", f"Bill No. {self.bill_no.get()} saved.")

      else :
          return 

  
  def find_bill(self):

      present = "no"

      for i in os.listdir("Bills//"):
          if i.split('.')[0] == self.search_bill.get():
              f1 = open(f"Bills//{i}", "r")
              self.txtarea.delete('1.0', END)

              for d in f1:
                  self.txtarea.insert(END, d)
              f1.close()

              present = "yes"
          
      if present == "no":
          messagebox.showerror("Error", "No records found.")

  
  def clear_data(self):

      option = messagebox.askyesno("CLEAR", "Do you really want to clear ?")

      if option > 0:
          # VARIABLES : Computer Parts
          self.monitor.set(0)
          self.hdd_ssd.set(0)
          self.ram.set(0)
          self.l_charger.set(0)
          self.kboard_mouse.set(0)
          self.antivirus.set(0)


          # VARIABLES : Electronics
          self.tv.set(0)
          self.fridge.set(0)
          self.air_con.set(0)
          self.fans.set(0)
          self.t_light.set(0)
          self.bulbs.set(0)


          # VARIABLES : Peripherals
          self.cables.set(0)
          self.switches.set(0)
          self.routers.set(0)
          self.e_phones.set(0)
          self.p_drives.set(0)
          self.r_kit.set(0)


          # Total Product Price and Tax variables
          self.com_parts_price.set("")
          self.electronics_price.set("")
          self.peripherals_price.set("")

          self.com_parts_tax.set("")
          self.electronics_tax.set("")
          self.peripherals_tax.set("")


          # CUSTOMER INFORMATION
          self.c_name.set("")
          self.c_phone.set("")

          self.bill_no.set("")
          x = random.randint(1000, 9999)
          self.bill_no.set(str(x))
          self.search_bill.set("")

          self.welcome()


  def Exit_app(self):

    option = messagebox.askyesno("EXIT", "Do you really want to exit ?")

    if option > 0:
        self.root.destroy()
  


root = Tk()
obj = System_App(root)
root.mainloop() 