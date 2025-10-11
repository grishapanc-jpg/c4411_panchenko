import requests
import sqlite3
import datetime

res = requests.get("https://wttr.in/Chernihiv?format=%t")
temp = res.text.strip()
print("Температура у Чернігові:", temp)

conn = sqlite3.connect("weather.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS weather (date_time TEXT, temperature TEXT)")

time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
c.execute("INSERT INTO weather VALUES (?, ?)", (time_now, temp))

conn.commit()
conn.close()

print("Дані збережено у базі!")
