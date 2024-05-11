import read_csv


data_path = './app/data.csv'
raw_data = read_csv.read_csv(data_path)
country = 'Argentina'


for country_data in raw_data:
    if country in country_data['Country/Territory']:
        filtered_data = list(filter(lambda item: item[0].isdigit(), list(country_data.keys())))

print(filtered_data)
    