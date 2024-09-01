# CertSPY - A Crt.sh Python Client
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Dependabot](https://img.shields.io/badge/dependabot-025E8C?style=for-the-badge&logo=dependabot&logoColor=white)

CertSPY is a Python client for interfacing with the [crt.sh](https://crt.sh/) website, allowing users to retrieve information on subdomains from SSL certificate transparency logs.

Certificate Transparency (CT) is an open framework aimed at improving the safety of SSL/TLS certificates by creating an open and auditable log of all certificates issued by certificate authorities. It allows for the detection of mistakenly or maliciously issued certificates. In the context of reconnaissance (recon), cybersecurity experts and ethical hackers can utilize CT logs as a rich source of information for mapping the internet landscape. They can extract data about the existence of subdomains of a target domain, revealing potential targets for further investigation or penetration testing. This kind of intel can be vital in identifying vulnerable endpoints, tracking the issuance of new certificates, and generally maintaining a strong security posture against potential cyber threats. The tool crafted in the script leverages CT logs accessible through the crt.sh platform to facilitate such recon efforts, aiding in the timely identification of potential security vulnerabilities.

## Features

- Query subdomain information from crt.sh.
- Support for wildcard and expired certificate queries.
- Command-line interface for easy usage.
- Option to save results to a file.
- Ability to display only the common names of certificates.


## Installation

You can install CertSPY using the `pip` command:

```sh
pip install certspy
```

## Dependencies

- Python 3.x
- `requests` library

## Usage

You can use the client from the command line with the following syntax:

```sh
certspy.py secretcorp.org
```

This will query the crt.sh website for subdomains of `secretcorp.org` and pretty print the JSON output to the console.

```sh
$ python3 certspy.py -h
usage: certspy.py [-h] [--no-wildcard] [--include-expired] [--common-name-only] [--output OUTPUT] domain

    CertSPY: A Python client for the crt.sh website to retrieve subdomains information.
    Author: Omar Santos (@santosomar).

positional arguments:
  domain                Domain to search for

optional arguments:
  -h, --help            show this help message and exit
  --no-wildcard         Do not prepend a wildcard to the domain.
  --include-expired     Include expired certificates in the search.
  --common-name-only    Show only the hostnames in the common name field of the certificate.
  --output OUTPUT, -o OUTPUT
                        Save output to a JSON file. You need to specify the path and name of the output file.
```

For example:

```sh
$ certspy secretcorp.org
[
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "secretcorp.org",
        "name_value": "secretcorp.org",
        "id": 10254588889,
        "entry_timestamp": "2023-08-30T08:49:46.284",
        "not_before": "2023-08-30T07:49:06",
        "not_after": "2023-11-28T07:49:05",
        "serial_number": "046cb5a18ef41e26f9867cfdb61d28452047"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "mail.secretcorp.org",
        "name_value": "mail.secretcorp.org",
        "id": 10039294064,
        "entry_timestamp": "2023-08-01T04:19:56.363",
        "not_before": "2023-08-01T03:19:55",
        "not_after": "2023-10-30T03:19:54",
        "serial_number": "049b42b3d9dfad81b882209188f2dd3416e4"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "app1.secretcorp.org",
        "name_value": "app1.secretcorp.org",
        "id": 10038384450,
        "entry_timestamp": "2023-08-01T01:00:56.816",
        "not_before": "2023-08-01T00:00:56",
        "not_after": "2023-10-30T00:00:55",
        "serial_number": "046bbf0c4112b9c2a1a8b30d8e50c8050264"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "app1.secretcorp.org",
        "name_value": "app1.secretcorp.org",
        "id": 10101930727,
        "entry_timestamp": "2023-08-01T01:00:56.476",
        "not_before": "2023-08-01T00:00:56",
        "not_after": "2023-10-30T00:00:55",
        "serial_number": "046bbf0c4112b9c2a1a8b30d8e50c8050264"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "internal.secretcorp.org",
        "name_value": "internal.secretcorp.org",
        "id": 10139355714,
        "entry_timestamp": "2023-07-31T22:56:26.114",
        "not_before": "2023-07-31T21:56:25",
        "not_after": "2023-10-29T21:56:24",
        "serial_number": "04f8357ed61e079460ed7d0bdb767ac49652"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "internal.secretcorp.org",
        "name_value": "internal.secretcorp.org",
        "id": 10101183289,
        "entry_timestamp": "2023-07-31T22:56:25.812",
        "not_before": "2023-07-31T21:56:25",
        "not_after": "2023-10-29T21:56:24",
        "serial_number": "04f8357ed61e079460ed7d0bdb767ac49652"
    },
    {
        "issuer_ca_id": 183267,
        "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
        "common_name": "cloud.secretcorp.org",
        "name_value": "cloud.secretcorp.org",
        "id": 10138072059,
        "entry_timestamp": "2023-07-31T20:15:24.822",
        "not_before": "2023-07-31T19:15:24",
        "not_after": "2023-10-29T19:15:23",
        "serial_number": "03efca1ae2f0688ac75231e58a0401716f0f"
    },
    <output omitted for brevity>
]
```

To show only the common names of the certificates, you can use the `--common-name-only` flag:

```sh
$ certspy secretcorp.org --common-name-only
[
    "secretcorp.org",
    "mail.secretcorp.org",
    "app1.secretcorp.org",
    "internal.secretcorp.org",
    "cloud.secretcorp.org",
    <output omitted for brevity>
]
```

To save the results to a file, you can use the `--output` flag:

```sh
$ certspy secretcorp.org --output results.json
```


## Contribution

Feel free to fork the repository and submit pull requests. For bug reports and feature requests, please create an issue in the GitHub issue tracker.

## License

See [LICENSE](LICENSE) for more details.

