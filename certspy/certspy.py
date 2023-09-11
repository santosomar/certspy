'''
This is a Python client for the crt.sh website to retrieve subdomains information.
@Author: Omar Santos @santosomar
Version: 1.0
'''

# Import the required libraries 
import requests
import json
import argparse

# Define the certspy class
class certspy(object):
    """
    CertSpy is a Python client for the crt.sh website to retrieve subdomains information.
    """
    def search(self, domain, wildcard=True, expired=True):
        """
        Search crt.sh for the given domain and returns a list of certificate data.
        
        :param domain: Domain to search for.
        :param wildcard: Whether to prepend a wildcard to the domain. Default is True.
        :param expired: Whether to include expired certificates. Default is True.
        :return: List of certificate data objects.
        """
        base_url = "https://crt.sh/?q={}&output=json"
        if not expired:
            base_url = base_url + "&exclude=expired"
        if wildcard and "%" not in domain:
            domain = "%.{}".format(domain)
        url = base_url.format(domain)

        ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        req = requests.get(url, headers={'User-Agent': ua})

        if req.ok:
            try:
                content = req.content.decode('utf-8')
                data = json.loads(content)
                return data
            except ValueError:
                data = json.loads("[{}]".format(content.replace('}{', '},{')))
                return data
            except Exception as err:
                print(f"Error retrieving information: {err}")
        return None

def main():
    parser = argparse.ArgumentParser(description="""
    CertSPY: A Python client for the crt.sh website to retrieve subdomains information.
    Author: Omar Santos (@santosomar). """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('domain', help='Domain to search for')
    parser.add_argument('--no-wildcard', action='store_false', help='Do not prepend a wildcard to the domain')
    parser.add_argument('--include-expired', action='store_true', help='Include expired certificates in the search')

    args = parser.parse_args()

    api = certspy()
    result = api.search(args.domain, wildcard=args.no_wildcard, expired=args.include_expired)

    if result:
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
