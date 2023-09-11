'''
This is a Python client for the crt.sh website to retrieve subdomains information.
@Author: Omar Santos @santosomar
Version: 1.0
'''

import requests
import argparse
import json

class CrtshClient:
    """A Python client for the crt.sh website to retrieve subdomains information."""
    
    def __init__(self):
        self.base_url = "https://crt.sh/?q={}&output=json"
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        
    def build_url(self, domain, wildcard=True, expired=True):
        """Builds the request URL based on the given parameters."""
        if not expired:
            self.base_url += "&exclude=expired"
        if wildcard and "%" not in domain:
            domain = f"%.{domain}"
        return self.base_url.format(domain)
    
    def search(self, domain, wildcard=True, expired=True):
        """
        Search crt.sh for the given domain and returns a list of certificate data.
        
        :param domain: Domain to search for.
        :param wildcard: Whether to prepend a wildcard to the domain. Default is True.
        :param expired: Whether to include expired certificates. Default is True.
        :return: List of certificate data objects.
        """
        url = self.build_url(domain, wildcard, expired)
        response = requests.get(url, headers={'User-Agent': self.user_agent})
        
        if response.ok:
            try:
                return response.json()
            except ValueError as err:
                print(f"Error decoding JSON: {err}")
            except Exception as err:
                print(f"An unexpected error occurred: {err}")
        else:
            response.raise_for_status()
        return None
    

def main():
    parser = argparse.ArgumentParser(description="""
    CertSPY: A Python client for the crt.sh website to retrieve subdomains information.
    Author: Omar Santos (@santosomar). """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("domain", help="The domain to search for (e.g., websploit.org).")
    args = parser.parse_args()
    
    client = CrtshClient()
    result = client.search(args.domain)
    if result:
        for entry in result:
            print(json.dumps(entry, indent=4))
    
if __name__ == "__main__":
    main()
