import json

# Load data from file
with open('sample-data.json') as f:
    data = json.load(f)

# Extract the relevant data from the JSON object
interfaces = data['imdata']

# Print the header
print('{:<50}{:<22}{:<8}{}'.format('DN', 'Description', 'Speed', 'MTU'))
print('-' * 70)

# Print the interface status for each interface
for interface in interfaces:
    dn = interface['infraAccPortP']['attributes']['dn']
    descr = interface['infraAccPortP']['attributes']['descr']
    speed = interface['infraAccPortP']['attributes']['speed']
    mtu = interface['infraAccPortP']['attributes']['mtu']
    print('{:<50}{:<22}{:<8}{}'.format(dn, descr, speed, mtu))
