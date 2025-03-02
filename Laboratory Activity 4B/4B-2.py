import csv

def load_rates(file):
    rates = {}
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rates[row['code']] = float(row['rate'])
    return rates

def convert(usd, curr, rates):
    return usd * rates[curr]

def main():
    file = 'Laboratory Activity 4B/currency.csv'
    rates = load_rates(file)
    
    usd = float(input("How much dollar do you have? "))
    curr = input("What currency you want to have? ").upper()
    
    result = convert(usd, curr, rates)
    
    print(f"Dollar: {usd} USD")
    print(f"{curr}: {result}")

if __name__ == "__main__":
    main()