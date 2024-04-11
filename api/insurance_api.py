# insurance_api.py

import requests
import json

def verify_insurance(patient_id):
    # Dummy API endpoint for insurance verification
    url = 'https://api.example.com/insurance/verify'
    payload = {'patient_id': patient_id}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to verify insurance'}
    except Exception as e:
        return {'error': str(e)}

# Example usage:
patient_id = 1
insurance_info = verify_insurance(patient_id)
print(json.dumps(insurance_info, indent=4))
