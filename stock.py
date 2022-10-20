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
    market_price = ticker['regularMarketPrice']
    current_time = datetime.datetime.now()
    print('Market Price of GOOGLE: ',market_price,"at ",current_time.hour,":",current_time.minute,":",current_time.second)
    time.sleep(5)




class Application(Frame):
    def __init__(self, master):
        """ Initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Create 3 useless buttons"""
        #first one
        self.bttn1=Button(self, text ="I do nothing!")
        self.bttn1.grid()
        #second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text ="Me too!")
        #third one
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"]="And me also!"

root=Tk()
#alter window
root.title("The simpliest gui")
root.geometry("200x100")
app=Application(root)
root.mainloop()



