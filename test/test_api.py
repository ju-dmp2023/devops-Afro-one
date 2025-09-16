import requests 
from calculator_client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse


class TestCalculatrorAPI():
    def test_add_api(self):
        url = "http://localhost:5000/calculate"
        payload = {
            "operation":"add",
            "operand1": 5,
            "operand2": 5
        }
        response = requests.post(url, json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 10
    
    def test_generated_code(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body=Calculation(Opertions.ADD, operand1=1, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result==3

    
