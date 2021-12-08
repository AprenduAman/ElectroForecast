import tkinter
from tkinter import *
from tkinter import messagebox

def nextIspressed():
    labeltext.destroy()
    labeltext1.destroy()
    labeltext2.destroy()
    labeltext3.destroy()
    labeltext4.destroy()
    labeltext5.destroy()
    labeltext6.destroy()
    labeltex2.destroy()
    labeltex3.destroy()
    labeltex4.destroy()
    labeltex6.destroy()
    labelimage2.destroy()
    labelimage3.destroy()
    labelimage4.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    e7.destroy()
    e8.destroy()
    btnnext.destroy()
    product2()
   
def product():
  global labeltext,labelimage3,labelimage2,img3,img4,img5,labelimage4,img6,labeltext1,labeltext2,labeltext3,labeltext4,labeltext5,btnnext,labeltex2,labeltex3,labeltex4,labeltext6,labeltex6,e1,e2,e3,e4,e5,e6,e7,e8,num1,num2,num3,num4,num5,num6,num7,num8
  labeltext = Label(
    root,
    text = "PRODUCTS",
    font = ("Colonna MT",40,"bold","underline"),
    foreground = "#ffffff",
    background = "#E84E36",

)
  labeltext.place(x=250,y=30)
  img3 = PhotoImage(file="logo2.png")

  labelimage2 = Label(
    root,
    image=img3,
    background = "#E84E36",
    border = 0,
    
) 
  labelimage2.place(x=10,y=10)
  img4 = PhotoImage(file="p1.png")

  labelimage3= Label(
    root,
    image=img4,
    background = "#E84E36",
    
) 
  labelimage3.place(x=40,y=185)
  labeltext1 = Label(
    root,
    text = "ACER LAPTOP",
    font = ("Bernard MT",28,"bold","underline"),
    foreground = "#ffffff",
    background = "#E84E36",
   
   
)
  labeltext1.place(x=275,y=100)
  labeltext2 = Label(
    root,
    text = "Buying price(in Rs.)=",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltext2.place(x=230,y=170)
  num1= IntVar()
  
  e1=Entry(
      root,
      textvariable = num1,
      font= ("Bell MT",16,"bold"),
      width=10
      )
  e1.place(x=450,y=170)
  labeltext3 = Label(
    root,
    text = "Selling price(in Rs.)=",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltext3.place(x=230,y=210)
  num2= IntVar()
  e2=Entry(
      root,
      textvariable = num2,
      font= ("Bell MT",16,"bold"),
      width=10
      )
  e2.place(x=450,y=210)
  labeltext4 = Label(
    root,
    text = "Preseason-sales =",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltext4.place(x=230,y=250)
  num3= IntVar()
  e3=Entry(
      root,
      textvariable = num3,
      font= ("Bell MT",16,"bold"),
      width=10
     )
  e3.place(x=450,y=250)
  labeltext6 = Label(
    root,
    text = "Discount(in % ) =",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltext6.place(x=230,y=290)
  num4= IntVar()
  e4=Entry(
      root,
      textvariable = num4,
      font= ("Bell MT",16,"bold"),
      width=10
      )
  e4.place(x=450,y=290)
  img5 = PhotoImage(file="p2.png")

  labelimage4= Label(
    root,
    image=img5,
    background = "#E84E36",
    
) 
  labelimage4.place(x=40,y=405)
 
  labeltext5= Label(
    root,
    text = "BOAT HEADPHONE",
    font = ("Bernard MT",28,"bold","underline"),
    foreground = "#ffffff",
    background = "#E84E36",
   
   
)
  labeltext5.place(x=260,y=340)
  labeltex2 = Label(
    root,
    text = "Buying price(in Rs.)=",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltex2.place(x=230,y=400)
  num5= IntVar()
  e5=Entry(
      root,
      textvariable = num5,
      font= ("Bell MT",16,"bold"),
      width=10,
      )
  e5.place(x=450,y=400)
  labeltex3 = Label(
    root,
    text = "Selling price(in Rs.)=",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltex3.place(x=230,y=440)
  num6= IntVar()
  e6=Entry(
      root,
      textvariable = num6,
      font= ("Bell MT",16,"bold"),
      width=10,
      )
  e6.place(x=450,y=440)
  labeltex4 = Label(
    root,
    text = "Preseason-sales =",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltex4.place(x=230,y=480)
  num7= IntVar()
  e7=Entry(
      root,
      textvariable = num7,
      font= ("Bell MT",16,"bold"),
      width=10,
      )
  e7.place(x=450,y=480)
  labeltex6 = Label(
    root,
    text = "Discount(in % ) =",
    font = ("Bell MT",16,"bold"),
    foreground = "#ffffff",
    background = "#E84E36",
  )
  labeltex6.place(x=230,y=520)
  num8= IntVar()
  e8=Entry(
      root,
      textvariable = num8,
      font= ("Bell MT",16,"bold"),
      width=10,
      )
  e8.place(x=450,y=520)
  img6 = PhotoImage(file="next.png")

  btnnext = Button(
    root,
    image = img6,
     background = "#E84E36",
    border = 0,
    command = nextIspressed,
)
  btnnext.place(x=610,y=540)

def calcIspressed():
    labeltet.destroy()
    labeltex1.destroy()
    labeltext7.destroy()
    labeltext8.destroy()
    labeltext9.destroy()
    labeltext10.destroy()
    labelimag2.destroy()
    labelimag3.destroy()
    p1.destroy()
    p2.destroy()
    p3.destroy()
    p4.destroy()
    btnano.destroy()
    btncalc.destroy()
    result()
    

def anoIspressed():
    messagebox.showinfo("update","This feature is under updation and  will be availabe in few days ")

def product2():
    global labeltet,im3,labelimag2,labelimag3,im4,labeltex1,labeltext7,labeltext8,labeltext9,labeltext10,img7,img8,btnano,btncalc,p1,p2,p3,p4,pum1,pum2,pum3,pum4
    labeltet = Label(
        root,
        text = "PRODUCTS",
        font = ("Colonna MT",40,"bold","underline"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
    labeltet.place(x=250,y=30)
    im3 = PhotoImage(file="logo2.png")
    labelimag2 = Label(
        root,
        image=im3,
        background = "#E84E36",
        border = 0,
        )
    labelimag2.place(x=10,y=10)
    im4 = PhotoImage(file="p3.png")
    labelimag3= Label(
        root,
        image=im4,
        background = "#E84E36",
        )
    labelimag3.place(x=40,y=195)
    labeltex1 = Label(
        root,
        text = "BOAT AIRPODS",
        font = ("Bernard MT",28,"bold","underline"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
    labeltex1.place(x=275,y=150)
    labeltext7 = Label(
        root,
        text = "Buying price(in Rs.)=",
        font = ("Bell MT",16,"bold"),
        foreground = "#ffffff",
        background = "#E84E36",
)
    labeltext7.place(x=230,y=210)
    pum1= IntVar()
    p1=Entry(
        root,
        textvariable = pum1,
        font= ("Bell MT",16,"bold"),
        width=10,
        )
    p1.place(x=450,y=210)
    

    labeltext8 = Label(
        root,
        text = "Selling price(in Rs.)=",
        font = ("Bell MT",16,"bold"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
    labeltext8.place(x=230,y=250)
    pum2= IntVar()
    p2=Entry(
    
        root,
        textvariable = pum2,
        font= ("Bell MT",16,"bold"),
        width=10,
        )
    p2.place(x=450,y=250)
    
    labeltext9 = Label(
        root,
        text = "Preseason-sales =",
        font = ("Bell MT",16,"bold"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
    labeltext9.place(x=230,y=290)
    pum3= IntVar()
    p3=Entry(
        root,
        textvariable = pum3,
        font= ("Bell MT",16,"bold"),
        width=10,
        )
    p3.place(x=450,y=290)
    
    
    labeltext10 = Label(
        root,
        text = "Discount(in % ) =",
        font = ("Bell MT",16,"bold"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
    labeltext10.place(x=230,y=330)
    pum4= IntVar()
    p4=Entry(
        root,
        textvariable = pum4,
        font= ("Bell MT",16,"bold"),
        width=10,
        )
    p4.place(x=450,y=330)
    
    
    img7 = PhotoImage(file="calc.png")
    btncalc = Button(
        root,
        image = img7,
        background = "#E84E36",
        border =0,
        command = calcIspressed,
        )
    btncalc.place(x=100,y=450)
    img8 = PhotoImage(file="ano.png")
    btnano = Button(
        root,
        image = img8,
        background = "#E84E36",
        border =0,
        command = anoIspressed,
        )
    btnano.place(x=350,y=460)

def result():
      global labelte,i3,labelima2,lblresult,num1,num2,num3,num4,num5,num6,num7,num8,pum1,pum2,pum3,pum4
      labelte = Label(
        root,
        text = "RESULTS",
        font = ("Colonna MT",50,"bold","underline"),
        foreground = "#ffffff",
        background = "#E84E36",
        )
      labelte.place(x=250,y=30)
      i3 = PhotoImage(file="logo2.png")
      labelima2 = Label(
    
        root,
        image=i3,
        background = "#E84E36",
        border = 0,
        )
      labelima2.place(x=20,y=20)
     
      r1= num3.get()*(num4.get()/2)+num3.get()
      r2=(num2.get()-(num4.get()/100*num2.get()))-num1.get()
      r3= num7.get()*(num8.get()/2)+num7.get()
      r4=(num6.get()-(num8.get()/100*num6.get()))-num5.get()
      r5= pum3.get()*(pum4.get()/2)+pum3.get()
      r6=(pum2.get()-(pum4.get()/100*pum2.get()))-pum1.get()
      
    
      lblresult = Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult.pack(pady=(150,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult.config(text= "Sales Forecast of ACER LAPTOP = "+str(r1))
      lblresult1= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult1.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult1.config(text= "Profit from ACER LAPTOP = "+str(r2))
      lblresult2= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult2.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult2.config(text= "Sales Forecast of BOAT HEADPHONE = "+str(r3))
      lblresult3= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult3.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult3.config(text= "Profit from BOAT HEADPHONE = "+str(r4))
      lblresult4= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult4.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult4.config(text= "Sales Forecast of BOAT AIRPODS = "+str(r5))
      lblresult5= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult5.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult5.config(text= "Profit from BOAT AIRPODS = "+str(r6))
      lblresult6= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult6.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult6.config(text= "Total Sales Forecast = "+str(r1+r3+r5))
      lblresult7= Label(
        root,
        text= "", font = ("Book Antiqua bold", 16), width = 570,relief= "sunken",justify ="left",background = "#ffffff",fg ="#E84E36",bd =1,
   )
      lblresult7.pack(pady=(0,5), padx=(35,35), ipadx=10, ipady=10)
      lblresult7.config(text= "Total Profit = "+str(r2+r4+r6))
   
def startIspressed():
    labelimage.destroy()
    lblRules.destroy()
    btnStart.destroy()
    product()
    
root = tkinter.Tk()
root.title("Electro Forecast")
root.geometry("700x600")
root.config(background="#E84E36")
root.resizable(0,0)

img1 = PhotoImage(file="logo.png")

labelimage = Label(
    root,
    image = img1,
    background = "#E84E36",
)
labelimage.pack(pady=(40,45))
img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image = img2,
     background = "#E84E36",
    border = 1,
    command = startIspressed,
)
btnStart.pack(pady=(20,85))
lblRules = Label(
    root,
    text = "This analysis and forecast the sales of \n electronic product based on discount \n and pre sales record. ",
    width = 100,
    justify = "center",
    font = ("Times",18),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()




root.mainloop()
