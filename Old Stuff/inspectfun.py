from inspect import getmembers, isfunction
from yahoo_fin import stock_info

functions_list = [o for o in getmembers(stock_info) if isfunction(o[1])]
