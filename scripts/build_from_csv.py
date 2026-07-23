import sys
import os
import csv
from bs4 import BeautifulSoup, Comment
from bs4.formatter import HTMLFormatter
from pathlib import Path

# TODO: just redo entire build file at some point, is very messy due to so many big design changes

# This file will update the website based on the info countries.csv
# This is intended to do EVERYTHING, that way Grant doesn't have to every look at any code, and can just make his changes in the CSV

# Get command line arguments
if (os.getcwd().split("/")[-1].lower() != "grants_map" and os.getcwd().split("/")[-1].lower() != "grantsmap"):
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

# Read in HTML file as string
html_string = None
with open("index.html", "r", encoding="utf-8") as file:
    html_string = file.read()

soup = BeautifulSoup(html_string, "html.parser")



# /*-- ================================================ --->
# <---                PULL CSV CHANGES                  --->
# <--- ================================================ --*/
country_table_html = "<tbody>\n\t\t\t\t\t"
for row in csv_data[1:]:
    (country_code, country_name, group, visited, year_visited) = row
    visited = visited.strip().lower() == "true"

    path_element = soup.find(id=country_code)
    if path_element == None:
        print(f"WARNING: Country {country_name} ({country_code}) not found in HTML")
        continue

    # Set visited class in path if needed
    if visited and "visited" not in path_element["class"]:
        print(f"INFO: Marking {country_name} ({country_code}) as visited")
        path_string = f"<path id=\"{country_code}\" class=\"country visited"
        html_string = html_string.replace(f"<path id=\"{country_code}\" class=\"country", path_string)

    elif not visited and "visited" in path_element["class"]:
        print(f"INFO: Removing visited mark from {country_name} ({country_code})")
        path_string = f"<path id=\"{country_code}\" class=\"country"
        html_string = html_string.replace(f"<path id=\"{country_code}\" class=\"country visited", path_string)

    # Shift country path to new group if needed
    path_element = soup.find(id=country_code)
    html_group = path_element.parent["id"]
    if html_group != group:
        print(f"INFO: Moving country {country_name} ({country_code}) from group {html_group} to {group}")
        
        start = html_string.find(f"<path id=\"{country_code}\"")
        end = html_string.find("/>", start) + 2
        path_string = html_string[start:end]

        old_group_string = f"<g id=\"{group}\">"
        new_group_string = f"<g id=\"{group}\">" + "\n\t\t\t\t" + path_string

        # If creating a new group
        if old_group_string not in html_string:
            print(f"INFO: Creating a new group for {group}")
            old_group_string = f"</g>\n\t\t</svg>"
            new_group_string = f"</g>\n\t\t\t<g id=\"{group}\">" + "\n\t\t\t\t" + path_string + "\n\t\t\t</g>\n\t\t</svg>"

        html_string = html_string.replace(path_string, "")
        html_string = html_string.replace(old_group_string.expandtabs(4), new_group_string.expandtabs(4))
    
    # Update table
    if visited:
        country_entry = f"<tr><td><span class=\"country-entry\" data-code=\"{country_code}\">{country_name.replace('_', ' ').title()}</span></td><td>{year_visited}</td></tr>\n\t\t\t\t\t"
        country_table_html += country_entry.expandtabs(4)



# /*-- ================================================ --->
# <---               PULL IMAGE CHANGES                 --->
# <--- ================================================ --*/
cities_table_html = "<tbody>\n\t\t\t\t\t\t"
photos_html = "<div id=\"photos-container\">\n\t\t\t"
current_country = None
current_city = None
for filepath in sorted(Path("./images").glob("*")):
    if not filepath.is_file():
        continue
    
    valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
    if not filepath.suffix.lower() in valid_extensions:
        print(f"File {filepath} in images folder is not an image file! Must have extension {valid_extensions}")

    # Get info about image
    try:
        metadata = filepath.name.replace(".", "_").split("_")
        country_code = metadata[0].upper()
        raw_city_name = metadata[1]
        formatted_city_name = metadata[1].replace("-", " ").title()
        order = int(metadata[2])
    except Exception as e:
        print(f"ERROR: filename \"{filepath.name}\" does not follow the format <CountryCode>_<CityName>_<OrderingNumber>_<ExtraInfo>! Make sure to use hyphens (-) instead of spaces in the city name.\n\tExample filenames: \"us_boston_1_example.jpg\" or \"us_san-antonio_4_riverwalk.jpg\")")
        continue

    # Determine if we have moved on to a new country
    is_new_country = country_code != current_country
    if is_new_country:
        # Close the old country photo container, and open a new one for this country
        photo_container_string = f"</div>\n\t\t\t<div id=\"{country_code}-photos\" class=\"country-photos hidden\">\n\t\t\t"
        if current_country == None:
            photo_container_string = photo_container_string.replace("</div>\n\t\t\t", "")
        photos_html += photo_container_string

        current_country = country_code
    
    # Determine if we have moved on to a new city
    is_new_city = raw_city_name != current_city
    if is_new_city:
        # Add divider for each city
        photos_html += f"\t<div id=\"{country_code}-{raw_city_name}\" class=\"city-divider\">{formatted_city_name}</div>\n\t\t\t"
        current_city = raw_city_name 

    # Add the city to the table
    city_entry = f"<tr class=\"city-row {country_code}-city\"><td><span class=\"city-entry\" data-photos=\"{country_code}-{raw_city_name}\">{formatted_city_name}</span></td></tr>\n\t\t\t\t\t\t"
    if city_entry.strip() not in cities_table_html:
        cities_table_html += city_entry.expandtabs(4)
    
    # Add the image to the country's photo container HTML
    photos_html += \
        f"""    <div class=\"photo-wrapper\">
                    <img class=\"photo\" src=\"{filepath}\">
                    <div class=\"photo-caption\"></div>
                </div>
            """

# Close last photos container
photos_html += "</div>\n\t\t"



# /*-- ================================================ --->
# <---                  WRITE CHANGES                   --->
# <--- ================================================ --*/
# Replace country table
start = html_string.find("<tbody>", html_string.index("table id=\"countries-table\""))
end = html_string.find("</tbody>", start)
html_string = html_string[:start] + country_table_html[:-4] + html_string[end:]

# Replace cities table
start = html_string.find("<tbody>", html_string.index("table id=\"cities-table\""))
end = html_string.find("</tbody>", start)
html_string = html_string[:start] + cities_table_html[:-4] + html_string[end:]

# Replace photos container
start = html_string.find("<div id=\"photos-container\">")
end = html_string.find("</div> <!-- END OF PHOTOS -->", start)
html_string = html_string[:start] + photos_html + html_string[end:]

# Write changes to HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_string)