import src.scrapers.regions as regions

# Sort Delhi's hospital by vacant beds

hospital_data = regions.scrape['delhi']()['data']

hospital_data.sort(key =lambda hospital: hospital['Vacant'], reverse= True)

for hospital in hospital_data:
    print(hospital['Hospital'])
    print("Vacant:",hospital['Vacant'])
    print("Occupied:",hospital['Occupied'])
    print("Total:",hospital['Total'])
    print("Last update:",hospital['Update'])
    print()
