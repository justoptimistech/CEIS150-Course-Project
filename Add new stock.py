def add_stock(self):
        new_stock = Stock(self.addSymbolEntry.get(), self.addNameEntry.get(), float(self.addSharesEntry.get())) 
        self.stock_list.append(new_stock)
        self.stocklist.insert(END,self.addSymbolEntry.get())
        self.addSymbolEntry.delete(0,END)
        self.addNameEntry.delete(0,END)
        self.addSharesEntry.delete(0,END)
