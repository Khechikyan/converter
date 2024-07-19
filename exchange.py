import requests as req
import tkinter as tk

def setDefaults(text):
    text.insert("end","AMD","USD","AED","AFN","ALL","ANG","AOA","ARS","AUD","AWG","AZN",
                "BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN",
                "BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUP","CVE",
                "CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK",
                "GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK",
                "HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD",
                "JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP",
                "LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU",
                "MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD",
                "OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB",
                "RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS","SRD",
                "SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD",
                "TWD","TZS","UAH","UGX","UYU","UZS","VES","VND","VUV","WST","XAF","XCD",
                "XDR","XOF","XPF","YER","ZAR","ZMW","ZWL" )
    
    
    valute1.insert(0, 'USD')
    valute2.insert(0, 'AMD')
    amount.insert(0, '1')
    presedCalc()

    
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

colors = {
    "entryColor" : _from_rgb((232, 112, 255)),
    "buttonColor": _from_rgb((177, 156, 217)),
    "rootColor" : _from_rgb((177, 156, 217)),
    "lightPurple": _from_rgb((198, 157, 219))
}


def presedCalc():
    try:
        calculate["state"] = "disabled"
        fro = valute1.get().upper()
        to = valute2.get().upper()
        count = float (amount.get())
        datas = req.get(f"https://v6.exchangerate-api.com/v6/776955c52b31c44fb34a4005/latest/{fro}").json()    
        course = datas["conversion_rates"][to]
        if count % 1 == 0 :
            count = int (count)
        if course % 1 == 0 :
            course = int (course)
        userViev["text"] = f"{count} {fro} = {course * count} {to}"
        calculate["state"] = "normal"

        
    except:
        print ("something went wrong")
        calculate["state"] = "normal"



def changeValutes():
     buff = valute1.get()
     valute1.delete(0, len(valute1.get()))
     valute1.insert(0, valute2.get())
     valute2.delete(0, len (valute2.get()))
     valute2.insert(0, buff)
     choose1["text"] = valute1.get().upper()
     choose2["text"] = valute2.get().upper()



# sb = tk.Scrollbar(mainWindow, command=text.yview)
# sb.pack(side="right")
# text.config(yscrollcommand = sb.set)

def openValutesList(choose1, choose2, valute1):

    global r
    try:

        if choose1.cget("text") != "chose":
            r = choose1.cget("text")
            print(r)
            text.place(x= 80, y= 8)
            choose1["text"] = "chose"
            choose2["state"] = tk.DISABLED
            change["state"] = tk.DISABLED
        else :
            x = text.curselection() 
            if len(x) == 0:
                valute1.delete(0, len (valute1.get()))
            
                valute1.insert(0, r)
                print (r)
                choose1["text"] = r
 
            elif len(x) != 0:
                    
                choose1["text"] = text.get(text.curselection())
                valute1.delete(0, len (valute1.get()))
            
                valute1.insert(0, text.get(text.curselection()))
            
            text.place_forget()
            choose2["state"] = tk.NORMAL
            change["state"] = tk.NORMAL

            
    except NameError:
        print("something went wrong")



mainWindow = tk.Tk()
mainWindow.title("change")
mainWindow.geometry("500x235+500+200")
mainWindow.configure(bg = colors["rootColor"])
mainWindow.resizable(False,False)

text = tk.Listbox (mainWindow, width= 10, height= 4, bg= "pink")


choose1 = tk.Button(mainWindow, width= 5,height= 1, bg= "lightgray", text= "USD", borderwidth=0,
                     command= lambda: openValutesList(choose1, choose2, valute1)
                     )

choose2 = tk.Button(mainWindow, width= 5,height= 1, bg= "lightgray", text= "AMD", borderwidth=0,
                     command= lambda: openValutesList(choose2, choose1, valute2))

userViev = tk.Label(mainWindow ,
                      height= 10, width= 71,
                      anchor= 'nw', font= 5, bg= "lightgray")

valute1 = tk.Entry(mainWindow , bg= colors["entryColor"],
                width = 6,font= 3) 

valute2 = tk.Entry(mainWindow , bg= colors["entryColor"],
                width = 6,font= 3) 

amount = tk.Entry(mainWindow, width= 15, font= 3,
                  bg= "lightgray", borderwidth=0)

change = tk.Button(mainWindow, bg= colors["rootColor"]
                   , width= 2, height= 2, text= "⭡⭣",
                     font= 20,  borderwidth=0, command= lambda: changeValutes())      

calculate = tk.Button(mainWindow, width= 12,bg= colors["lightPurple"],
                       height= 1, text= "convert", font= 3,
                       command= lambda: presedCalc(), borderwidth=0)

setDefaults(text)


  
amount.place(x= 350, y= 10)
userViev.place(x= 0, y= 80)
calculate.place(x= 350, y= 40)
valute1.place(x= 0, y= 10)
valute2.place(x= 0, y= 40)
change.place(x= 215, y= 0)
choose2.place(x= 146, y= 38)
choose1.place(x= 146, y= 8)

mainWindow.mainloop()

