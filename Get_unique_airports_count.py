import re
import json
import sys


def read_csv(file_name='airlines2.csv'):
    # Function to read CSV file, takes in the file path as input. Returns list of lines. 
    try:
        results = []
        with open(file_name,'r') as file:
            text = file.readlines()
            for lines in text:
                line_data = lines.split('\n')[0]
                data = [line for line in re.split("( |[\\\"'].*[\\\"'])", line_data) if line_data.strip()]
                if data:
                    results.append(data)
        return results
    except FileNotFoundError:
        print("Wrong file or file path")
        sys.exit(1)
    

def get_unique_airports(airport_data):
    # Function to get unique airports from the file. Takes in the airport list data as input. Returns dictionary of unique airport. 
    unique_airports = {}
    for airport in airport_data[1:]:
        airport_name=airport[1].replace('"','')
        if airport_name in unique_airports.keys():
            unique_airports[airport_name] +=1
        else:
            unique_airports[airport_name] =1
    return unique_airports


def get_max_min_mentions(unique_airports):
    # Function to get name of minimum and maximum mentioned airport. Takes in unique_airports dictionary as input. Returns maximum and minumum value
    max_val = []
    min_val = []
    for k,v in unique_airports.items():
        if max_val:
            if v > max_val[1]:
                max_val.clear()
                max_val.extend([k,v])
        if not max_val:
            max_val.extend([k,v])
        if min_val:
            if v < min_val[1]:
                min_val.clear()
                min_val.extend([k,v])
        if not min_val:
            min_val.extend([k,v])
    return max_val,min_val

def main():
    # Driver Function 
    csv_data = read_csv()
    unique_airports =  get_unique_airports(csv_data)
    max_val,min_val = get_max_min_mentions(unique_airports)
    print(json.dumps(unique_airports, indent=4))
    print(f'\nMaximum mention of airport --- Name: "{max_val[0]}", Count: {max_val[1]}')
    print(f'\nMinimum mention of airport --- Name: "{min_val[0]}", Count: {min_val[1]}')


if __name__ == '__main__':
    main()
