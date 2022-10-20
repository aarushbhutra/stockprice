import yfinance as yf
import time
from tkinter import *
import datetime

forever = True

ticker = yf.Ticker('GOOGL').info

previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Previous Close Price:', previous_close_price)

while forever:
    ticker = yf.Ticker('GOOGL').info
    market_price = ticker['regularMarketPrice']
    current_time = datetime.datetime.now()
    print('Market Price of GOOGLE: ',market_price,"at ",current_time.hour,":",current_time.minute,":",current_time.second)
    time.sleep(5)


root = Tk()
root.title("Google Stock Price")
# Set geometry (widthxheight)
root.geometry('350x200')

output = 'Market Price of GOOGLE: ',market_price,"at ",current_time.hour,":",current_time.minute,":",current_time.second

lbl = Label(root, text = output)
lbl.grid()

root.mainloop()
