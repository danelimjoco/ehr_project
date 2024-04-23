# Electronic Health Record (EHR) Application

This project is an Electronic Health Record (EHR) application designed to streamline the management of patient information and scheduling for a physical therapy clinic.

# Table of Contents
- [Electronic Health Record (EHR) Application](#electronic-health-record-ehr-application)
  - [Features](#features)
  - [Directory Structure](#directory-structure)
  - [Setup and Usage](#setup-and-usage)
  - [Database setup](#database-setup)
  - [psql commands](#psql-commands)
  - [Running this app](#running-this-app)

## Features

- **Patient Information Management**: Collect and store patient demographic information, insurance details, treatment history, etc.
- **Insurance Verification**: Perform real-time or batch insurance verification to check coverage and eligibility.
- **Scheduling**: Manage appointments and schedule sessions for patients and therapists.
- **Integration with Electronic Health Records (EHR)**: Seamlessly integrate with existing EHR systems to ensure data consistency and interoperability.

## Directory Structure

The project directory is organized as follows:

- `api/`: Contains Python scripts for interacting with external APIs (e.g., insurance verification, scheduling).
- `database/`: Contains SQL scripts for database initialization and management.
- `src/`: Contains HTML and CSS files for the user interface (UI) of the application.
- `server/`: Contains server-side scripts (e.g., Flask application) for handling form submissions and database interactions.
- `README.md`: This file, providing an overview of the project and instructions for setup and usage.
- `requirements.txt`: File listing Python dependencies required for running the application.

## Setup and Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Initialize Database**: Run the database initialization script (`init_script.sql`) to create the necessary tables and schema in your PostgreSQL database.

3. **Load Dummy Data**: Optionally, load dummy data into your database tables to populate them with sample records.

4. **Install Dependencies**: Install the required Python dependencies listed in `requirements.txt` using pip.

   ```bash
   pip install -r requirements.txt
   ```

## Database setup (on local machine)

Install postgres

```bash
brew install postgresql
```

Confirm installation

```bash
psql --version 
```

Start the Postgres server

```bash
pg_ctl -D /opt/homebrew/var/postgresql@14/ start
```

Create an inital database for the first time

```bash
createdb
```

Run init script to initialize the ehr_database

```bash
psql -f init_script.sql
```


## Running this app (container for flask, container for db)

```bash
cd path/to/ehr_project
docker compose up
```

This will spin up 2 containers:
1. a flask app container (port 8080 on host machine, port 5000 on container)
2. a postgres container (port 5432 on host machine, port 5432 on container)

Now in browser, type:
```bash
http://localhost:8080/
```

This will show UI in browser and CRUD operations may be performed to interact with db on other container.

To check database container, run:
```bash
docker exec -it ehr_project-db-1 bash
```

Connect to database:

```bash
psql -U danelimjoco ehr_database
\c ehr_database
```

List tables

```bash
\dt
```

Get first 5 records of whatever table

```bash
SELECT * FROM table_name LIMIT 5;
```

Exit

```bash
\q
```






