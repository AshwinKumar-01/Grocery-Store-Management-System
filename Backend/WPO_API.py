import requests
from requests.auth import HTTPBasicAuth

url = "https://sus-testing.nokiaosdp.dyn.nesc.nokia.net/api/v1/nm_son_data/nokia.nm.son.demands/call/_get_nm_son_data/"
username = "nm_son_data"
password = "e05e3151-2f14-42de-998c-fef74f95887b"
response = requests.get(url,auth=HTTPBasicAuth(username,password))
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}:{response.text}")