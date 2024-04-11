import psycopg2
import logging

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.logger.setLevel(logging.INFO) 

# Database connection configuration
DB_HOST = 'localhost'
DB_NAME = 'ehr_database'
DB_USER = 'danelimjoco'
DB_PASSWORD = 'Uppt1986!'

# Function to add a new patient
def add_patient(first_name, last_name, date_of_birth, gender, address, insurance_id):
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (first_name, last_name, date_of_birth, gender, address, insurance_id) VALUES (%s, %s, %s, %s, %s, %s)",
                   (first_name, last_name, date_of_birth, gender, address, insurance_id))
    conn.commit()
    conn.close()
    app.logger.info("ADDED PATIENT!")
    pass

# Function to get patient info
def get_patient_info(patient_id):
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    patient_info = cursor.fetchone()
    conn.commit()
    conn.close()
    return patient_info

# Function to update patient info
def update_patient_info(patient_id, first_name, last_name, date_of_birth, gender, address, insurance_id):
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("UPDATE patients SET first_name = %s, last_name = %s, date_of_birth = %s, gender = %s, address = %s, insurance_id = %s WHERE patient_id = %s",
                   (first_name, last_name, date_of_birth, gender, address, insurance_id, patient_id))
    conn.commit()
    conn.close()
    pass

# Function to delete patient info
def delete_patient_info(patient_id):
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
    conn.commit()
    conn.close()
    pass

# Route for adding a new patient
@app.route('/add_patient', methods=['POST'])
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
    return redirect(url_for('index', action='added'))

# Route for getting patient info
@app.route('/get_patient', methods=['GET'])
def get_patient_route():
    # Get patient ID from query parameters
    patient_id = request.args.get('patient_id')

    # Get patient info from database
    patient_info = get_patient_info(patient_id)

    if patient_info:
        # Render template with patient info
        return render_template('index.html', patient_info=patient_info, action='retrieved')
    else:
        # Render template with error message
        return render_template('index.html', action='not_found')

# Route for updating patient info
@app.route('/update_patient', methods=['POST'])
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
    return redirect(url_for('index', action='updated'))

# Route for deleting patient info
@app.route('/delete_patient', methods=['POST'])
def delete_patient_route():
    # Get patient ID from query parameters
    patient_id = request.form['patient_id']
    
    # Delete patient info from database
    delete_patient_info(patient_id)
    
    # Redirect to index page with success message
    return redirect(url_for('index', action='deleted'))

# Route for the index page
@app.route('/')
def index():
    # Check for action parameter in URL (added, updated, deleted)
    action = request.args.get('action')
    return render_template('index.html', action=action)

if __name__ == '__main__':
    app.run(debug=True)
