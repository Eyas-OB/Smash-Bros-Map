import requests
from bs4 import BeautifulSoup
import certifi
import csv

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
pic = soup.find_all("img", class_="attachment-thumblist size-thumblist wp-post-image")

# Create a list to store the scraped data
scraped_data = []

for event_time, event_date, event_name, event_place, event_pic in zip(time, date, name, place, pic):
    name_text = event_name.get_text().strip()
    time_text = event_time.get_text().strip()
    date_text = event_date.get_text().strip()
    place_text = event_place.get_text().strip()
    
    # Extract the href attribute from the link if it exists
    link = event_name.find("a")
    href = link.get("href") if link else "No link found"

    # Extract the image source URL
    image_src = event_pic['src'] if 'src' in event_pic.attrs else "No image found"
    
    event_data = [date_text, time_text, name_text, place_text, href, image_src]
    scraped_data.append(event_data)

# Save the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(["Date", "Time", "Name", "Place", "Link", "Image"])
    
    # Write the data from the scraped_data list
    csvwriter.writerows(scraped_data)

print("Data saved to scraped_data.csv")

