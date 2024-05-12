import read_csv
import charts


data_path = './app/data.csv'
raw_data = read_csv.read_csv(data_path)
country = 'Argentina'


for country_data in raw_data:
    if country in country_data['Country/Territory']:
        # filtered_data = list(filter(lambda item: item[0].isdigit(), list(country_data.keys())))
        filtered_data = dict(filter(lambda item: item[0][0].isdigit(), country_data.items()))
        years_list = list(map(lambda x: x.replace(' Population', ''),list(filtered_data.keys())))
        population_list = list(map(lambda x: int(x), list(filtered_data.values())))

print(filtered_data)
print('')
print(years_list)
print('')
print(population_list)

charts.generate_bar_chart(years_list, population_list)
    