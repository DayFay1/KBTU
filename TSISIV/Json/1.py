import json

# Load the JSON data from a local file
with open('sample_data.json','r') as file:
    data = json.load(file)

# Extract the relevant information from the data
interfaces = data['imdata']
table_data = []
for interface in interfaces:
    dn = interface['fvCEp']['attributes']['dn']
    descr = interface['fvCEp']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')

    # Append the extracted information to the table data
    table_data.append([dn, descr, speed, mtu])

# Print the table header
print('Interface Status')
print('=' * 90)
print('{:<50} {:<25} {:<8} {:<6}'.format('DN', 'Description', 'Speed', 'MTU'))
print('-' * 90)

# Print the table rows
for row in table_data:
    print('{:<50} {:<25} {:<8} {:<6}'.format(*row))

