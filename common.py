###############################################################################
#
#         Name: common.py 
#       Author: Guang Mo 
#         Date: May 1st, 2018 
#  Description: This file stores the common functions that I use over time. 
# 
###############################################################################

###############################################################################
#    Function: readStockList()
# Description: This function reads an input file that stores stock symbols and 
#              buy/sell action, and it returns a list that contains all stocks 
#              in buy or sell action.  
#      Inputs: fileName - stocklist.txt
#              action - 1 for buy, 0 for sell
#              numOfColumn - how many number of columns in the input file
#      Output: A stock list 
#  Assumption: The columns are separated by space
#              The first column is stock symbol
#              The second column is action 
###############################################################################
def readStockList(fileName, action, numOfColumn):
    stockList = [] 
    lineNum = 0
    for line in open( fileName,'r'):
        lineNum = lineNum + 1 
        # Need to validate the formate of the line is correct 
        assert len(line.split()) == numOfColumn, "input file line # %r does not have the right number of columns" % lineNum
        if int(line.split()[1]) == action:
            stockList.append(line.split()[0])
    return stockList 