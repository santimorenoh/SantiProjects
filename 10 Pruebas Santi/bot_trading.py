from binance.client import Client

# Tus claves de API
api_key = '7EKws1SgjPQhMY8JQX95mBaLmmJtd5psLwgsVw9CBGwbiX8hcpHNgVtMkzkGkzAB'
api_secret = '4GqPKGZZJb0tHGjK6m51EROFpvV0wIQBCpyrNu80fepijUi6yCVlRnjkR0zKd7dG'

client = Client(api_key, api_secret)

# Obtener el precio actual de BTC/USDT
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"El precio actual de BTC es: {btc_price['price']}")