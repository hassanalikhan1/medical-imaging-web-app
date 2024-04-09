# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
