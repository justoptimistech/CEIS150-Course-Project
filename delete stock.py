def delete_stock(self):
        symbol = self.stocklist.get(self.stocklist.curselection()) 
        i = 0
        for stock in self.stock_list:
            if stock.symbol == symbol:
                self.stock_list.pop(i)
            i = i+1
        self.display_stock_data()
        self.stocklist.delete(o,END)
        for stock in self.stock_list:
            self.stocklist.insert(END,stock.symbol)
        messagebox.showinfo("Stock deleted", symbol, "Removed")
