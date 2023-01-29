import geojson
import parse as p

def create_map(data_file):
    # Define type of GeoJSON we're creating
    geo_map = {'type': "FeatureCollection"}
    # Define empty list to collect each point to graph
    item_list = []
    # Iterate over our data to create GeoJSON document.
    # We're using enumerate() so we get the line, as well
    # the index, which is the line number.
    for index, ele in enumerate(data_file):
        # Skip any zero coordinates as this will throw off
        # our map.
        if ele['X'] == '0' or ele['Y'] == '0':
            continue
        # Setup a new dictionary for each iteration.
        data = {}
        # Assign line items to appropriate GeoJSON fields.
        data['type'] = 'Feature'
        data['id'] = str(index) #!!!with int type, properties can't show in github gist when click
        data['properties'] = {
            'title': ele['Category'],
            'description': ele['Descript'],
            'date': ele['Date']
        }
        data['geometry'] = {
            'type': 'Point',
            'coordinates': (ele['X'], ele['Y'])
        }
        # Add data dictionary to our item_list
        item_list.append(data)
    # For each point in our item_list, we add the point to our
    # dictionary.  setdefault creates a key called 'features' that
    # has a value type of an empty list.  With each iteration, we
    # are appending our point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)
        #Python dictionary method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
        
    # Now that all data is parsed in GeoJSON write to a file so we
    # can upload it to gist.github.com
    with open('file_sf.geojson', 'w') as f:
        geojson.dump(geo_map, f, indent=6)
        
def main():
    data = p.parse(p.MY_FILE, ',')
    return create_map(data)
    
if __name__ == "__main__":
    main()