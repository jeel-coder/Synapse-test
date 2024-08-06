request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transaction": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance": 5000.00,
        "transaction": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati": {
        "balance": 3500.00,
        "transaction": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00,
        "transaction": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}

array=[]
def array_creation(request_spending,account_id:str):
    for i in request_spending[account_id]['transaction']:
        return request_spending[account_id]['transaction']#[{'amount': -9000.0, 'category': 'Creatives'}, {'amount': 7000.0, 'category': 'Sponsor'}, {'amount': -2000.0, 'category': 'Prize-Money'}]

def total_spending(request_spending, account_id: str, category: str):
     for item  in array:
        if item['amount']<0.00 and item['category']==category:
             print(f"{account_id}  {category} {item['amount']}")

    
def account_balance(request_spending, account_id: str):
     balance=0
     balance+=request_spending[account_id]['balance']
     print(f'{account_id} has balance {balance}')
     return balance

def money_owed(request_spending, account_id: str) :
     return(total+add)
      
array += array_creation(request_spending,'Arham')
#print(array)

for j in array:
       total_spending(request_spending,'Arham',j['category'])
total=0            
for i in array:
    total+=i['amount']


add=account_balance(request_spending, 'Arham') 
money=money_owed(request_spending, 'Arham')
print(f'money owed {money}')
