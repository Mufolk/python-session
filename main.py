from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xuae0WpKiRs")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
# print(seven_day)
forecast_items = seven_day.find_all(class_="tombstone-container")
# print(forecast_items)
tonight = forecast_items[0]
# print(tonight)

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# print(period)
# print(short_desc)
# print(temp)

img = tonight.find("img")
desc = img['title']
# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)
# print(temps)
# print(descs)

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
