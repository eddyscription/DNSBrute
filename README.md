# DNSBrute
DNSBrute: Subdomain Enumeration Tool using Wordlists in Python

The code is a subdomain search tool written in Python that uses a word list to generate possible subdomains for a given domain. The tool uses the "dns.resolver" library to resolve the IP addresses corresponding to the generated subdomains and print the results on the screen.

The user must provide the name of the target domain and the path to the word list file. The code then attempts to open the file and read the lines. If the file is found, it iterates through each word in the list and generates subdomains by concatenating them with the target domain name. If an IP address is found for a generated subdomain, it is printed on the screen.

How to use:
Insert in this order, site and dictionary.

      python3 dnsbrute.py abcdefg.com dnsbrutedictionaryPTBR.txt




It's important to note that DNSBrute is a tool that can be used for penetration testing purposes, and should be used responsibly and only on authorized systems.
