###  Assignment No 5 ###

"""Assignment Title :  Implement regular expression function to find URL, IP address, Date,
PAN number in textual data using python libraries"""

import re

# Sample text data
text = """
Visit our website: https://www.sample.com
Server IP: 192.168.45.100
Date: 2023-01-01
PAN: ABCDE1234F
"""

# Define regex patterns
url_pattern = r'https?://\S+|www\.\S+'
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
date_pattern = r'\d{4}-\d{2}-\d{2}'
pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'

# Find all matches
urls = re.findall(url_pattern, text)
ips = re.findall(ip_pattern, text)
dates = re.findall(date_pattern, text)
pans = re.findall(pan_pattern, text)

# Print results
print("URLs:", urls)
print("IP Addresses:", ips)
print("Dates:", dates)
print("PAN Numbers:", pans)