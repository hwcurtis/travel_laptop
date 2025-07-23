import pandas as pd

# Data: COVID-19 case counts by U.S. state in 2025
data = {
    "State": [
        "California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio", "Georgia",
        "North Carolina", "Michigan", "Arizona", "Tennessee", "Indiana", "Massachusetts", "Wisconsin",
        "Washington", "Virginia", "Missouri", "Minnesota", "South Carolina", "Alabama", "Colorado",
        "Kentucky", "Louisiana", "Oklahoma", "Oregon", "Connecticut", "Iowa", "Mississippi", "Arkansas",
        "Nevada", "Utah", "Kansas", "New Mexico", "Nebraska", "West Virginia", "Idaho", "Hawaii", "Maine",
        "New Hampshire", "Rhode Island", "Montana", "Delaware", "South Dakota", "North Dakota", "Alaska",
        "Vermont", "District of Columbia", "Wyoming"
    ],
    "Total_Confirmed_Cases": [
        11307308, 8616462, 7632104, 6799196, 4194265, 3688494, 3498129, 2340689, 3543280, 3147894,
        2494926, 2648968, 2200528, 2413794, 2100673, 2357861, 2320820, 1878727, 1920830, 1956208,
        1660786, 1774970, 1797726, 1623028, 1337445, 1925317, 982973, 1000591, 978581, 977662, 1220874,
        1079044, 979699, 697320, 660709, 650456, 554244, 413397, 360161, 387203, 558267, 331909, 334466,
        327412, 313647, 287135, 160744, 169149, 186136
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("covid_case_counts_by_state_2025.csv", index=False)
