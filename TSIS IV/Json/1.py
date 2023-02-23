import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DN".ljust(50) + "Description".ljust(25) + "Speed".ljust(10) + "MTU")
print("-" * 80)

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print(dn.ljust(50) + description.ljust(25) + speed.ljust(10) + mtu)

