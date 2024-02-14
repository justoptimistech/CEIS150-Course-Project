def display_report(stock_list):
    print("Stock Report ----")
    for stock in stock_list:
        print("Report for: ", stock.symbol, stock.name)
        print("Shares: ", stock.shares)
        #variable initialization
        count = 0
        price_total = 0 
        volume_total = 0
        lowPrice = 99999999.99
        highPrice = 0.0
        lowVolume = 9999999999
        highVolume = 0
        
        for daily_data in stock.Datalist:
            count = count + 1
            price_total = price_total + daily_data.close
            volume_total = volume_total + daily_data.volume
            if daily_data.close < lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
                highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
               highVolume = daily_data.volume
               
            priceChange = highPrice - lowPrice
            print(daily_data.date, daily_data.close,daily_data.volume)
        if count > 0:
            print("Summary ----")
            print("Low Price: ${:,.2f}".format(lowPrice))
            print("High Price: ${:,.2f}".format(highPrice))
            print("Average Price: ${:,.2f}".format(price_total/count))
            print("Low Volume: ", lowVolume)
            print("High Volume: ", highVolume)
            print("Average Volume: {:,.2f}".format(volume_total/count))
            print("Change in Price: ${:,.2f}".format(priceChange))
            print("Profit/Loss: ${:,.2f}".format(priceChange * stock.shares))
        else:
            print("**** No daily history")
        print("\n\n\n")
    print(" - - - Report complete - - -")     
    _=input("Press Enter to continue")
            
