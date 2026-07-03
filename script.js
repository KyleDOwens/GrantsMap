const countries = document.querySelectorAll('.country');
const svg = document.getElementById("map-svg");
const infoBox = document.getElementById("info-box");
const secondaryInfoBox = document.getElementById("secondary-info-box");

let zoomedGroup = null;
let displayedCountry = null;
let secondaryInfoTimer = null;

const codeMappings = {
    "AF": "afghanistan",
    "AO": "angola",
    "AL": "albania",
    "AE": "united_arab_emirates",
    "AR": "argentina",
    "AM": "armenia",
    "AU": "australia",
    "AT": "austria",
    "AZ": "azerbaijan",
    "BI": "burundi",
    "BE": "belgium",
    "BJ": "benin",
    "BF": "burkina_faso",
    "BD": "bangladesh",
    "BG": "bulgaria",
    "BH": "bahrain",
    "BA": "bosnia_and_herzegovina",
    "BY": "belarus",
    "BZ": "belize",
    "BO": "bolivia",
    "BR": "brazil",
    "BN": "brunei_darussalam",
    "BT": "bhutan",
    "BW": "botswana",
    "CF": "central_african_republic",
    "CA": "canada",
    "CH": "switzerland",
    "CL": "chile",
    "CN": "china",
    "CI": "côte_d'ivoire",
    "CM": "cameroon",
    "CD": "democratic_republic_of_the_congo",
    "CG": "republic_of_congo",
    "CO": "colombia",
    "CR": "costa_rica",
    "CU": "cuba",
    "CZ": "czech_republic",
    "DE": "germany",
    "DJ": "djibouti",
    "DK": "denmark",
    "DO": "dominican_republic",
    "DZ": "algeria",
    "EC": "ecuador",
    "EG": "egypt",
    "ER": "eritrea",
    "EE": "estonia",
    "ET": "ethiopia",
    "FI": "finland",
    "FJ": "fiji",
    "GA": "gabon",
    "GB": "united_kingdom",
    "GE": "georgia",
    "GH": "ghana",
    "GN": "guinea",
    "GM": "the_gambia",
    "GW": "guinea",
    "GQ": "equatorial_guinea",
    "GR": "greece",
    "GL": "greenland",
    "GT": "guatemala",
    "GY": "guyana",
    "HN": "honduras",
    "HR": "croatia",
    "HT": "haiti",
    "HU": "hungary",
    "ID": "indonesia",
    "IN": "india",
    "IE": "ireland",
    "IR": "iran",
    "IQ": "iraq",
    "IS": "iceland",
    "IL": "israel",
    "IT": "italy",
    "JM": "jamaica",
    "JO": "jordan",
    "JP": "japan",
    "KZ": "kazakhstan",
    "KE": "kenya",
    "KG": "kyrgyzstan",
    "KH": "cambodia",
    "KR": "south_korea",
    "XK": "kosovo",
    "KW": "kuwait",
    "LA": "laos",
    "LB": "lebanon",
    "LR": "liberia",
    "LY": "libya",
    "LK": "sri_lanka",
    "LS": "lesotho",
    "LT": "lithuania",
    "LU": "luxembourg",
    "LV": "latvia",
    "MA": "morocco",
    "MD": "moldova",
    "MG": "madagascar",
    "MX": "mexico",
    "MK": "macedonia",
    "ML": "mali",
    "MM": "myanmar",
    "ME": "montenegro",
    "MN": "mongolia",
    "MZ": "mozambique",
    "MR": "mauritania",
    "MW": "malawi",
    "MY": "malaysia",
    "NA": "namibia",
    "NE": "niger",
    "NG": "nigeria",
    "NI": "nicaragua",
    "NL": "netherlands",
    "NO": "norway",
    "NP": "nepal",
    "NZ": "new_zealand",
    "OM": "oman",
    "PK": "pakistan",
    "PA": "panama",
    "PE": "peru",
    "PH": "philippines",
    "PG": "papua_new_guinea",
    "PL": "poland",
    "KP": "north_korea",
    "PT": "portugal",
    "PY": "paraguay",
    "PS": "palestine",
    "QA": "qatar",
    "RO": "romania",
    "RU": "russia",
    "RW": "rwanda",
    "EH": "western_sahara",
    "SA": "saudi_arabia",
    "SD": "sudan",
    "SS": "south_sudan",
    "SN": "senegal",
    "SL": "sierra_leone",
    "SV": "el_salvador",
    "RS": "serbia",
    "SR": "suriname",
    "SK": "slovakia",
    "SI": "slovenia",
    "SE": "sweden",
    "SZ": "swaziland",
    "SY": "syria",
    "TD": "chad",
    "TG": "togo",
    "TH": "thailand",
    "TJ": "tajikistan",
    "TM": "turkmenistan",
    "TL": "timor-leste",
    "TN": "tunisia",
    "TR": "turkey",
    "TW": "taiwan",
    "TZ": "tanzania",
    "UG": "uganda",
    "UA": "ukraine",
    "UY": "uruguay",
    "US": "united_states",
    "UZ": "uzbekistan",
    "VE": "venezuela",
    "VN": "vietnam",
    "VU": "vanuatu",
    "YE": "yemen",
    "ZA": "south_africa",
    "ZM": "zambia",
    "ZW": "zimbabwe",
    "SO": "somalia",
    "GF": "french_guiana",
    "FR": "france",
    "ES": "spain",
    "AW": "aruba",
    "AI": "anguilla",
    "AD": "andorra",
    "AG": "antigua_and_barbuda",
    "BS": "bahamas",
    "BM": "bermuda",
    "BB": "barbados",
    "KM": "comoros",
    "CV": "cape_verde",
    "KY": "cayman_islands",
    "DM": "dominica",
    "FK": "falkland_islands",
    "FO": "faeroe_islands",
    "GD": "grenada",
    "HK": "hong_kong",
    "KN": "saint_kitts_and_nevis",
    "LC": "saint_lucia",
    "LI": "liechtenstein",
    "MF": "saint_martin",
    "MV": "maldives",
    "MT": "malta",
    "MS": "montserrat",
    "MU": "mauritius",
    "NC": "new_caledonia",
    "NR": "nauru",
    "PN": "pitcairn_islands",
    "PR": "puerto_rico",
    "PF": "french_polynesia",
    "SG": "singapore",
    "SB": "solomon_islands",
    "ST": "são_tomé_and_principe",
    "SX": "saint_martin",
    "SC": "seychelles",
    "TC": "turks_and_caicos_islands",
    "TO": "tonga",
    "TT": "trinidad_and_tobago",
    "VC": "saint_vincent_and_the_grenadines",
    "VG": "british_virgin_islands",
    "VI": "united_states_virgin_islands",
    "CY": "cyprus",
    "RE": "reunion",
    "YT": "mayotte",
    "MQ": "martinique",
    "GP": "guadeloupe",
    "CW": "curaco",
    "IC": "canary_islands",
    "BL": "saint_barthélemy",
    "GU": "guam",
    "WS": "samoa",
    "AS": "american_samoa",
    "MP": "northern_mariana_islands",
    "PW": "palau",
    "MH": "marshall_islands",
    "FM": "micronesia",
    "TV": "tuvalu",
    "BQS": "caribbean_netherlands",
    "BQB": "caribbean_netherlands",
    "BQS": "caribbean_netherlands",
    "VA": "vatican_city",
}

/**
 * Formats the behind the scenes country name to a printable version.
 * Capitalizes the first character, and all characters following "special" characters in the country name.
 * Replace underscores with spaces
 * @param {*} name the country name to convert to print version
 */
function getCountryPrintName(code) {
    let name = codeMappings[code];
    console.log(code);
    printName = "";
    printName += name[0].toUpperCase();
    name = name.replaceAll("_", " ");
    for (let i = 1; i < name.length; i++) {
        if (("-' _".includes(name[i - 1])) && !(name[i - 1] == " " && name[i + 1] == "'")) { // Second boolean is an exception made for Côte d'Ivoire
            printName += name[i].toUpperCase();
        }
        else {
            printName += name[i];
        }
    }

    return printName
}

function getGroupFromCountry(country) {
    let classArray = Array.from(country.classList); 
    classArray = classArray.filter(item => item !== "country" && item !== "visited");
    return classArray[0];
}

function getBoundingBox(group) {
    let groupElements = document.getElementById(group);
    return groupElements.getBBox()
}

function drawSvgLine(x1, y1, x2, y2, color, thickness) {
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", x1);
    line.setAttribute("y1", y1);
    line.setAttribute("x2", x2);
    line.setAttribute("y2", y2);
    line.setAttribute("stroke", color);
    line.setAttribute("stroke-width", thickness);
    line.setAttribute("stroke-linecap", "round");
    svg.appendChild(line);
}

function smoothViewBoxTransition(targetX, targetY, targetWidth, targetHeight, duration) {
  const start = performance.now();
  
  // Parse current viewBox
  const currentAttr = svg.getAttribute('viewBox').split(' ').map(Number);
  const [startX, startY, startWidth, startHeight] = currentAttr;

  function step(time) {
    const elapsed = time - start;
    const progress = Math.min(elapsed / duration, 1);
    
    const ease = 1 - Math.pow(1 - progress, 3);

    const x = startX + (targetX - startX) * ease;
    const y = startY + (targetY - startY) * ease;
    const width = startWidth + (targetWidth - startWidth) * ease;
    const height = startHeight + (targetHeight - startHeight) * ease;

    svg.setAttribute('viewBox', `${x} ${y} ${width} ${height}`);

    if (progress < 1) {
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}

function getZoomPaddings(totalWidth, totalHeight, zoomWidth, zoomHeight) {
    let widthScale = zoomWidth / totalWidth;
    let heightScale = zoomHeight / totalHeight;
    let scale = 1;

    let baseWidthPadding = 25;
    let baseHeightPadding = baseWidthPadding*(totalHeight/totalWidth);

    // If width bound
    if (widthScale >= heightScale) {
        scale = widthScale;
        widthPadding = baseWidthPadding + ((totalWidth * scale - zoomWidth) / 2);
        heightPadding = ((totalHeight * scale - zoomHeight) / 2);
    }
    // If height bound
    else {
        scale = heightScale;
        heightPadding = baseHeightPadding + ((totalHeight * scale - zoomHeight) / 2);
        widthPadding = baseWidthPadding + ((totalWidth * scale - zoomWidth) / 2);
    }

    return [widthPadding, heightPadding]
}

function zoomIntoGroup(group) {
    // Get zoom bounding box and set it
    let bbox = getBoundingBox(group);
    let paddings = getZoomPaddings(svg.getBoundingClientRect().width, svg.getBoundingClientRect().height, bbox.width, bbox.height);
    let widthPadding = paddings[0];
    let heightPadding = paddings[1];
    zoomedGroup = group;
    smoothViewBoxTransition(bbox.x - widthPadding, bbox.y - heightPadding, bbox.width + (widthPadding * 2), bbox.height + (heightPadding * 2), 750);

    // Unhighlight all countries in the group once we zoom in to switch to individual country highlighting
    unhighlightGroup(group);

    // drawSvgLine(bbox.x, bbox.y, bbox.x + bbox.width, bbox.y, "red", 1);
    // drawSvgLine(bbox.x, bbox.y, bbox.x, bbox.y + bbox.height, "red", 1);
    // drawSvgLine(bbox.x + bbox.width, bbox.y, bbox.x + bbox.width, bbox.y + bbox.height, "red", 1);
    // drawSvgLine(bbox.x, bbox.y + bbox.height, bbox.x + bbox.width, bbox.y + bbox.height, "red", 1);

    // drawSvgLine((bbox.x - widthPadding), (bbox.y - heightPadding), (bbox.x - widthPadding) + (bbox.width + (widthPadding * 2)), (bbox.y - heightPadding), "blue", 3);
    // drawSvgLine((bbox.x - widthPadding), (bbox.y - heightPadding), (bbox.x - widthPadding), (bbox.y - heightPadding) + (bbox.height + (heightPadding * 2)), "blue", 3);
    // drawSvgLine((bbox.x - widthPadding) + (bbox.width + (widthPadding * 2)), (bbox.y - heightPadding), (bbox.x - widthPadding) + (bbox.width + (widthPadding * 2)), (bbox.y - heightPadding) + (bbox.height + (heightPadding * 2)), "blue", 3);
    // drawSvgLine((bbox.x - widthPadding), (bbox.y - heightPadding) + (bbox.height + (heightPadding * 2)), (bbox.x - widthPadding) + (bbox.width + (widthPadding * 2)), (bbox.y - heightPadding) + (bbox.height + (heightPadding * 2)), "blue", 3);
}

function highlightGroup(group) {
    document.querySelectorAll('.' + group).forEach((groupItem, index) => {
        groupItem.style.fill = (groupItem.classList.contains("visited")) ? "#3d8c40" : "#6d8396";;
    });
}

function unhighlightGroup(group) {
    document.querySelectorAll('.' + group).forEach((groupItem, index) => {
        groupItem.style.fill = (groupItem.classList.contains("visited")) ? "#4CAF50" : "#88a4bc";;
    });
}

function hideDisplayedPhotos(countryCode) {
    if (displayedCountry != null && document.getElementById(countryCode + "_photos") != null) {
        document.getElementById(displayedCountry + "_photos").classList.add("hidden");
    }
    displayedCountry = null;
}

function displayPhotos(countryCode) {
    if (countryCode != null && document.getElementById(countryCode + "_photos") != null) {
        infoBox.textContent = `Photos from ${getCountryPrintName(countryCode)} (${countryCode})`;
        document.getElementById(countryCode + "_photos").classList.remove("hidden");
    }
    displayedCountry = countryCode;
}

function clearSecondaryInfoTimer() {
    if (secondaryInfoTimer) {
        clearTimeout(secondaryInfoTimer);
        secondaryInfoBox.style.display = "none";
    }
}

function resetSecondaryInfoTimer() {
    clearSecondaryInfoTimer();
    secondaryInfoBox.style.display = "block";
    secondaryInfoTimer = setTimeout(() => {
        secondaryInfoBox.style.display = "none";
    }, 5000);
}

countries.forEach(country => {
    // Handle clicking a country - zoom to region and scale up
    country.addEventListener('click', () => {
        let group = getGroupFromCountry(country);
        if (zoomedGroup == null || group != zoomedGroup) {
            zoomIntoGroup(group);
        }
        else {
            let countryCode = country.getAttribute('id');
            if (country.classList.contains("visited")) {
                hideDisplayedPhotos(countryCode);
                displayPhotos(countryCode);
                clearSecondaryInfoTimer();
            }
            else {
                secondaryInfoBox.style.display = "block";
                secondaryInfoBox.textContent = `No photos! Grant hasn't visited ${getCountryPrintName(countryCode)} (or hasn't uploaded photos)`;
                resetSecondaryInfoTimer();
            }
        }
    });

    // Highlight group on hover
    country.addEventListener('mouseenter', () => {
        let group = getGroupFromCountry(country);
        if (zoomedGroup != null && group == zoomedGroup) {
            country.style.fill = (country.classList.contains("visited")) ? "#3d8c40" : "#6d8396";
            document.getElementById("cursor-text").style.display = "block";
            document.getElementById("cursor-text").innerText = getCountryPrintName(country.getAttribute('id'));
        }
        else {
            highlightGroup(group);
        }
    });

    // Unhighlight group on ending hover
    country.addEventListener('mouseleave', () => {
        let group = getGroupFromCountry(country);
        if (zoomedGroup != null && group == zoomedGroup) {
            country.style.fill = (country.classList.contains("visited")) ? "#4CAF50" : "#88a4bc";
            document.getElementById("cursor-text").style.display = "none";
        }
        else {
            unhighlightGroup(group);
        }
    });
});

document.getElementById("overlay-btn").addEventListener("click", () => {
    zoomedGroup = null;
    smoothViewBoxTransition(0, 0, 700, 300, 750);
});

window.addEventListener('mousemove', (e) => {
    let cursorText = document.getElementById("cursor-text");
    cursorText.style.left = e.clientX + 16 + "px";
    cursorText.style.top = e.clientY + 16 + "px";
});
