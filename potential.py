from ryan_tools import * 







import pickle






class account():
    name = None
    email = None
    phone = None
    

    changes = None
    
    def add(self, usd, method):
        length = len(self.changes)
        self.changes.loc[length, 'date'] = datetime.datetime.now()
        self.changes.loc[length, 'amount'] = float(usd)
        self.changes.loc[length, 'date'] = method

    def __init__(self):
        self.name = input('Human Name?')
        self.email = input('Email?')
        self.phone = input('Phone?')
        self.changes = pd.DataFrame(columns = ['date','amount', 'method' ] )
    def __str__(self):
        temp = self.changes.copy()
        temp.loc['TOTAL', 'amount'] = self.changes['amount'].sum()
        return str(temp)
        
