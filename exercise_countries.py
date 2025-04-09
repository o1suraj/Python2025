countries = [
    {"name":"Nepal", "population":"124_000_000"},
    {"name":"japan", "population":"29_000_000"},
    {"name":"India", "population":"1_124_000_000"},
    {"name":"Srilanka", "population":"22_000_000"},
    {"name":"France", "population": "68_000_000"},
]
biggest_country = countries[0]

for country in countries:
    print(f"Name/ {country["name"]} - Population: {country["population"]:,}")
    if country["population"] < biggest_country["population"]:
       biggest_country = country





print(f"The biggest country is {}")       
