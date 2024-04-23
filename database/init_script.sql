-- YOU DONT NEED TO CREATE DATABASE HERE, IT IS ALREADY CREATED IN docker-compose.yml
--CREATE DATABASE ehr_database; Y

-- Connect to the newly created database
\c ehr_database;

-- Create tables for the EHR database
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    address VARCHAR(100),
    insurance_id INT
);

CREATE TABLE patient_insurance (
    insurance_id SERIAL PRIMARY KEY,
    insurance_name VARCHAR(100),
    copay DECIMAL(10, 2),
    deductible DECIMAL(10, 2),
    coinsurance DECIMAL(5, 2)
);

CREATE TABLE evaluations (
    eval_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    date_of_evaluation DATE,
    diagnosis VARCHAR(255),
    physician VARCHAR(100)
);

CREATE TABLE treatments (
    treatment_id SERIAL PRIMARY KEY,
    eval_id INT REFERENCES evaluations(eval_id),
    treatment_date DATE,
    treatment_notes TEXT
);

-- Create users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    is_active BOOL NOT NULL DEFAULT TRUE
);

-- Insert dummy data into the tables
INSERT INTO patients (first_name, last_name, date_of_birth, gender, address, insurance_id)
VALUES
    ('John', 'Doe', '1980-01-01', 'Male', '123 Main St', 1),
    ('Jane', 'Smith', '1985-05-15', 'Female', '456 Elm St', 2);

INSERT INTO patient_insurance (insurance_name, copay, deductible, coinsurance)
VALUES
    ('Blue Cross Blue Shield', 25.00, 1000.00, 0.20),
    ('UnitedHealthcare', 30.00, 1500.00, 0.25);

INSERT INTO evaluations (patient_id, date_of_evaluation, diagnosis, physician)
VALUES
    (1, '2022-01-05', 'Lower back pain', 'Dr. Smith'),
    (2, '2022-02-10', 'Knee injury', 'Dr. Johnson');

INSERT INTO treatments (eval_id, treatment_date, treatment_notes)
VALUES
    (1, '2022-01-07', 'Prescribed physical therapy for 6 weeks.'),
    (2, '2022-02-12', 'Administered corticosteroid injection.');

-- Insert dummy data into the users table
INSERT INTO users (username, password_hash, email)
VALUES
    ('admin', 'admin123', 'admin@example.com');
