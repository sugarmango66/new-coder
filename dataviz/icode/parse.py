import csv
import json
MY_FILE = '../data/sample_sfpd_incident_all.csv'
save_file = '../data/save_after_parse.json'

def parse(raw_file, delimiter):
    '''turn csv file to json-like data'''
    #open file
    opened_file = open(raw_file)
    #read file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    #build a data structure to return json-like data
    parsed_data = []
    fields = next(csv_data) #py3 use next(iterator)
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
        
    #close file
    opened_file.close()
    return parsed_data

def save_json_file(data, filename):
    '''save list of dicts in json file'''
    with open(filename, 'w') as f:
        json.dump(data, f, indent=6)

def main():
    new_data = parse(MY_FILE, ',')
    # print(new_data)
    save_json_file(new_data, save_file)
    
if __name__ == '__main__':
    main()