import folium
import pandas as pd


# Create a map centered at a specific location with a specific zoom level
map = folium.Map(location=[44.500000, -89.500000], zoom_start=7.5)

# Create a base map layer
folium.TileLayer("Cartodb dark_matter", show=True).add_to(map)
folium.TileLayer("OpenStreetMap").add_to(map)



# Create a layer control to allow users to switch between map layers
folium.LayerControl().add_to(map)

# Read data from the CSV files
tournaments_df = pd.read_csv('scraped_data.csv')  # Contains tournament data, including image URLs
coordinates_df = pd.read_csv('geocodes.csv')  # Contains coordinates

# Merge the data based on a common column (e.g., tournament names)
merged_df = tournaments_df.merge(coordinates_df, on='Address')

# Plot markers on the map based on the merged data
for index, row in merged_df.iterrows():
    lat = row['Latitude']
    long = row['Longitude']
    name = row['Name']
    start_time = row['Time']
    event_link = row['Link']
    date = row['Date']
    image_url = row['Image']  # Make sure you have an 'Image' column in your tournament_data.csv

    # Create a popup for the marker with additional information, including the image
    # Create a popup for the marker with additional information
    popup_content = f"<h1>{name}</h1><br><span style='font-size: 14px;'>Start Time: {start_time}</span><br><span style='font-size: 14px;'>Date: {date}</span><br>Event Link: <a href='{event_link}'>Link</a><br><img src='{image_url}' alt='Tournament Image' width='300' height='300'>"
    popup = folium.Popup(popup_content, max_width=400)


    folium.Marker(location=[lat, long], icon=folium.Icon(color='blue'), popup=popup).add_to(map)
    # You can customize the appearance of the points by adjusting the icon parameters.

# Display the map
map.save('my_map_with_points.html')  # Save the map to an HTML file

