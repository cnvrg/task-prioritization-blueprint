import requests
import argparse
import base64
from requests.structures import CaseInsensitiveDict
import json 
import os

cnvrg_workdir = os.environ.get('CNVRG_WORKDIR', '/cnvrg')

parser = argparse.ArgumentParser(description="""Preprocessor""")

parser.add_argument('--domain', action='store', dest='domain', required=True,
					help="""string domain name""")

parser.add_argument('--email', action='store', dest='email', required=True,
					help="""string email""")

parser.add_argument('--password', action='store', dest='password', required=True,
					help="""string password""")

parser.add_argument('--field', action='store', dest='field', required=False, default="subject",
					help="""string password""")


args = parser.parse_args()
domain = args.domain
email = args.email
password = args.password
field = args.field


message = email+':'+password
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic "+str(base64_bytes)[2:-1]

response = requests.get('https://'+domain+'.zendesk.com/api/v2/tickets.json', headers=headers)


tickets =json.loads(response.content.decode("utf-8"))


subjects = [t[field] for t in tickets['tickets']]
with open(cnvrg_workdir + '/tickets.json', 'w') as outfile:
	json.dump(subjects, outfile)
