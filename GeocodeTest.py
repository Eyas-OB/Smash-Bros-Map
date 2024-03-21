from geopy.geocoders import Nominatim
import csv
import time

# Create a Geocoder object
geolocator = Nominatim(user_agent="GetLoc")

# List of addresses
addresses = [
    "Main St. Sun Prairie, WI 53590",
    "975 University Ave, Madison, WI 53706",
    "100 W Capitol Dr Appleton WI 54911",
    "6640 Odana Rd. Madison, WI 53719",
    "3807 S Packard Ave. St. Francis, WI",
    "3807 S Packard Ave. St. Francis, WI",
    "100 W Capitol Dr Appleton WI 54911",
    "6640 Odana Rd. Madison, Wi 53719",
    "Concordia University, Mequon, WI 53097",
    "Concordia University, Mequon, WI 53097",
    "975 University Ave, Madison, WI 53706",
    "100 W Capitol Dr Appleton WI 54911"
]

# Create or open a CSV file for writing
with open("geocodes.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(["Address", "Latitude", "Longitude"])
    
    # Iterate through the list of addresses
    for address in addresses:
        retry_count = 0
        
        while retry_count < 3:  # Maximum of 3 retries
            try:
                location = geolocator.geocode(address, timeout=10)  # Set a 10-second timeout
                if location:
                    # Extract data
                    addr = location.address
                    lat = location.latitude
                    lon = location.longitude
                    # Write data to the CSV file
                    csvwriter.writerow([addr, lat, lon])
                else:
                    # Write a placeholder for addresses not found
                    csvwriter.writerow([address, "Not Found", "Not Found"])
                break  # If successful, break out of the retry loop
            except Exception as e:
                print(f"Error: {str(e)}")
                retry_count += 1
                time.sleep(3)  # Add a delay of 3 seconds before the next retry
        time.sleep(3)  # Add a delay of 3 seconds between requests to respect the rate limit

print("done")