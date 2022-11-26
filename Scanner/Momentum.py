from .Base import Base
from helper import register
import talib


class Momentum(Base):

    @register(name="RSI > 70", Trend="BEARISH")
    def rsi_gt_70(self):
        rsi = talib.RSI(self.df["close"], timeperiod=14).values
        return rsi[-1] > 70

    @register(name="RSI < 30", Trend="BULLISH")
    def rsi_lt_30(self):
        rsi = talib.RSI(self.df["close"], timeperiod=14).values
        return rsi[-1] < 30

    @register(name="52W High", Trend="BULLISH")
    def week52_high(self):
        last_year = self.df.iloc[-252:]
        max_high = last_year["high"].max()
        return self.df["high"].iloc[-1] == max_high

    @register(name="52W Low", Trend="BEARISH")
    def week52_low(self):
        last_year = self.df.iloc[-252:]
        min_low = last_year["low"].min()
        return self.df["low"].iloc[-1] == min_low

