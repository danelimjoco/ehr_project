from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from app.models.patients import Patient
from app import db

# Create a Blueprint for patient routes
patient_bp = Blueprint('patient', __name__, url_prefix='/patients')

#############
# Functions #   
#############

# Function to add a new patient
def add_patient(first_name, last_name, date_of_birth, gender, address, insurance_id):
    new_patient = Patient(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender,
        address=address,
        insurance_id=insurance_id
    )
    db.session.add(new_patient)
    db.session.commit()

# Function to get patient info
def get_patient_info(patient_id):
    patient = Patient.query.filter_by(patient_id=patient_id).first()
    if patient:
        return patient.serialize()
    else:
        return None

# Function to update patient info
def update_patient_info(patient_id, first_name, last_name, date_of_birth, gender, address, insurance_id):
    patient = Patient.query.get(patient_id)
    if patient:
        patient.first_name = first_name
        patient.last_name = last_name
        patient.date_of_birth = date_of_birth
        patient.gender = gender
        patient.address = address
        patient.insurance_id = insurance_id
        db.session.commit()

# Function to delete patient info
def delete_patient_info(patient_id):
    patient = Patient.query.get(patient_id)
    if patient:
        db.session.delete(patient)
        db.session.commit()

##########
# Routes #
##########     

# Route for the index page
@patient_bp.route('/')
def index():
    # Check for action parameter in URL (added, updated, deleted)
    action = request.args.get('action')
    return render_template('patients.html', action=action) 

# Route for adding a new patient
@patient_bp.route('/add_patient', methods=['POST'])
def add_patient_route():
    # Get form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    address = request.form['address']
    insurance_id = request.form['insurance_id']
    
    # Add patient to database
    add_patient(first_name, last_name, date_of_birth, gender, address, insurance_id)
    
    # Redirect to index page with success message
    return redirect(url_for('patient.index', action='added'))

# Route for getting patient info
@patient_bp.route('/get_patient', methods=['GET'])
def get_patient_route():
    # Get patient ID from query parameters
    patient_id = request.args.get('patient_id')

    # Get patient info from database
    patient_info = get_patient_info(patient_id)

    if patient_info:
        # Return JSON representation of patient
        return render_template('patients.html', patient_info=patient_info, action='retrieved')

    # Render template with error message
    return render_template('patients.html', action='not_found')

# Route for updating patient info
@patient_bp.route('/update_patient', methods=['POST'])
def update_patient_route():
    # Get form data
    patient_id = request.form['patient_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    address = request.form['address']
    insurance_id = request.form['insurance_id']
    
    # Update patient info in database
    update_patient_info(patient_id, first_name, last_name, date_of_birth, gender, address, insurance_id)
    
    # Redirect to index page with success message
    return redirect(url_for('patient.index', action='updated'))

# Route for deleting patient info
@patient_bp.route('/delete_patient', methods=['POST'])
def delete_patient_route():
    # Get patient ID from query parameters
    patient_id = request.form['patient_id']
    
    # Delete patient info from database
    delete_patient_info(patient_id)
    
    # Redirect to index page with success message
    return redirect(url_for('patient.index', action='deleted'))

