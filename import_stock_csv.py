def import_stock_csv(stock_list):
    print("\nAdd historial date to a stock in the stock")
    print("Stock List: [ ", end=" ")
    for stock in stock_list:
        print(stock.symbol, " ",end=" ")
    print("]")
    symbol = input("Enter stock symbol: ").upper()
    filename = input("Enter the file name: ")
    for stock in stock_list:
        if stock.symbol == symbol:
            with open(filename, newline=" ") as stockdata:
                datareader =  csv.reader(stockdata, delimiter = ",")
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]), float(row[4]),float(row[6]))
                    stock.add_data(daily_data)
    display_report(stock_list)
