from nsepy.history import get_price_list
import datetime as dt
from nsepy import get_history
import os
import warnings
warnings.filterwarnings('ignore')          #This function will ignore all the warnings


Main=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #This will return the main path

Global=os.path.join(Main,"Global") # Here we are making a new directory and joining with Global [we are creatung a new directory]
OHLC=os.path.join(Global,'ohlc')  #inside the global directory we are creating another directory ohlc

if not os.path.exists(OHLC):  # this is a conditional statement whihch check if the path exist . If it doesn't new directory is made
                            # otherwise it's ignored because we will run this file daily and we don't want to create new directory.
    os.makedirs(OHLC)

df=get_price_list(dt=dt.date(2019, 1, 1)) # Here we are creating a new df and this get_price_list function to get pirce of all stocks on
stock_list=list(df['SYMBOL']) # and we extract the symbol

start_date=dt.date(2021,9,1) # we provide the start date
end_date=dt.date.today() #and the end date is today

def get_price_data(stocks):  # this function runs from the save_stock_Data and stock is the stock name as parameter
    # for stocks in stock_list:
        stock_data=get_history(symbol=stocks,start=start_date,end=end_date) #get history function accepsts stocks as a parameter
        mapping={
            'Symbol':'symbol',
            'Open':'open',
            'High':'high',
            'Low':'low',
            'Close':'close',
            'Deliverable Volume':'deliverable volume',
            '%Deliverble':'deliverable_percentage',
            'Volume':'volume'
        }
        stock_data=stock_data.rename(columns=mapping)
        stock_data=stock_data[mapping.values()]
        return stock_data #this returns a data frame of stock data

def save_stock_data(): #this function save the stock data
    for stocks in stock_list:  #loops through each stock list from the stock symbol which we extracted.
        file_name = os.path.join(OHLC, f'{stocks}.csv') # we are declaring a new variable file_name and saving it in OHLC data and each stock name
        df=get_price_data(stocks) # this function calls the get_price_data(stocks) and it runs from here
        if df.empty:  #this check if the data frame is empty. If it's empty it saves to csv aand the file name is one whcih we declares
            df.to_csv(file_name)

        else:
            df1=df.iloc[-1]  #this will extract last row of the dataframe if the datrframe is not empty
            df=df.append(df1) #and we append it to the datadframe
            df = df[~df.index.duplicated(keep='last')] #we check if there is duplicate and ~ returns which are not duplicate and extract only the true
            df.to_csv(file_name) #and save it file name
            print("processing",df.iloc[-1])










save_stock_data()

