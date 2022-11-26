catalog={}

# {Crossover:[{MA20:True,trend:bullish},MA9:False,MA30:True]

def register(**kwargs):
    def wrap(func):
        full_name=func.__qualname__
        class_name = full_name.split(".")[0]
        function_list=catalog.setdefault(class_name,[])
        temp={}
        temp['strategy_name']=kwargs['name']
        temp['Trend']=kwargs['Trend']
        temp['functions_name']=func.__name__
        function_list.append(temp)
        catalog[class_name]=function_list
        # print(catalog)
        return func
    return wrap



