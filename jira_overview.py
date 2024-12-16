import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://bluewhale.atlassian.net//rest/api/3/issue"

API_Token = "Your_api_token_T3xFfGF0MGpTicVFdQYxgMPwZ57FWfvHtb1sZ5bJ_SNj6fdKHrbqhnmw8C-KP89t0dqaMn53zvB47cgGRcfmTYvUIsK2tLW65Tou-nb2kQ4lrtfjeNGzjhhHBFMzEcmy4HZvHnOzDuzEdRpDtjjob3Ot0xrNuM0t7lvi5xE6wMxTZk7AkiM=B7CB8733"


auth = HTTPBasicAuth("Xyz@gmail.com", API_Token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "RA"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))