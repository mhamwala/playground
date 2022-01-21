# Iterate through the json list, see if contains dependancies, if not then move on

import json
import csv

with open('ls-withLicense1.json') as c:
    licensedata = json.loads(c.read())

with open('ls-deps.json') as f:
    data = json.loads(f.read())

listofdependencies = []

"""Extract nested values from a JSON tree."""

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

print(len(json_extract(data, 'from')))
print(len(json_extract(data, 'version')))
print(len(json_extract(licensedata, 'repository')))
print(len(json_extract(licensedata, 'licenses')))
print(len(json_extract(data, 'resolved')))

fromarr = json_extract(data, 'from')
versionarr = json_extract(data, 'version')
resolvedarr = json_extract(data, 'resolved')

emptyarr = []

# print(json_extract(data, 'from')[0])
count = 0

for x in range(len(json_extract(data, 'from'))):
    # creating temp array to sort the data
    sortedarr = []
    sortedarr.append(json_extract(data, 'from')[count])
    sortedarr.append(json_extract(data, 'version')[count])
    try:
        sortedarr.append(json_extract(licensedata, 'repository')[count])
    except IndexError:
        # print('sorry, no 5') 
        sortedarr.append(' ') 
    try:
        sortedarr.append(json_extract(licensedata, 'licenses')[count])
    except IndexError:
        # print('sorry, no 5') 
        sortedarr.append(' ')
    # if(json_extract(licensedata, 'repository')[count]):
    #     sortedarr.append(json_extract(licensedata, 'repository')[count])
    # else:
    #     print("appending empty string")
    #     sortedarr.append(' ')
    # if(json_extract(licensedata, 'licenses')[count]):
    #     sortedarr.append(json_extract(licensedata, 'licenses')[count])
    # else:
    #     print("appending empty string")
    #     sortedarr.append(' ')
    sortedarr.append(json_extract(data, 'resolved')[count])
    # appending the sorted data to the emptyarr
    emptyarr.append(sortedarr)
    count += 1

header = ['name', 'version', 'repository', 'licenses', 'url_to_source']

with open('rasldsepsd.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(emptyarr)

# Why have we got 1230 repositories??