#import modules
from tkinter import *
import requests
import json
from bs4 import BeautifulSoup

#scraping currency code and exchange rate from "https://www.iban.com/exchange-rates"
currency_codes_url = "https://www.iban.com/exchange-rates";
currency_codes_url_res = BeautifulSoup(requests.get(currency_codes_url).content , 'html.parser')
currencyNameToSymbolHtml = currency_codes_url_res.tbody.find_all('tr')

#declaring dicts
currencyNameToSymbol = {}
currencySymbolWithEuroExchangeRate = {}

#getting country name,symbol,and rate in euro and mapping them to the dicts
for currencyInf in currencyNameToSymbolHtml:
    currencyInfList = list(currencyInf.find_all('td'))
    currencyName   = str(currencyInfList[1].string);
    currencySymbol = currencyInfList[0].img.next_sibling.strip();
    currencyInEuro = float(currencyInfList[2].string)

    currencyNameToSymbol[currencyName] = currencySymbol
    currencySymbolWithEuroExchangeRate[currencyName] = currencyInEuro




#configuring tkinter
top = Tk()
top.geometry("450x250")
top.configure(bg='#222831')

#making the dropdown menus for choosing currencies
BASE_OPTIONS = list(currencyNameToSymbol.keys())
TO_OPTIONS = list(currencyNameToSymbol.keys())

base = StringVar(top)
base.set(BASE_OPTIONS[0]) # default value

to = StringVar(top)
to.set(TO_OPTIONS[0]) # default value

baseOptionsMenu = OptionMenu(top, base, *BASE_OPTIONS)
toOptionsMenu = OptionMenu(top, to, *TO_OPTIONS)
resultLabel = Label(top,bg='#222831' , foreground='#fff')

#making a number only entry
def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

vcmd = (top.register(callback))
amountInput = Entry(top ,validate='all', validatecommand=(vcmd, '%P'))


baseOptionsMenu.configure(width=15 , height=2,bg='#1f6f8b')
toOptionsMenu.configure(width=15 , height=2,bg='#1f6f8b')

#placing the widgets in the screen using grid
baseOptionsMenu.grid(row=1 , column=3 , pady=(250//2 - 70 , 5) , padx=(10 ,10))
toOptionsMenu.grid(row=1 , column=5 , pady=(250//2 - 70 , 5) , padx=(10 ,10))
amountInput.grid(row=1 , column=4 , pady=(250//2 - 70 , 5))
resultLabel.grid(row=2 , column=4)

#function to calculate result
def returnResult():

    baseInEuro = currencySymbolWithEuroExchangeRate[base.get()]
    toInEuro = currencySymbolWithEuroExchangeRate[to.get()]

    result = (float(toInEuro) / float(baseInEuro))* int(amountInput.get())
    resultLabel['text'] = f'{currencyNameToSymbol[to.get()]} {result}'

button = Button(top, text="Convert", command=returnResult , width=7 , height=1,bg="#ff4d4d")
button.grid(row=3 , column=4,padx=(0 ,10) , pady=(10))

#mainloop
mainloop()
