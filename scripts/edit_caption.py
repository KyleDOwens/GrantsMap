import sys
import os

# Get command line arguments
cwd = os.getcwd().replace("\\", "/")
if (cwd.split("/")[-1].lower() != "grants_map" and cwd.split("/")[-1].lower() != "grantsmap"):
    exit("ERROR: This script must be run from the project root directory")

if len(sys.argv) < 5:
    print("This script takes 5 arguments! Usage:")
    print("python3 edit_caption.py <CountryCode> <CityName> <OrderNumber> <Caption>") 
    exit()

country_code, city_name, order_num = sys.argv[1:4]
caption = " ".join(sys.argv[4:])

# Read in HTML file as string
html_string = None
with open("index.html", "r", encoding="utf-8") as file:
    html_string = file.read()

# Find photo
filename = f"{country_code}_{city_name}_{order_num}"

# Replace caption in HTML
start = html_string.find("<div class=\"photo-caption\">", html_string.find(filename))
end = html_string.find("</div>", start)
caption = "<div class=\"photo-caption\">" + caption
html_string = html_string[:start] + caption + html_string[end:]

# Write changes to HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_string)