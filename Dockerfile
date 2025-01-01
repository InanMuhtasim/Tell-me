# Use the official Python slim image as a base
FROM python:3.9-slim

# Set environment variables to avoid interactive prompts during apt-get install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies needed for mysqlclient and Python build tools
RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    libmariadb-dev \
    build-essential \
    gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the application's requirements file to the container
COPY requirements.txt /app/

# Create a virtual environment and install Python dependencies
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that your app will run on
EXPOSE 8000

# Define the default command to run the application
# Change this to match your application’s entry point
CMD ["/opt/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
