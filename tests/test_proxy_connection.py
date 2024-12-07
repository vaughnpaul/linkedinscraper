import requests
import json

url2 = 'https://ipv4.icanhazip.com'
proxy = 'http://_country-us@geo.iproyal.com:12321'
proxy_auth = 'BaKE2JPMknaa2FFP:7VI6GJUJHYvMN710'
proxies = {
    'http': f'http://{proxy_auth}@{proxy}',
    'https': f'http://{proxy_auth}@{proxy}'
}

print("proxies: ------------------------------------\n")
print(proxies)

def test_proxy_connection():

  url1 = "https://api.ipify.org?format=json"

  # Load proxy configuration from config.json
  with open('config.json') as config_file:
    config = json.load(config_file)
   # proxy = config['proxies']
    header = config['headers']

  # Make the first API call without using the proxy
  try:
    response1 = requests.get(url1)
    response1.raise_for_status()
    ip1 = response1.json()['ip']
    # Print ip addresses
    print(f"Personal IP1: {ip1}")

  except requests.exceptions.RequestException as e:
    assert False, f"MSG1: Proxy connection test failed: Failed to make the first API call without proxy. Reason: {str(e)}"

  # Make the second API call using the proxy
  try:
    response2 = requests.get(url2, proxies=proxies)
    response2.raise_for_status()
    ip2 = response2.json()['ip']
    print(response2.text)
    print(proxies)
    print(headers)
    print(f"Personal IP2: {ip2}")
  except requests.exceptions.RequestException as e:
    assert False, f"MSG2: Proxy connection test failed: Failed to make the second API call with proxy. Reason: {str(e)}"

  # Verify that the two IP addresses are different
  assert ip1 != ip2, "MSG3: Proxy connection test failed: IP addresses are the same"

  # Print the IP addresses for verification
  print(f"Personal IP: {ip1}")
  print(f"Proxy IP: {ip2}")
  print("Proxy connection was successfully used for request.")


if __name__ == '__main__':
  test_proxy_connection()
