# Function to create stock chart
def display_stock_chart(stock_list, symbol):
    date =[]
    price =[]
    volume =[]
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date,price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()   
