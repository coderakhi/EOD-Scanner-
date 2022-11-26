from .Base import Base
from helper import register
import talib
import pandas as pd

class Crossover(Base):

    @register(name='crossover_50>200_SMA',Trend="Bullish")
    def crossover_50_200_SMA(self):
        sma50=talib.SMA(self.df['close'],timeperiod=50).values
        sma200 = talib.SMA(self.df['close'], timeperiod=200).values
        return sma50[-1]>sma200[-1] and sma50[-2]<sma200[-2]


    @register(name='crossover_9>21_SMA',Trend="Bullish")
    def crossover_9_21_SMA(self):
        sma9 = talib.SMA(self.df['close'], timeperiod=9).values
        sma21 = talib.SMA(self.df['close'], timeperiod=21).values
        return sma9[-1] > sma21[-1] and sma9[-2] < sma21[-2]

    @register(name='crossover_50>21_SMA',Trend="Bearish")
    def crossover_50_21(self):
        sma50 = talib.SMA(self.df['close'], timeperiod=50).values
        sma21 = talib.SMA(self.df['close'], timeperiod=21).values
        return sma50[-1] > sma21[-1] and sma50[-2] < sma21[-2]



df=pd.read_csv('3131.csv')
obj1=Crossover(df)
print(obj1.crossover_50_21())

