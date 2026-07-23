# Website for Grant's Travel Photos
Website to display Grant's travel photos.

You can visit the website at: [*website domain coming soon*]


# Instructions for Grant
I have designed this website so Grant does not need to do ANY coding.
All he will ever need to do is update the data in `countries.csv`, and upload photos to `images/`.


### Editing the CSV
The CSV file contains information about each country.
All the info in the CSV is reflected in the website's content.

Things that can be changed in the CSV:
* The groupings of countries on the map (including adding new groups)
* If you have visited a country or not
* The name of countries
* The year you last visited the country

Once you have made your changes *and saved the file*, make your changes take effect by:
1. Opening the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Typing `python3 scripts/build_from_csv.py` and hitting enter


### Uploading Photos
In order for my script to work, photos must be named following a particular format.
Photos should be named `<CountryCode>_<CityName>_<OrderingNumber>_<ExtraInfo>`.
Each section of the filename should be separate by an underscore (_).
Photos can be any image format (jpg, jpeg, png, gif).

Photos are organized per country, per city.
Only one countries photos will be displayed at a time.
All the photos for that country will be grouped per city.
There is a clear separation between photos for different cities.

* The `CountryCode` is the ISO two-letter country code for that country.
For example, the United States' country code is "US".
You can find all country codes in `countries.csv`.

* The `CityName` is the name of the city (as you want it displayed).
If the city name has a space in it, replace the space with a hyphen (-).

* The `OrderingNumber` determines what order the photo is displayed for that specific city.
The photo with the *smallest* number will be displayed first.
The numbers do not need to start at 1 and count up.
This *does not* impact the order in which cities are displayed. Cities will always be displayed in alphabetical order.

* The `ExtraInfo` is just extra info to help you remember what the photo is for.
It is not used by me, so you can put whatever you want there.
If you do not want to include any extra info, you can just end the filename after the OrderingNumber.

Examples:
* If you want to upload a photo for Qarshi in Uzbekistan that you want displayed third, you should name the file `uz_qarshi_3.jpg`
* If you want to upload a photo of the alamo for San Antonio in the United States that you want displayed first, you should name the file `us_san-antonio_1_alamo.jpg`.



# Design Notes
### Repository Structure
The repository structure is pretty self-explanatory, but here is a quick rundown:
* `flags/` images of the flags for each country
* `fonts/` custom fonts used
* `images/` all the photos from Grant's travels
* `images/styling` all the images used by HTML/CSS for styling purposes
* `scripts/` python scripts which are used by me to help during development
* All HTML, CSS, and JavaScript source files are located in the home directory

### Resources
* https://www.iban.com/country-codes
* https://simplemaps.com/
* https://flagicons.lipis.dev/


<!-- * STYLE: vintage travel posters
* STYLE: middle eastern tiles

* [-] STRETCH GOAL - recreate flighty? -->



 --------------------------------------------------------------
### QUESTIONS
* [-] In country table, add column for the order in which each country was visited?
* [-] In country table, color code the countries in some way (green, yellow, red)? number of days? recency of visit? enjoyment of travel there? recommendation to others?
* [-] Does grant want a "default country" to display pictures of?
* [-] Does grant also want to display "fun facts" when a country is clicked on? Like the capital, population, language, etc.

### DONE:
* [+] Why script doesnt work for grant (think this was just because i didnt push my changes, oopsie)
* [+] Added postcard page (although the styles don't match at all anymore, may need to redo)
* [+] Add flag to country info when clicked
* [+] Add box to skip to certain cities
* [+] Build script to automatically add HTML for all photos
* [+] Build script to put city subheader to separate photos
* [+] Build script to put photos in correct order (should be automatic since in alpha order)
* [+] Make clicking on city entries go to city subheader
* [+] Hide city table until a country is clicked on

### TODO:
#### Design
* [-] Add paneling around each letter in the table to mimic departure display
* [-] Make each photo look like a polaroid?
* [-] Info box look like passport page?

#### Website Code
* [-] Stop SVG canvas from changing size when zooming
* [-] Allocate some default space for the photo container
* [-] Make display on mobile (single column for everything)

#### Scripts
* [+] Add script to allow grant to edit the caption for a photo
    * Something like `edit_caption <country> <city> <photoNumber | photoName> <caption>`
* [+] Add script to easily change image orders by changing the OrderNumber in all filenames
    * Something like `change_order <currentFilename> <newFilename>`
* [-] Add cache to remember captions across build process (ignoring the orderNumber)