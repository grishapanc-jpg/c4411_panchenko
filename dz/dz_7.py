import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
data = response.json()

usd_rate = None
for currency in data:
    if currency["cc"] == "USD":
        usd_rate = currency["rate"]
        break

if usd_rate is None:
    print("Не вдалося знайти курс долара.")
else:
    print(f"Курс долара США: {usd_rate} грн")

    amount = float(input("Введіть кількість гривень: "))
    usd = amount / usd_rate
    print(f"{amount} грн = {usd:.2f} $")
