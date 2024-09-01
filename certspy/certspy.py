__author__ = "Omar Santos (@santosomar)"
__version__ = "0.9.0"
__description__ = "A Python client for the crt.sh website to retrieve subdomains information."

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

        # Check if the request was successful 
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

    def format_results(self, data, common_name_only=False):
        """
        Format the results based on the common_name_only flag.
        
        :param data: List of certificate data objects.
        :param common_name_only: Whether to return only common names. Default is False.
        :return: Formatted results (list of common names or full data).
        """
        if common_name_only:
            return list(set(item['common_name'] for item in data))
        return data

def main():
    """
    Main function to parse arguments and execute the search.
    """
    parser = argparse.ArgumentParser(description="""
    CertSPY: A Python client for the crt.sh website to retrieve subdomains information.
    Author: Omar Santos (@santosomar). """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('domain', help='Domain to search for')
    parser.add_argument('--no-wildcard', action='store_true', help='Do not prepend a wildcard to the domain.')
    parser.add_argument('--include-expired', action='store_true', help='Include expired certificates in the search.')
    parser.add_argument('--common-name-only', action='store_true', help='Show only the hostnames in the common name field of the certificate.')
    parser.add_argument('--output', '-o', help='Save output to a JSON file. You need to specify the path and name of the output file.')

    args = parser.parse_args()

    api = certspy()
    result = api.search(args.domain, wildcard=not args.no_wildcard, expired=not args.include_expired)

    if result:
        formatted_result = api.format_results(result, common_name_only=args.common_name_only)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(formatted_result, f, indent=4)
            print(f"Hack the Planet! Results successfully saved to {args.output}")
        else:
            print(json.dumps(formatted_result, indent=4))

if __name__ == "__main__":
    main()
