import requests

# response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
# print(response.json())

def get_country():
  flag = True
  while (flag):
    country = input("FULL NAME of country that you'd like to convert amount to: ")
    country = country.upper()
    x = find_currency_code(country)
    if (x == False):
      print("Sorry, we can't find the country")
    elif (find_currency_rate(x) == False):
      print("Sorry, this program doesn't support the currency code for the country")
    else:
      flag = False
  # check1 = check_country(country)
  # if (check1 == False):
  #   quit()
  # country = country.upper()
      return country

def get_amount():
  flag = True
  while (flag):
    amount = input("Money in USD: ")
    if (amount.isdigit() == False):
      print("Invalid Input. Enter an integer!")
      # pass
    else:
      flag = False
  amount = int(amount)
  return amount

# def check_country(country):
#   country = country.upper()
#   x = find_currency_code(country)
#   if (x == False):
#     print("Sorry, we can't find the country")
#     return x
#   else:
#     y = find_currency_rate(x)
#     if (y == False):
#       print("Sorry, this program doesn't support the currency code for the country")
#       return y

def find_currency_code(country):
  country_code_api = "https://pkgstore.datahub.io/core/currency-codes/codes-all_json/data/029be9faf6547aba93d64384f7444774/codes-all_json.json"
  country_code = requests.get(country_code_api)
  country_code = country_code.json()

  for i in country_code:
    if (i["Entity"] == country):
      code = i["AlphabeticCode"]
      return code
  return False

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
  return False

def calculate(amount, conversion_rate, currency_code):
  ans = conversion_rate * amount
  # put the currency code (ex: USD)
  print(ans, currency_code) 

def main():
  country = get_country()
  amount = get_amount()
  x = find_currency_code(country)
  y = find_currency_rate(x)
  calculate(amount, y, x)

main()
