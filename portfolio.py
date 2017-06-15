from ryan_tools import * 
import pickle
from git import Repo

    


current_val = 0
def get_current_value():
    global current_val
    return current_val

def change_current_value(change, dollar_amount_update = False):
    global current_val
    current_val = current_val + change
    if dollar_amount_update:
        update_dollars()
def update_dollars():
    'updates dollar values based on percentages Current Val is King'
    current = get_current_value()
    portfolio['last value'] = portfolio['percentage'] * current


def update_percentages(name):
    'updates percentage values based on dollar amount, used during deposit or withdrawal ONLY'
    current = get_current_value()
    for index in portfolio.index:
        usd = portfolio.loc[index, 'last value']
        portfolio.loc[index, 'percentage'] = usd/current
    

def add_account(iden):
    if iden in portfolio.index:
        raise Exception(' ID already taken. Choose new id' )
    portfolio.loc[iden, 'percentage'] = 0
    portfolio.loc[iden, 'last value'] = 0


def deposit(name, usd):
    global portfolio   

    if name not in portfolio.index:
        raise Exception('Please Add ', name , ' to accounts with add_account() first ' )
    
    update_dollars()
    change_current_value(usd)
    portfolio.loc[name, 'last value'] = portfolio.loc[name, 'last value'] + usd
    update_percentages(name)
    update_dollars()
  

        
    
    
def withdraw(name, usd):
    usd = -1 * abs(usd)
    update_dollars()
    available = portfolio.loc[name, 'last value']
    if abs(usd) > available:
        raise Exception(' Account value is ', available )
    deposit(name, usd )
    


def __init__():
    global portfolio
    global current_val
    portfolio = pd.DataFrame(columns = ['percentage', 'last value'])
    current_val = 0

    

def save():
    global portfolio
    global current_val
    with open('current_val.float', 'wb') as file_stream:
        pickle.dump(current_val, file_stream)
    with open('portfolio.df', 'wb') as file_stream:
        pickle.dump(portfolio,file_stream)
        

def load():
    global portfolio
    global current_val
    
    with open('current_val.float', 'rb') as file_stream:
        current_val = pickle.load(file_stream)
    with open('portfolio.df', 'rb') as file_stream:
        portfolio =  pickle.load(file_stream)
        
load()
