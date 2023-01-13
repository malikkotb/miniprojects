from pprint import pprint
import requests

base_url = "https://free.currconv.com"
api_key = "7a0e10f6eefbf7367302"

def exchange_rate(curr1, curr2):
    # rate
    response = requests.get(base_url + f"/api/v7/convert?q={your_curr}_{output_curr}&compact=ultra&apiKey={api_key}")
    response.raise_for_status()
    data = response.json()
    if len(data) == 0:
        print("Invalid currency.")
        return
    return data[f'{your_curr}_{output_curr}']

print('Welcome to the currency converter.')
print("List - Lists out all currencies.")
print("Convert - Convert one currency to another.")
print("Rate - View the exchange rates of two currencies.")

while True:
    command = input("Enter a command. q to quit. ").lower()

    if command == 'q':
        break
    else:
        if command == 'list':
            # list out all currencies
            response = requests.get(base_url + f"/api/v7/currencies?apiKey={api_key}")
            response.raise_for_status()
            data = response.json()['results']

            all_currencies = []
            for key in data:
                currencySymbol = ""
                if 'currencySymbol' in data[key]:
                    currencySymbol = data[key]['currencySymbol']
                all_currencies.append(f"{data[key]['id']} - {data[key]['currencyName']} - {currencySymbol}")

        elif command == 'convert':
            your_curr = input("Enter your currency: ")
            amount = float(input(f"Enter an amount in {your_curr}: "))
            output_curr = input(f"Enter the desired currency: ")

            rate = exchange_rate(your_curr, output_curr)
            converted_amount = rate * amount
            print(f"{amount} {your_curr} -> {output_curr} = {converted_amount}")

        elif command == 'rate':
            # view the exchange rates of two currencies
            your_curr = input("Enter your currency: ")
            output_curr = input(f"Enter the desired currency: ")

            rate = exchange_rate(your_curr, output_curr)
            print(f"Exchange Rate: {your_curr} -> {output_curr}: {rate}")
