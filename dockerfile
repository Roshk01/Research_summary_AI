# Use an official Python runtime as base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your app code into the container
COPY . .

# Install system dependencies (for audio + NLP)
RUN apt-get update && \
    apt-get install -y ffmpeg espeak libespeak1 && \
    apt-get clean

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip
RUN pip install gtts
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Streamlit runs on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
