# Iterate through the json list, see if contains dependancies, if not then move on

import json
import csv

# Contains whitespaces after commas, which will stay after splitting


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

final_cut_pro_bro = []

with open('node-postgres/test.json') as f:
    data = json.loads(f.read())

resolves = json_extract(data, 'resolved')

with open('node-postgres/testWithLicence.csv') as c:
    licensedata = csv.reader(c, delimiter=',')
   
    for x in licensedata:
        lst = x[0].rsplit('@',1)

        if len(lst) > 1:
            
            resolve = ''
        
            for text in resolves:

                if lst[0] in text:
                    resolve = text

            final_cut_pro_bro.append([lst[0],lst[1],x[1],x[2],resolve])
        

header = ['name', 'version','licenses', 'repository', 'url_to_source']

with open('final_cut_pro.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(final_cut_pro_bro)

# # print(len(json_extract(data, 'from')))
# # print(len(json_extract(data, 'version')))
# # print(len(json_extract(licensedata, 'repository')))
# # print(len(json_extract(licensedata, 'licenses')))
# # print(len(json_extract(data, 'resolved')))

# # print(json_extract(data, 'from')[0])

# emptydata = []
# emptylicencedata = []

# count = 0
# # # for x in range(len(json_extract(data, 'version'))):
# #     # creating temp array to sort the data
# #     sortedata = []

# #     # sortedata.append(json_extract(data, 'from')[count])
# #     sortedata.append(json_extract(data, 'version')[count])
# #     sortedata.append(json_extract(data, 'resolved')[count])

# #     # # appending the sorted data to the emptyarr
# #     emptydata.append(sortedata)
# #     count += 1

# count = 0

# # for x in range(len(json_extract(data, 'version'))):
# #     # creating temp array to sort the data
# #     sortedlicensedata = []

# #     sortedlicensedata.append(json_extract(licensedata, 'repository')[count])
# #     sortedlicensedata.append(json_extract(licensedata, 'licenses')[count])

# #     # # appending the sorted data to the emptyarr
# #     emptylicencedata.append(sortedlicensedata)
# #     count += 1

# # print(emptydata[0])
# # print(emptylicencedata[0])



# # Why have we got 1230 repositories??