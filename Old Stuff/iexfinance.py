exec("""
from iexfinance import Stock
baba = Stock('BABA')
print(baba.get_price())
""")