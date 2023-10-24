import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website you want to scrape
url = "https://www.windy.com/?31.540,75.913,5"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the HTML elements that contain the data you want to scrape
    temperature = soup.find("span", class_="temperature").text
    humidity = soup.find("span", class_="humidity").text
    
    # Create a list to store the data
    weather_data = [
        {"Measurement": "Temperature", "Value": temperature},
        {"Measurement": "Humidity", "Value": humidity}
    ]

    # Define the name of the CSV file to save the data
    csv_file = "weather_data.csv"

    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        fieldnames = ["Measurement", "Value"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in weather_data:
            writer.writerow(data)

    print(f"Data scraped and saved to {csv_file}")
else:
    print("Failed to retrieve data from the website.")
