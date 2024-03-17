import csv

def write_holiday_cities(first_letter):

    with open('travel-notes.csv', 'r', newline='') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',')

        data = [row for row in csv_data if row['Name'].startswith(first_letter)]

        visited_cities = [row['Visited'] for row in data]
        desired_cities = [row['Desired'] for row in data]

        cities_visited = set()
        cities_desired = set()
        cities_not_visited = set()

        for cities in visited_cities:
            cities_visited.update(cities.split(','))

        for cities in desired_cities:
            cities_desired.update(cities.split(','))

        cities_not_visited = cities_desired - cities_visited

        first_city_to_visit = next(iter(cities_not_visited), None)

        with open('holiday.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Cities Visited', 'Cities Desired', 'Cities Not Visited', 'First City to Visit'])
            writer.writerow([', '.join(cities_visited), ', '.join(cities_desired), ', '.join(cities_not_visited),
                             first_city_to_visit])


write_holiday_cities('L')