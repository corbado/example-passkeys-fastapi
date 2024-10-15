# Base image
FROM python:latest

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy .env file (including credentials) and project code
COPY . .

# Expose port
EXPOSE 3000

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]