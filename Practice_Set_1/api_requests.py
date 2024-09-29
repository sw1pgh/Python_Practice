# Importing the Requests -> Python external module
import requests

def api_request_using_external_module():
    
    # store the response from an API in response
    response = requests.get("https://api.github.com")
    
    # Checking if the reponse status
    if response.status_code == 200:
        print("Successfully connected to GitHub API!")
    else:
        print("Failed to connect to GitHub API!")
        
if __name__ == '__main__':
    api_request_using_external_module()