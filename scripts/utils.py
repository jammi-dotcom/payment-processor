import datetime
import hashlib
import logging
import os
import pytz

from typing import Dict, List

logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    salt = os.urandom(32)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + hashed_password.hex()

def verify_password(stored_password: str, provided_password: str) -> bool:
    salt = bytes.fromhex(stored_password[:64])
    stored_hash = bytes.fromhex(stored_password[64:])
    return hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000).hex() == stored_hash.hex()

def generate_transaction_id() -> str:
    return hashlib.sha256(os.urandom(32)).hexdigest()

def get_current_timestamp() -> str:
    return datetime.datetime.now(pytz.utc).isoformat()

def get_transaction_status(status_code: int) -> Dict:
    status_map = {
        200: {'status': 'success', 'message': 'Transaction successful'},
        404: {'status': 'error', 'message': 'Transaction not found'},
        500: {'status': 'error', 'message': 'Internal server error'}
    }
    return status_map.get(status_code, {'status': 'error', 'message': 'Invalid status code'})

def validate_request_body(request_body: Dict, required_fields: List) -> bool:
    return all(field in request_body for field in required_fields)

def format_response(response_data: Dict) -> Dict:
    return {'data': response_data, 'timestamp': get_current_timestamp()}