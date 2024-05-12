import read_csv
import charts



data_path = './app/data.csv'
raw_data = read_csv.read_csv(data_path)
selected_column = 'World Population Percentage'

raw_data = list(filter(lambda item: item['Continent'] == 'South America', raw_data))

labels = [x['Country/Territory'] for x in raw_data]
values = [float(x[selected_column]) for x in raw_data]

charts.generate_pie_chart(labels, values)
