# App Name : buyLowSellHigh.py 
# Author   : Guang Mo 
# 
#
#

import sys
import datetime

# Read file as input
buyStockList = []; #List of potential buy stocks 
sellStockList = []; #List of potential sell stocks
CONST_BUY = 1; 
CONST_SELL = 0; 

#
# Function: readStockList() 
# Inputs: stockList.txt
#         Action
# Output: A stock list
def readStockList():
    stockList = [] 
    for line in open( str(sys.argv[1]),'r'): 
        print(line.split()[1])
        if int(line.split()[1]) == CONST_BUY:
            print("guang mo") 
            stockList.append(line.split()[0])
    return stockList 

buyStockList = readStockList()
print(buyStockList)



