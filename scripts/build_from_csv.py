import sys
import os
import csv
from bs4 import BeautifulSoup, Comment
from bs4.formatter import HTMLFormatter

# Get command line arguments
if (os.getcwd().split("/")[-1] != "grants_map"):
        exit("ERROR: This script must be run from the project root directory")

if len(sys.argv) > 1:
    print("This script takes no arguments! Usage:")
    print("python3 build_from_csv.py") 
    exit()

# Read in data from CSV
csv_data = None
with open("countries.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    csv_data = list(reader)

# Parse through HTML file
html_string = None
with open("index.html", "r", encoding="utf-8") as file:
    html_string = file.read()

soup = BeautifulSoup(html_string, "html.parser")

# Loop through CSV and make changes
for row in csv_data[1:]:
    (country_code, country_name, group, visited) = row
    visited = visited.strip().lower() == "true"

    # Get country element
    path_element = soup.find(id=country_code)
    if path_element == None:
        print(f"ERROR: Country {country_name} ({country_code}) not found in HTML")
        continue

    # Set visited class in path if needed
    if visited and "visited" not in path_element["class"]:
        print(f"Marking {country_name} ({country_code}) as visited")
        path_string = f"<path id=\"{country_code}\" class=\"country visited"
        html_string = html_string.replace(f"<path id=\"{country_code}\" class=\"country", path_string)

    elif not visited and "visited" in path_element["class"]:
        print(f"Removing visited mark from {country_name} ({country_code})")
        path_string = f"<path id=\"{country_code}\" class=\"country"
        html_string = html_string.replace(f"<path id=\"{country_code}\" class=\"country visited", path_string)
    
    # Add country-photos element if needed
    country_photos = soup.find(id=f"{country_code}-photos")
    if visited and country_photos == None:
        print(f"Adding new photo group for country {country_name} ({country_code})")

        photos_string = f"""<!-- {country_name.capitalize()} -->
        <div id="{country_code}-photos" class="country-photos hidden">
        </div>

        <!-- COUNTRY_PHOTOS_REPLACEME -->"""

        html_string = html_string.replace("<!-- COUNTRY_PHOTOS_REPLACEME -->", photos_string)


    # Shift country path to group if needed
    path_element = soup.find(id=country_code)
    html_group = path_element.parent["id"]
    if html_group != group:
        print(f"Moving country {country_name} ({country_code}) from group {html_group} to {group}")
        
        start = html_string.find(f"<path id=\"{country_code}\"")
        end = html_string.find("/>", start) + 2
        path_string = html_string[start:end]

        group_string = f"<g id=\"{group}\">" + "\n\t\t\t\t" + path_string

        html_string = html_string.replace(path_string, "")
        html_string = html_string.replace(f"<g id=\"{group}\">", group_string)
        

# Write changes to HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_string)