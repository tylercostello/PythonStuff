from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
spydata=si.get_data('spy' , start_date = '12/27/2014')
print(spydata)
