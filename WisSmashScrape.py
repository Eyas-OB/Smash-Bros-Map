import requests
from bs4 import BeautifulSoup
import certifi

# Create a custom SSL certificate bundle using Certifi
session = requests.Session()
session.verify = certifi.where()

# Make the request using the custom certificate bundle
page_to_scrape = session.get("https://wismash.com/events-calendar/", verify=False)
soup = BeautifulSoup(page_to_scrape.content, "html.parser")

# Continue with your scraping
time = soup.find_all("div", class_="mec-time-details")
date = soup.find_all("span", class_="mec-start-date-label")
name = soup.find_all("h3", class_="mec-event-title")
place = soup.find_all("address", class_="mec-event-address")
link = soup.find("a", class_="mec-color-hover")
pic = soup.find_all("img", class_="attachment-thumblist size-thumblist wp-post-image")

# Extract the href attribute from the link if it exists
href = link.get("href") if link else "No link found"

# Extract the image source from the first image (assuming you want the first image)
image_src = pic[0]['src'] if pic else "No image found"

for event_time, event_date, event_name, event_place in zip(time, date, name, place):
    name_text = event_name.get_text().strip()
    time_text = event_time.get_text().strip()
    date_text = event_date.get_text().strip()
    place_text = event_place.get_text().strip()
    
    print(f"Date: {date_text} - Time: {time_text} - Name: {name_text} - Place: {place_text} - Link: {href}")
    print(f"Image Source: {image_src}")
