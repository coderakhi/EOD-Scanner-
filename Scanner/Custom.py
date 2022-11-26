from .Base import Base
from helper import register
import talib



class Custom(Base):

    @register(name="Higher Highs 3", Trend="BULLISH")
    def higher_highs_3(self):
        highs = self.df["high"].values
        return highs[-3] < highs[-2] < highs[-1]

    @register(name="Lower Lows 3", Trend="BEARISH")
    def lower_lows_3(self):
        lows = self.df["low"].values
        return lows[-3] > lows[-2] > lows[-1]

    @register(name="Higher Close 3", Trend="BULLISH")
    def higher_close_3(self):
        close = self.df["close"].values
        return close[-3] < close[-2] < close[-1]

    @register(name="Lower Close 3", Trend="BEARISH")
    def lower_close_3(self):
        close = self.df["close"].values
        return close[-3] > close[-2] > close[-1]

