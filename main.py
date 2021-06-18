import requests
from bs4 import BeautifulSoup



page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.33806999999996#.XIR')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
print(period_names)