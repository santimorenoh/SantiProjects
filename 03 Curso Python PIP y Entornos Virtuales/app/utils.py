def get_population(country):
    
    filtered_data = list(filter(lambda item: item[0][0].isdigit(), country.items()))
    
    keys = [i[0].replace(' Population', '') for i in filtered_data]
    values = [int(i[1]) for i in filtered_data]
    
    return keys, values

def population_by_country(data, country):

    result = list(filter(lambda item: item['Country/Territory'] == country, data))

    return result

