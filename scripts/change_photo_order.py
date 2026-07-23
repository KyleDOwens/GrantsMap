from pathlib import Path
import subprocess
import sys
import os

# Get command line arguments
if (os.getcwd().split("/")[-1].lower() != "grants_map" and os.getcwd().split("/")[-1].lower() != "grantsmap"):
        exit("ERROR: This script must be run from the project root directory")

if len(sys.argv) != 5:
    print("This script takes 5 arguments! Usage:")
    print("python3 edit_caption.py <CountryCode> <CityName> <OldOrderNumber> <NewOrderNumber>") 
    exit()

country_code, city_name, old_num, target_num = sys.argv[1:]

try:
    country_code = country_code.lower()
    city_name = city_name.lower()
    old_num = int(old_num)
    target_num = int(target_num)
except Exception as e:
    print("Incorrect arguments given. Make sure the country code and city name are letters, and the order numbers are numbers")
    exit()

if target_num == old_num:
    exit()



# Rename all image files
direction = 1 if (old_num > target_num) else -1

target_segments = None

for filepath in sorted(Path("./images").glob(f"{country_code}_{city_name}*"), reverse=(direction == 1)):
    is_target_file = f"{country_code}_{city_name}_{old_num}" in filepath.name
    
    segments = filepath.name.replace(".", "_").split("_") # countryCode, cityName, orderNum, extraInfo, extension
    order_num = int(segments[2])

    if not (old_num <= order_num <= target_num) and not (target_num <= order_num <= old_num):
        continue
    
    new_num = order_num + direction

    if is_target_file:
        renamed = f"target.{segments[-1]}"
        target_segments = segments
    elif (len(segments) == 4):
        renamed = f"{country_code}_{city_name}_{new_num}.{segments[-1]}"
    else:
        renamed = f"{country_code}_{city_name}_{new_num}_{segments[3]}.{segments[-1]}"
    
    print(f"Changing file '{filepath.name}' to '{renamed}'")
    new_filepath = filepath.with_name(renamed)
    filepath.rename(new_filepath)

target_path = Path(f"./images/target.{target_segments[-1]}")
target_path.rename(f"./images/{country_code}_{city_name}_{target_num}{f'_{target_segments[3]}' if len(target_segments) > 4 else ''}.{target_segments[-1]}")
print(f"Changing file '{target_path.name}' to '{country_code}_{city_name}_{target_num}{f'_{target_segments[3]}' if len(target_segments) > 4 else ''}.{target_segments[-1]}'")

# Call the build script
# result = subprocess.run(
#     [sys.executable, "./scripts/build_from_csv.py"], 
#     capture_output=True, 
#     text=True
# )