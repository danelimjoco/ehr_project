# Dockerfile for PostgreSQL database

# Use an official PostgreSQL image as a parent image
FROM postgres:latest

# Copy the initialization script into the container
COPY init_script.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
