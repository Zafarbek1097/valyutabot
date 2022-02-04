import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/6645acf0f9b6945564caeec3/latest/USD'  #uzbek so'miga nisbatan barcha davlatlarni valyuta kursi
#url = "https://v6.exchangerate-api.com/v6/6645acf0f9b6945564caeec3/pair/USD/UZS" #dollr kursi

# Making our request
response = requests.get(url)
data = response.json()

print(data)

# Your JSON object

#print(response.status_code)   #tekshirish

	