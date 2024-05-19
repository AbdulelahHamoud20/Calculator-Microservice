import requests
import json

def test_calculator_service():
    url = 'http://127.0.0.1:5000/calculate'
    headers = {'Content-Type': 'application/json'}

    # Example request data
    data = {
        'operation': 'multiply',
        'num1': 10,
        'num2': 5
    }

    

    # Send the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print the response data
    if response.status_code == 200:
        result = response.json().get('result')
        print(f"Result: {result}")
    else:
        print(f"Error: {response.json().get('error')}")

if __name__ == '__main__':
    test_calculator_service()
