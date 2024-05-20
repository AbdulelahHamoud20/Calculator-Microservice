# Calculator Microservice

## How to Run Locally

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd <repository_directory>

2. Set Up Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies:
pip install -r requirements.txt

4. Run the Microservice:
python microservice.py

5. Run the Test Program:
python test_program.py

Request Data
To programmatically request data from the microservice, send a POST request to /calculate with the following JSON body:

{
  "operation": "add",
  "num1": 10,
  "num2": 5
}

Receive Data
The response will be a JSON object containing the result:

{
  "result": 15
}

Example call: 
import requests
import json

url = 'http://127.0.0.1:5000/calculate'
headers = {'Content-Type': 'application/json'}
data = {
    'operation': 'add',
    'num1': 10,
    'num2': 5
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())

UML Sequence Diagram
<img width="271" alt="image" src="https://github.com/AbdulelahHamoud20/Calculator-Microservice/assets/114612988/d5223a38-8455-48db-9e4a-f114983bd738">





