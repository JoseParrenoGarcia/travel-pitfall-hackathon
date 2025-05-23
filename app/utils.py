import json
import re

def safe_json_parse(raw: str) -> dict:
    """
    Tries to clean and parse a GPT-style JSON string.
    Strips markdown code blocks and parses JSON safely.
    """
    try:
        # Remove any ```json or ``` wrapping
        cleaned = re.sub(r"^```(json)?|```$", "", raw.strip(), flags=re.MULTILINE)
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "valid": False,
            "suggested_city": None,
            "suggested_country": None,
            "message": "Could not parse GPT response.",
            "raw": raw
        }

country_list = [
    {"name": "Aruba", "code": "AW", "flag": "🇦🇼"},
    {"name": "Afghanistan", "code": "AF", "flag": "🇦🇫"},
    {"name": "Angola", "code": "AO", "flag": "🇦🇴"},
    {"name": "Anguilla", "code": "AI", "flag": "🇦🇮"},
    {"name": "Åland Islands", "code": "AX", "flag": "🇦🇽"},
    {"name": "Albania", "code": "AL", "flag": "🇦🇱"},
    {"name": "Andorra", "code": "AD", "flag": "🇦🇩"},
    {"name": "United Arab Emirates", "code": "AE", "flag": "🇦🇪"},
    {"name": "Argentina", "code": "AR", "flag": "🇦🇷"},
    {"name": "Armenia", "code": "AM", "flag": "🇦🇲"},
    {"name": "American Samoa", "code": "AS", "flag": "🇦🇸"},
    {"name": "Antarctica", "code": "AQ", "flag": "🇦🇶"},
    {"name": "French Southern Territories", "code": "TF", "flag": "🇹🇫"},
    {"name": "Antigua and Barbuda", "code": "AG", "flag": "🇦🇬"},
    {"name": "Australia", "code": "AU", "flag": "🇦🇺"},
    {"name": "Austria", "code": "AT", "flag": "🇦🇹"},
    {"name": "Azerbaijan", "code": "AZ", "flag": "🇦🇿"},
    {"name": "Burundi", "code": "BI", "flag": "🇧🇮"},
    {"name": "Belgium", "code": "BE", "flag": "🇧🇪"},
    {"name": "Benin", "code": "BJ", "flag": "🇧🇯"},
    {"name": "Bonaire, Sint Eustatius and Saba", "code": "BQ", "flag": "🇧🇶"},
    {"name": "Burkina Faso", "code": "BF", "flag": "🇧🇫"},
    {"name": "Bangladesh", "code": "BD", "flag": "🇧🇩"},
    {"name": "Bulgaria", "code": "BG", "flag": "🇧🇬"},
    {"name": "Bahrain", "code": "BH", "flag": "🇧🇭"},
    {"name": "Bahamas", "code": "BS", "flag": "🇧🇸"},
    {"name": "Bosnia and Herzegovina", "code": "BA", "flag": "🇧🇦"},
    {"name": "Saint Barthélemy", "code": "BL", "flag": "🇧🇱"},
    {"name": "Belarus", "code": "BY", "flag": "🇧🇾"},
    {"name": "Belize", "code": "BZ", "flag": "🇧🇿"},
    {"name": "Bermuda", "code": "BM", "flag": "🇧🇲"},
    {"name": "Bolivia, Plurinational State of", "code": "BO", "flag": "🇧🇴"},
    {"name": "Brazil", "code": "BR", "flag": "🇧🇷"},
    {"name": "Barbados", "code": "BB", "flag": "🇧🇧"},
    {"name": "Brunei Darussalam", "code": "BN", "flag": "🇧🇳"},
    {"name": "Bhutan", "code": "BT", "flag": "🇧🇹"},
    {"name": "Bouvet Island", "code": "BV", "flag": "🇧🇻"},
    {"name": "Botswana", "code": "BW", "flag": "🇧🇼"},
    {"name": "Central African Republic", "code": "CF", "flag": "🇨🇫"},
    {"name": "Canada", "code": "CA", "flag": "🇨🇦"},
    {"name": "Cocos (Keeling) Islands", "code": "CC", "flag": "🇨🇨"},
    {"name": "Switzerland", "code": "CH", "flag": "🇨🇭"},
    {"name": "Chile", "code": "CL", "flag": "🇨🇱"},
    {"name": "China", "code": "CN", "flag": "🇨🇳"},
    {"name": "Côte d'Ivoire", "code": "CI", "flag": "🇨🇮"},
    {"name": "Cameroon", "code": "CM", "flag": "🇨🇲"},
    {"name": "Congo, The Democratic Republic of the", "code": "CD", "flag": "🇨🇩"},
    {"name": "Congo", "code": "CG", "flag": "🇨🇬"},
    {"name": "Cook Islands", "code": "CK", "flag": "🇨🇰"},
    {"name": "Colombia", "code": "CO", "flag": "🇨🇴"},
    {"name": "Comoros", "code": "KM", "flag": "🇰🇲"},
    {"name": "Cabo Verde", "code": "CV", "flag": "🇨🇻"},
    {"name": "Costa Rica", "code": "CR", "flag": "🇨🇷"},
    {"name": "Cuba", "code": "CU", "flag": "🇨🇺"},
    {"name": "Curaçao", "code": "CW", "flag": "🇨🇼"},
    {"name": "Christmas Island", "code": "CX", "flag": "🇨🇽"},
    {"name": "Cayman Islands", "code": "KY", "flag": "🇰🇾"},
    {"name": "Cyprus", "code": "CY", "flag": "🇨🇾"},
    {"name": "Czechia", "code": "CZ", "flag": "🇨🇿"},
    {"name": "Germany", "code": "DE", "flag": "🇩🇪"},
    {"name": "Djibouti", "code": "DJ", "flag": "🇩🇯"},
    {"name": "Dominica", "code": "DM", "flag": "🇩🇲"},
    {"name": "Denmark", "code": "DK", "flag": "🇩🇰"},
    {"name": "Dominican Republic", "code": "DO", "flag": "🇩🇴"},
    {"name": "Algeria", "code": "DZ", "flag": "🇩🇿"},
    {"name": "Ecuador", "code": "EC", "flag": "🇪🇨"},
    {"name": "Egypt", "code": "EG", "flag": "🇪🇬"},
    {"name": "Eritrea", "code": "ER", "flag": "🇪🇷"},
    {"name": "Western Sahara", "code": "EH", "flag": "🇪🇭"},
    {"name": "Spain", "code": "ES", "flag": "🇪🇸"},
    {"name": "Estonia", "code": "EE", "flag": "🇪🇪"},
    {"name": "Ethiopia", "code": "ET", "flag": "🇪🇹"},
    {"name": "Finland", "code": "FI", "flag": "🇫🇮"},
    {"name": "Fiji", "code": "FJ", "flag": "🇫🇯"},
    {"name": "Falkland Islands (Malvinas)", "code": "FK", "flag": "🇫🇰"},
    {"name": "France", "code": "FR", "flag": "🇫🇷"},
    {"name": "Faroe Islands", "code": "FO", "flag": "🇫🇴"},
    {"name": "Micronesia, Federated States of", "code": "FM", "flag": "🇫🇲"},
    {"name": "Gabon", "code": "GA", "flag": "🇬🇦"},
    {"name": "United Kingdom", "code": "GB", "flag": "🇬🇧"},
    {"name": "Georgia", "code": "GE", "flag": "🇬🇪"},
    {"name": "Guernsey", "code": "GG", "flag": "🇬🇬"},
    {"name": "Ghana", "code": "GH", "flag": "🇬🇭"},
    {"name": "Gibraltar", "code": "GI", "flag": "🇬🇮"},
    {"name": "Guinea", "code": "GN", "flag": "🇬🇳"},
    {"name": "Guadeloupe", "code": "GP", "flag": "🇬🇵"},
    {"name": "Gambia", "code": "GM", "flag": "🇬🇲"},
    {"name": "Guinea-Bissau", "code": "GW", "flag": "🇬🇼"},
    {"name": "Equatorial Guinea", "code": "GQ", "flag": "🇬🇶"},
    {"name": "Greece", "code": "GR", "flag": "🇬🇷"},
    {"name": "Grenada", "code": "GD", "flag": "🇬🇩"},
    {"name": "Greenland", "code": "GL", "flag": "🇬🇱"},
    {"name": "Guatemala", "code": "GT", "flag": "🇬🇹"},
    {"name": "French Guiana", "code": "GF", "flag": "🇬🇫"},
    {"name": "Guam", "code": "GU", "flag": "🇬🇺"},
    {"name": "Guyana", "code": "GY", "flag": "🇬🇾"},
    {"name": "Hong Kong", "code": "HK", "flag": "🇭🇰"},
    {"name": "Heard Island and McDonald Islands", "code": "HM", "flag": "🇭🇲"},
    {"name": "Honduras", "code": "HN", "flag": "🇭🇳"},
    {"name": "Croatia", "code": "HR", "flag": "🇭🇷"},
    {"name": "Haiti", "code": "HT", "flag": "🇭🇹"},
    {"name": "Hungary", "code": "HU", "flag": "🇭🇺"},
    {"name": "Indonesia", "code": "ID", "flag": "🇮🇩"},
    {"name": "Isle of Man", "code": "IM", "flag": "🇮🇲"},
    {"name": "India", "code": "IN", "flag": "🇮🇳"},
    {"name": "British Indian Ocean Territory", "code": "IO", "flag": "🇮🇴"},
    {"name": "Ireland", "code": "IE", "flag": "🇮🇪"},
    {"name": "Iran, Islamic Republic of", "code": "IR", "flag": "🇮🇷"},
    {"name": "Iraq", "code": "IQ", "flag": "🇮🇶"},
    {"name": "Iceland", "code": "IS", "flag": "🇮🇸"},
    {"name": "Israel", "code": "IL", "flag": "🇮🇱"},
    {"name": "Italy", "code": "IT", "flag": "🇮🇹"},
    {"name": "Jamaica", "code": "JM", "flag": "🇯🇲"},
    {"name": "Jersey", "code": "JE", "flag": "🇯🇪"},
    {"name": "Jordan", "code": "JO", "flag": "🇯🇴"},
    {"name": "Japan", "code": "JP", "flag": "🇯🇵"},
    {"name": "Kazakhstan", "code": "KZ", "flag": "🇰🇿"},
    {"name": "Kenya", "code": "KE", "flag": "🇰🇪"},
    {"name": "Kyrgyzstan", "code": "KG", "flag": "🇰🇬"},
    {"name": "Cambodia", "code": "KH", "flag": "🇰🇭"},
    {"name": "Kiribati", "code": "KI", "flag": "🇰🇮"},
    {"name": "Saint Kitts and Nevis", "code": "KN", "flag": "🇰🇳"},
    {"name": "Korea, Republic of", "code": "KR", "flag": "🇰🇷"},
    {"name": "Kuwait", "code": "KW", "flag": "🇰🇼"},
    {"name": "Lao People's Democratic Republic", "code": "LA", "flag": "🇱🇦"},
    {"name": "Lebanon", "code": "LB", "flag": "🇱🇧"},
    {"name": "Liberia", "code": "LR", "flag": "🇱🇷"},
    {"name": "Libya", "code": "LY", "flag": "🇱🇾"},
    {"name": "Saint Lucia", "code": "LC", "flag": "🇱🇨"},
    {"name": "Liechtenstein", "code": "LI", "flag": "🇱🇮"},
    {"name": "Sri Lanka", "code": "LK", "flag": "🇱🇰"},
    {"name": "Lesotho", "code": "LS", "flag": "🇱🇸"},
    {"name": "Lithuania", "code": "LT", "flag": "🇱🇹"},
    {"name": "Luxembourg", "code": "LU", "flag": "🇱🇺"},
    {"name": "Latvia", "code": "LV", "flag": "🇱🇻"},
    {"name": "Macao", "code": "MO", "flag": "🇲🇴"},
    {"name": "Saint Martin (French part)", "code": "MF", "flag": "🇲🇫"},
    {"name": "Morocco", "code": "MA", "flag": "🇲🇦"},
    {"name": "Monaco", "code": "MC", "flag": "🇲🇨"},
    {"name": "Moldova, Republic of", "code": "MD", "flag": "🇲🇩"},
    {"name": "Madagascar", "code": "MG", "flag": "🇲🇬"},
    {"name": "Maldives", "code": "MV", "flag": "🇲🇻"},
    {"name": "Mexico", "code": "MX", "flag": "🇲🇽"},
    {"name": "Marshall Islands", "code": "MH", "flag": "🇲🇭"},
    {"name": "North Macedonia", "code": "MK", "flag": "🇲🇰"},
    {"name": "Mali", "code": "ML", "flag": "🇲🇱"},
    {"name": "Malta", "code": "MT", "flag": "🇲🇹"},
    {"name": "Myanmar", "code": "MM", "flag": "🇲🇲"},
    {"name": "Montenegro", "code": "ME", "flag": "🇲🇪"},
    {"name": "Mongolia", "code": "MN", "flag": "🇲🇳"},
    {"name": "Northern Mariana Islands", "code": "MP", "flag": "🇲🇵"},
    {"name": "Mozambique", "code": "MZ", "flag": "🇲🇿"},
    {"name": "Mauritania", "code": "MR", "flag": "🇲🇷"},
    {"name": "Montserrat", "code": "MS", "flag": "🇲🇸"},
    {"name": "Martinique", "code": "MQ", "flag": "🇲🇶"},
    {"name": "Mauritius", "code": "MU", "flag": "🇲🇺"},
    {"name": "Malawi", "code": "MW", "flag": "🇲🇼"},
    {"name": "Malaysia", "code": "MY", "flag": "🇲🇾"},
    {"name": "Mayotte", "code": "YT", "flag": "🇾🇹"},
    {"name": "Namibia", "code": "NA", "flag": "🇳🇦"},
    {"name": "New Caledonia", "code": "NC", "flag": "🇳🇨"},
    {"name": "Niger", "code": "NE", "flag": "🇳🇪"},
    {"name": "Norfolk Island", "code": "NF", "flag": "🇳🇫"},
    {"name": "Nigeria", "code": "NG", "flag": "🇳🇬"},
    {"name": "Nicaragua", "code": "NI", "flag": "🇳🇮"},
    {"name": "Niue", "code": "NU", "flag": "🇳🇺"},
    {"name": "Netherlands", "code": "NL", "flag": "🇳🇱"},
    {"name": "Norway", "code": "NO", "flag": "🇳🇴"},
    {"name": "Nepal", "code": "NP", "flag": "🇳🇵"},
    {"name": "Nauru", "code": "NR", "flag": "🇳🇷"},
    {"name": "New Zealand", "code": "NZ", "flag": "🇳🇿"},
    {"name": "Oman", "code": "OM", "flag": "🇴🇲"},
    {"name": "Pakistan", "code": "PK", "flag": "🇵🇰"},
    {"name": "Panama", "code": "PA", "flag": "🇵🇦"},
    {"name": "Pitcairn", "code": "PN", "flag": "🇵🇳"},
    {"name": "Peru", "code": "PE", "flag": "🇵🇪"},
    {"name": "Philippines", "code": "PH", "flag": "🇵🇭"},
    {"name": "Palau", "code": "PW", "flag": "🇵🇼"},
    {"name": "Papua New Guinea", "code": "PG", "flag": "🇵🇬"},
    {"name": "Poland", "code": "PL", "flag": "🇵🇱"},
    {"name": "Puerto Rico", "code": "PR", "flag": "🇵🇷"},
    {"name": "Korea, Democratic People's Republic of", "code": "KP", "flag": "🇰🇵"},
    {"name": "Portugal", "code": "PT", "flag": "🇵🇹"},
    {"name": "Paraguay", "code": "PY", "flag": "🇵🇾"},
    {"name": "Palestine, State of", "code": "PS", "flag": "🇵🇸"},
    {"name": "French Polynesia", "code": "PF", "flag": "🇵🇫"},
    {"name": "Qatar", "code": "QA", "flag": "🇶🇦"},
    {"name": "Réunion", "code": "RE", "flag": "🇷🇪"},
    {"name": "Romania", "code": "RO", "flag": "🇷🇴"},
    {"name": "Russian Federation", "code": "RU", "flag": "🇷🇺"},
    {"name": "Rwanda", "code": "RW", "flag": "🇷🇼"},
    {"name": "Saudi Arabia", "code": "SA", "flag": "🇸🇦"},
    {"name": "Sudan", "code": "SD", "flag": "🇸🇩"},
    {"name": "Senegal", "code": "SN", "flag": "🇸🇳"},
    {"name": "Singapore", "code": "SG", "flag": "🇸🇬"},
    {"name": "South Georgia and the South Sandwich Islands", "code": "GS", "flag": "🇬🇸"},
    {"name": "Saint Helena, Ascension and Tristan da Cunha", "code": "SH", "flag": "🇸🇭"},
    {"name": "Svalbard and Jan Mayen", "code": "SJ", "flag": "🇸🇯"},
    {"name": "Solomon Islands", "code": "SB", "flag": "🇸🇧"},
    {"name": "Sierra Leone", "code": "SL", "flag": "🇸🇱"},
    {"name": "El Salvador", "code": "SV", "flag": "🇸🇻"},
    {"name": "San Marino", "code": "SM", "flag": "🇸🇲"},
    {"name": "Somalia", "code": "SO", "flag": "🇸🇴"},
    {"name": "Saint Pierre and Miquelon", "code": "PM", "flag": "🇵🇲"},
    {"name": "Serbia", "code": "RS", "flag": "🇷🇸"},
    {"name": "South Sudan", "code": "SS", "flag": "🇸🇸"},
    {"name": "Sao Tome and Principe", "code": "ST", "flag": "🇸🇹"},
    {"name": "Suriname", "code": "SR", "flag": "🇸🇷"},
    {"name": "Slovakia", "code": "SK", "flag": "🇸🇰"},
    {"name": "Slovenia", "code": "SI", "flag": "🇸🇮"},
    {"name": "Sweden", "code": "SE", "flag": "🇸🇪"},
    {"name": "Eswatini", "code": "SZ", "flag": "🇸🇿"},
    {"name": "Sint Maarten (Dutch part)", "code": "SX", "flag": "🇸🇽"},
    {"name": "Seychelles", "code": "SC", "flag": "🇸🇨"},
    {"name": "Syrian Arab Republic", "code": "SY", "flag": "🇸🇾"},
    {"name": "Turks and Caicos Islands", "code": "TC", "flag": "🇹🇨"},
    {"name": "Chad", "code": "TD", "flag": "🇹🇩"},
    {"name": "Togo", "code": "TG", "flag": "🇹🇬"},
    {"name": "Thailand", "code": "TH", "flag": "🇹🇭"},
    {"name": "Tajikistan", "code": "TJ", "flag": "🇹🇯"},
    {"name": "Tokelau", "code": "TK", "flag": "🇹🇰"},
    {"name": "Turkmenistan", "code": "TM", "flag": "🇹🇲"},
    {"name": "Timor-Leste", "code": "TL", "flag": "🇹🇱"},
    {"name": "Tonga", "code": "TO", "flag": "🇹🇴"},
    {"name": "Trinidad and Tobago", "code": "TT", "flag": "🇹🇹"},
    {"name": "Tunisia", "code": "TN", "flag": "🇹🇳"},
    {"name": "Turkey", "code": "TR", "flag": "🇹🇷"},
    {"name": "Tuvalu", "code": "TV", "flag": "🇹🇻"},
    {"name": "Taiwan, Province of China", "code": "TW", "flag": "🇹🇼"},
    {"name": "Tanzania, United Republic of", "code": "TZ", "flag": "🇹🇿"},
    {"name": "Uganda", "code": "UG", "flag": "🇺🇬"},
    {"name": "Ukraine", "code": "UA", "flag": "🇺🇦"},
    {"name": "United States Minor Outlying Islands", "code": "UM", "flag": "🇺🇲"},
    {"name": "Uruguay", "code": "UY", "flag": "🇺🇾"},
    {"name": "United States", "code": "US", "flag": "🇺🇸"},
    {"name": "Uzbekistan", "code": "UZ", "flag": "🇺🇿"},
    {"name": "Holy See (Vatican City State)", "code": "VA", "flag": "🇻🇦"},
    {"name": "Saint Vincent and the Grenadines", "code": "VC", "flag": "🇻🇨"},
    {"name": "Venezuela, Bolivarian Republic of", "code": "VE", "flag": "🇻🇪"},
    {"name": "Virgin Islands, British", "code": "VG", "flag": "🇻🇬"},
    {"name": "Virgin Islands, U.S.", "code": "VI", "flag": "🇻🇮"},
    {"name": "Viet Nam", "code": "VN", "flag": "🇻🇳"},
    {"name": "Vanuatu", "code": "VU", "flag": "🇻🇺"},
    {"name": "Wallis and Futuna", "code": "WF", "flag": "🇼🇫"},
    {"name": "Samoa", "code": "WS", "flag": "🇼🇸"},
    {"name": "Yemen", "code": "YE", "flag": "🇾🇪"},
    {"name": "South Africa", "code": "ZA", "flag": "🇿🇦"},
    {"name": "Zambia", "code": "ZM", "flag": "🇿🇲"},
    {"name": "Zimbabwe", "code": "ZW", "flag": "🇿🇼"},
]