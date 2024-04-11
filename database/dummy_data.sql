-- dummy_data.sql

-- Insert dummy data into the tables
INSERT INTO patients (patient_id, first_name, last_name, date_of_birth, gender, address, insurance_id)
VALUES
    (1, 'John', 'Doe', '1980-01-01', 'Male', '123 Main St', 1),
    (2, 'Jane', 'Smith', '1985-05-15', 'Female', '456 Elm St', 2);

INSERT INTO patient_insurance (insurance_id, insurance_name, copay, deductible, coinsurance)
VALUES
    (1, 'Blue Cross Blue Shield', 25.00, 1000.00, 0.20),
    (2, 'UnitedHealthcare', 30.00, 1500.00, 0.25);

INSERT INTO evaluations (eval_id, patient_id, date_of_evaluation, diagnosis, physician)
VALUES
    (1, 1, '2022-01-05', 'Lower back pain', 'Dr. Smith'),
    (2, 2, '2022-02-10', 'Knee injury', 'Dr. Johnson');

INSERT INTO treatments (treatment_id, eval_id, treatment_date, treatment_notes)
VALUES
    (1, 1, '2022-01-07', 'Prescribed physical therapy for 6 weeks.'),
    (2, 2, '2022-02-12', 'Administered corticosteroid injection.');
