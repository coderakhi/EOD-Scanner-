from Scanner import Momentum
from Scanner import Crossover
from Scanner import Custom
from nsepy import get_history
from nsepy.history import get_price_list
import datetime as dt
import pandas as pd
import glob
import os
import talib
from  helper import register
from helper import catalog
import warnings
warnings.filterwarnings('ignore')

df=get_price_list(dt=dt.date(2019, 1, 1))
stock_lists=list(df['SYMBOL'])


ScanList=[Crossover,Momentum,Custom]

csv_files = glob.glob("Global/ohlc/*.csv")
result=[]
for scanners in ScanList:

    function_list=[function for function in dir(scanners) if function.startswith('__') is False]

    # for functions in function_list:

    # have to loop through the functions inside each class

    for f in csv_files:
            stock=f.split("\\")[1].split(".")[0]
            df=pd.read_csv(f)
            if df.empty:
                continue
            else:
                for functions in function_list:
                    obj1=scanners(df)
                    temp={"stocks":stock,functions:getattr(obj1,functions)()}
                    result.append(temp)


df=pd.DataFrame(result)

df_result=pd.DataFrame()
for group_index, sliced_df in df.groupby("stocks"):
        dfs=sliced_df.max().to_frame().T
        df_result=df_result.append(dfs)

print(df_result)
print(df_result.columns)


















