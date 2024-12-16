'''
from flask import Flask

# Creating an instance of the Flask class
app = Flask(__name__)

#creating decorator which will be done  just before the function, can be used for purpose like authn
@app.route('/')
def hello():
    return 'Hey There'

# Running the app on localhost
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # You can specify a different port if needed, 5000 is by default port flask uses

'''
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    data = request.json
    
    # Extract title and command body from the incoming JSON
    title = data["issue"]["title"]
    command_body = data['comment']['body']

    # Check if the comment contains the keyword '@jira'
    if "@jira" in command_body:
        url = "https://bluewhale.atlassian.net/rest/api/3/issue"  # Your Jira URL
        
        # Replace with your actual API token and email
        API_TOKEN = "your_api_token_xFfGF0on8r9cToGCf21ayHVp5hrHLBc3U9AC7-VUpUoMM4VMEbq2Ns28eS3wMYtz4ahd8OHCkTcgH9mx-uda_N7t5XsMdup3jV63UF35K45yj06PxOuHDzguBY2NR7-m6zUI9Ek55XzflizG_BrGdx0nyDELvnn5LN-uPjMVVfQ3bwlBI=0EA50AD2"
        auth = HTTPBasicAuth("xyz@gmail.com", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
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
                    "key": "SCRUM"  # Ensure this project key is correct
                },
                "issuetype": {
                    "id": "10006"  # Ensure this issue type ID is valid for your project
                },
                "summary": title,
            }
        })

        response = requests.post(
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        # Print the status code and response content for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # Check if the response indicates success or failure
        if response.status_code in [200, 201]:
            print("Issue created successfully.")
            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")) 
        else:
            print("Failed to create issue. Check the response for details.")
            return json.dumps({"error": response.text}), response.status_code

    else:
        # If '@jira' is not in the comment, simply return a message indicating no action was taken.
        print("No action taken; comment does not contain '@jira'.")
        return json.dumps({"message": "No action taken; comment does not contain '@jira'."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
