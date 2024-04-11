# scheduling_api.py

from datetime import datetime

def create_appointment(patient_id, appointment_date):
    # Dummy function to create an appointment
    try:
        # Perform validation and create appointment
        if validate_appointment_date(appointment_date):
            # Appointment creation logic
            return {'success': True, 'message': 'Appointment created successfully'}
        else:
            return {'success': False, 'message': 'Invalid appointment date'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def validate_appointment_date(appointment_date):
    # Dummy function to validate appointment date
    try:
        # Perform validation logic
        appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Example usage:
patient_id = 1
appointment_date = '2022-04-15'
result = create_appointment(patient_id, appointment_date)
print(result)
