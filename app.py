# App Name : buyLowSellHigh.py 
# Author   : Guang Mo 
# 
#
#

import sys
import datetime
from common import readStockList

# Read file as input
buyStockList = [] #List of potential buy stocks 
sellStockList = [] #List of potential sell stocks
CONST_BUY = 1 
CONST_SELL = 0 
NUM_COLUMN = 2  # number of columns of the input file

stockListFile = str(sys.argv[1])

buyStockList = readStockList(stockListFile, CONST_BUY, NUM_COLUMN)
sellStockList = readStockList(stockListFile, CONST_SELL, NUM_COLUMN)

print(buyStockList)
print("next")
print(sellStockList)


