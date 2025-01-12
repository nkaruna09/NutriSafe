# Use the official Python base image
FROM python:3.10-slim

# Install system dependencies for zbar
RUN apt-get update && apt-get install -y \
    zbar-tools \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy your requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files into the container
COPY . .

# Expose port 8501 (Streamlit's default)
EXPOSE 8501

# Start Streamlit app when the container is run
CMD ["streamlit", "run", "app.py"]
