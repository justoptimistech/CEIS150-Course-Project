# Display Chart
def display_chart(stock_list):
    print("Stock Chart - - - ")
    print("Stock List: [ ", end=" ")
    for stock in stock_list:
        print(stock.symbol, " ",end=" ")
    print("]")
    symbol = input("Pick a stock for a chart: ").upper()
    found = False

    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, current_stock.symbol)
    else: 
        print("Symbol not found")
        _= input("press enter to continue")
