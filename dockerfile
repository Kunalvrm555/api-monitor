# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get -y install cron

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the monitor.py script
COPY monitor.py .

# Copy the crontab file
COPY crontab /etc/cron.d/monitor-cron

# Give execute permissions to the cron job
RUN chmod 0644 /etc/cron.d/monitor-cron

# Apply the cron job
RUN crontab /etc/cron.d/monitor-cron

# Run the cron service
CMD cron && tail -f /var/log/cron.log
