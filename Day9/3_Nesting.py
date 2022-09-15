# Nesting putting another dictonaries or list inside dictonaries. example:
random_dict = {"key1": ["list1", "list2", "list3"],
               "key2": {"anotherDict"}}

# Nesting
capitals = {
    "India": "Rajasthan",
    "USA": "Silicon"
}

# Nesting dictionary inside dictionary
travel_log = {
    "India": {
        "cities_visited": ["Punjab", "Rajasthan", "Uttar-Pradesh"],
        "total_visit": 12},
    "USA": {
        "cities_visited": "None",
        "total_visit": 0,
    }
}


# Nesting Dictionaries in Lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
