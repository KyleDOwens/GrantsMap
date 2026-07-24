# Website for Grant's Travel Photos
Website to display Grant's travel photos.

You can visit the website at: [*website domain coming soon*]


# Instructions for Grant
I have designed this website so Grant does not need to do ANY coding.
All he will ever need to do is update the data in `countries.csv`, and upload photos to `images/`.

There are additional helper scripts to change photo captions and alter the order of photos.

I can't account for every possible edge case, so if things go wrong and my notes don't mention how to fix it, text/call me.


### Editing the CSV
The CSV file `countries.csv` contains information about each country.
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
This *does not* impact the order in which cities are displayed.
Cities will always be displayed in alphabetical order.

* The `ExtraInfo` is just extra info to help you remember what the photo is for.
It is not used by me, so you can put whatever you want there.
If you do not want to include any extra info, you can just end the filename after the OrderingNumber.

Examples:
* If you want to upload a photo for Qarshi in Uzbekistan that you want displayed 3rd, you should name the file `uz_qarshi_3.jpg`
* If you want to upload a photo of the alamo for San Antonio in the United States that you want displayed 1st, you should name the file `us_san-antonio_1_alamo.jpg`.


### Changing a Photo Caption
By default, all photos will be uploaded without a caption.
To add a caption to them, you will need to use one of my scripts.
1. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Type `python3 scripts/edit_caption.py <CountryCode> <CityName> <OrderingNumber> <Caption>` (and fill in all the fields with the correct info) and hit enter

For each field in the script, fill them in following the same instructions as the filename.
So:
* `CountryCode` should be the ISO two-letter code for the country of the photo.
* `CityName` is the city name of the photo, with any spaces replaced by a hyphen (-).
* `OrderingNumber` is the current ordering number of the photo.
* `Caption` is the full caption that you want to include, surrounded by quotation marks. It can be as long as you want, and *can* include spaces.

For example, running `python3 ./scripts/edit_caption.py us san-antonio 2 "this is my example caption"` will set the caption to "this is my example caption" for the 2nd photo for San Antonio when the United States is selected.


### Changing the Order of Photos
As described in the section about uploading photos, all photos will be displayed in order of the `OrderingNumber` in their filename.
Ideally, you won't be picky about the order and will just add photos one after the other.

But, if you want to change the order of photos after you have uploaded them, there are two different options.
1) You can manually change the filename to the new number you want it displayed as. Note that the order cannot be guaranteed if two photos have the same `OrderingNumber` (but it may). This may require you to change multiple filenames to make sure everything is in the right order and there are no repeats.
2) You can use a script I wrote that will automatically update the filename, and update all other filenames to make sure there are not duplicate `OrderingNumber`s (preserving the relative order of all the other photos).

To use the script,
1. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Type `python3 scripts/change_photo_order.py <CountryCode> <CityName> <OldOrderingNumber> <NewOrderingNumber>` (and fill in all the fields with the correct info) and hit enter

For each field in the script, fill them in following the same instructions as the filename.
So:
* `CountryCode` should be the ISO two-letter code for the country of the photo.
* `CityName` is the city name of the photo, with any spaces replaced by a hyphen (-).
* `OldOrderingNumber` is the *current* ordering number of the photo you want to move.
* `NewOrderingNumber` is the *new* ordering number you want to move the current photo to.

For example, running `python3 ./scripts/change_photo_order.py us san-antonio 4 1` will move the photo current displayed 4th, to instead be displayed 1st.


## How to Upload Your Website Changes
The website code on your computer is not the real website code.
It is just a copy of the code.
So whenever you make any changes, you will have to upload the new code onto the server where the website is stored.

To do this:
1. Complete all the changes you want to make.
2. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
3. Type `git add *` and hit enter
4. Type `git commit -m "<YourMessage>"` (replacing &lt;YourMessage&gt; with a short summary of what the changes are) and hit enter
5. Type `git push` and hit enter


## How to Download the Latest Version of the Website
In order to make any changes to the website, you will have to make sure you are changing the most recent version of the website.
The version on your computer might be an older version of the website, and you will have to redownload it to be the newest version.

To check if you need to update the website:
1. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Type `git status` (and fill in all the fields with the correct info) and hit enter
3. You are up-to-date if you see a message similar to 
    ```
    On branch main
    Your branch is up to date with 'origin/main'.
    nothing to commit, working directory clean
    ```

If you got a different message, that means the version on your computer is likely old.
To update it to the latest version:
1. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Type `git pull` and hit enter

IMPORTANT NOTE:
You sometime may be able to download the latest version of the website if you have made any changes to the website without uploading them!
You will know this is the case if you try to download the latest version and get a message that is similar to:
```
error: Your local changes to the following files would be overwritten by merge:
    <filename>
Please commit your changes or stash them before you merge.
Aborting
```

To fix this and download the latest version:
1. Open the terminal by pressing `'Ctrl' + '~'` on your keyboard
2. Type `git stash` and hit enter
3. Type `git pull` and hit enter
2. Type `git stash pop` and hit enter


 --------------------------------------------------------------

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


 --------------------------------------------------------------
### QUESTIONS
* [-] In country table, add column for the order in which each country was visited?
* [-] In country table, color code the countries in some way (green, yellow, red)? number of days? recency of visit? enjoyment of travel there? recommendation to others?
* [-] Does grant want a "default country" to display pictures of?
* [-] Does grant also want to display "fun facts" when a country is clicked on? Like the capital, population, language, etc.
* [-] Get Grant a GitHub account set up so I can eventually transfer ownership to him (and give myself edit permissions) (maybe make it so we both know password so I can log in if needed)

### DONE:
* [+] Why script doesnt work for grant (i didnt push my changes, oopsie)
* [+] Added postcard page (styles don't match at all anymore, may need to redo)
* [+] Add flag to country info when clicked
* [+] Add box to skip to certain cities
* [+] Build script to automatically add HTML for all photos
* [+] Build script to put city subheader to separate photos
* [+] Build script to put photos in correct order (should be automatic since in alpha order)
* [+] Make clicking on city entries go to city subheader
* [+] Hide city table until a country is clicked on
* [+] Add script to allow grant to edit the caption for a photo
* [+] Add script to easily change image orders
* [+] Add cache to remember captions across build process (ignoring the orderNumber)
* [+] Write documentation for Grant for the photo scripts

### TODO:
#### Design
* [-] Add paneling around each letter in the table to mimic departure display
* [-] Make each photo look like a polaroid?
* [-] Info box look like passport page?
* [-] Steal kyle's world scrollbars

#### Website Code
* [-] Stop SVG canvas from changing size when zooming
* [-] Allocate some default space for the photo container
* [-] Make display on mobile (single column for everything)
* [-] Make the map back button only be visible when zoomed into a group