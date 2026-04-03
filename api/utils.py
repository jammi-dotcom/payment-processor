import os
import json
import hashlib
import uuid
from typing import Dict

class PaymentProcessor:
    def __init__(self, payment_gateway: str, secret_key: str):
        self.payment_gateway = payment_gateway
        self.secret_key = secret_key
        self.payment_gateway_url = f"https://{payment_gateway}/api/v1"

    def get_payment_gateway_id(self) -> str:
        return self.payment_gateway_url + "/v1/payments"

    def get_payment_gateway_token(self) -> str:
        return self.payment_gateway_url + "/v1/payments/token"

    def get_payment_gateway_token_response(self) -> Dict:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.payment_gateway_token}"
        }
        response = requests.get(self.get_payment_gateway_token(), headers=headers)
        return response.json()

    def create_payment(self, amount: float, currency: str, description: str, payment_method: str) -> Dict:
        data = {
            "amount": amount,
            "currency": currency,
            "description": description,
            "payment_method": payment_method
        }
        response = requests.post(self.get_payment_gateway_token_response(), json=data)
        return response.json()

    def get_payment(self, payment_id: str) -> Dict:
        response = requests.get(f"{self.get_payment_gateway_url}/v1/payments/{payment_id}")
        return response.json()

    def update_payment(self, payment_id: str, data: Dict) -> Dict:
        response = requests.put(f"{self.get_payment_gateway_url}/v1/payments/{payment_id}", json=data)
        return response.json()

    def delete_payment(self, payment_id: str) -> Dict:
        response = requests.delete(f"{self.get_payment_gateway_url}/v1/payments/{payment_id}")
        return response.json()