import requests
import time

api_path = "https://sandboxdnac2.cisco.com/dna"
auth = ("devnetuser", "Cisco123!")

def get_token():
    headers = {"Content-Type": "application/json"}
    auth_resp = requests.post(f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers)

    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return(token)

def get_devices(token):
    headers={"X-Auth-Token": token, "Content-Type": "application/json"}
    devices_list = requests.get(f"{api_path}/intent/api/v1/network-device", headers=headers)
    dev_list_json = devices_list.json()
    return(dev_list_json)

def display_names(device_list):
    for item in device_list:
        print (f"O IP do device é {item['managementIpAddress']} e o ID é {item['id']}")

def add_device(token):
    headers={"X-Auth-Token": token, "Content-Type": "application/json"}

    new_device_dict = {
        "ipAddress": ["192.168.253.23"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }

    add_resp = requests.post(f"{api_path}/intent/api/v1/network-device", json=new_device_dict, headers=headers)

    if add_resp.ok:
        print("nao vale a pena :( ")
    else:
        print(f"Device addition failed with code {add_resp.status_code}")
        print(f"Failure body: {add_resp.text}")

def main():
    """
    e aqui começa o codigo
    """
    token = get_token()
    #devices = get_devices(token)
    #display_names(devices['response'])
    add_device(token)

if __name__ == "__main__":
    main()