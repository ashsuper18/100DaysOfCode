travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# to be added to the travel_log. 👇


def add_new_country(country_visited, total_visits, cities_visited):
    travel_log.append({
        "country": country_visited,
        "visits": total_visits,
        "cities": cities_visited
    })
    print(travel_log)


add_new_country("India", 2, ["abc", "affa", "fadf"])
