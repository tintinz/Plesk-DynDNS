import requests
import sys
host_server = sys.argv[1]
domain = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
oldipdomain = "oldip." + domain + "."

headers = {
    'accept': 'application/json',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

x = requests.get("https://icanhazip.com/")
ip_addr = x.text

def getOldIP(subdomain):
    for i in subdomain:
        if i['host'] == oldipdomain:
            return i['value']
    print("Missing subdomain oldip.")

def updateOldIP(subdomain):
    for i in subdomain:
        if i['host'] == oldipdomain:
            setNewIP(i['id'], i['type'], i['host'])


def getIDs(subdomains, oldIP):

    needupdate = sum([item['value'] == oldIP for item in subdomains])

    while needupdate >= 0:

        print(f"right now there is {needupdate} domain outdated")
        for i in subdomains:


            if i['value'] == oldIP:
                setNewIP(i['id'], i['type'], i['host'])
                needupdate -= 1


            print(f"right now there is {needupdate} domain outdated")
def setNewIP(id, type, host):
    json_data = {
        'id': id,
        'type': type,
        'host': host,
        'value': ip_addr
        }
    response2 = requests.put(f'https://{host_server}/api/v2/dns/records/{id}', headers=headers, json=json_data, verify=False, auth=(user, password))
    #print(response2.text)


response = requests.get(f'https://{host_server}/api/v2/dns/records?domain={domain}', verify=False,
                        auth=(user, password))

domain_data = response.json()
oldIP = getOldIP(domain_data)

if ip_addr.strip() != oldIP:
    getIDs(domain_data, oldIP)
    updateOldIP(domain_data)

else:
    print('no need to updte')






