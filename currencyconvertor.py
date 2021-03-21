import requests

response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
# print(response.json())

def get_input():
  country = input("FULL NAME of country that you'd like to convert amount to: ")

  flag = True
  while (flag):
    amount = input("Money in USD: ")
    if (amount.isdigit() == False):
      print("Invalid Input. Enter an integer!")
      # pass
    else:
      flag = False
  
  amount = int(amount)
  country = country.upper()
  return amount, country

def find_currency_code(country):
  country_code_api = "https://pkgstore.datahub.io/core/currency-codes/codes-all_json/data/029be9faf6547aba93d64384f7444774/codes-all_json.json"
  country_code = requests.get(country_code_api)
  country_code = country_code.json()

  for i in country_code:
    if (i["Entity"] == country):
      code = i["AlphabeticCode"]
      return code

def find_currency_rate(currency_code):
  currency_rate_api = "https://api.exchangeratesapi.io/latest?base=USD"
  currency_rate = requests.get(currency_rate_api)
  currency_rate = currency_rate.json()
  rates = currency_rate["rates"]
  rates_keys = rates.keys()
  # print(currency_rate["rates"])

  for i in rates_keys:
    if (i == currency_code):
      rate = rates[i]
      return rate
    else:
      return False

def calculate(amount, conversion_rate):
  ans = conversion_rate * amount
  print(ans) 

def main():
  amount, country = get_input()
  x = find_currency_code(country)
  y = find_currency_rate(x)
  calculate(amount, y)

main()
