def fetch_available_balance(exchange):
    balances = exchange.fetch_balance()
    
    for balance in balances:
        if isinstance(balances[balance], dict) and 'total' in balances[balance] and balances[balance]['total'] > 0:
            print(balance, balances[balance])
    