# CertSPY - A Crt.sh Python Client

CertSPY is a Python client for interfacing with the [crt.sh](https://crt.sh/) website, allowing users to retrieve information on subdomains from SSL certificate transparency logs.

Certificate Transparency (CT) is an open framework aimed at improving the safety of SSL/TLS certificates by creating an open and auditable log of all certificates issued by certificate authorities. It allows for the detection of mistakenly or maliciously issued certificates. In the context of reconnaissance (recon), cybersecurity experts and ethical hackers can utilize CT logs as a rich source of information for mapping the internet landscape. They can extract data about the existence of subdomains of a target domain, revealing potential targets for further investigation or penetration testing. This kind of intel can be vital in identifying vulnerable endpoints, tracking the issuance of new certificates, and generally maintaining a strong security posture against potential cyber threats. The tool crafted in the script leverages CT logs accessible through the crt.sh platform to facilitate such recon efforts, aiding in the timely identification of potential security vulnerabilities.

## Features

- Query subdomain information from crt.sh.
- Support for wildcard and expired certificate queries.
- Command-line interface for easy usage.

## Installation

You can clone the repository to your local machine using the following command:

```sh
git clone https://github.com/santosomar/certspy.git
```

## Dependencies

- Python 3.x
- `requests` library

You can install the necessary Python packages using the following command:

```sh
pip install -r requirements.txt
```

## Usage

You can use the client from the command line with the following syntax:

```sh
python crtsh_client.py secretcorp.org
```

This will query the crt.sh website for subdomains of `secretcorp.org` and pretty print the JSON output to the console.

```sh
$ python3 certspy.py -h
usage: certspy.py [-h] domain

    CertSPY: A Python client for the crt.sh website to retrieve subdomains information.
    Author: Omar Santos (@santosomar). 

positional arguments:
  domain      The domain to search for (e.g., websploit.org).

options:
  -h, --help  show this help message and exit
```

## Contribution

Feel free to fork the repository and submit pull requests. For bug reports and feature requests, please create an issue in the GitHub issue tracker.

## License

See [LICENSE](LICENSE) for more details.

