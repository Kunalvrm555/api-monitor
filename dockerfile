# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy the monitor.py script
COPY monitor.py .

# Copy the .env file into the container
COPY .env .

# Set the environment variables from .env file
ENV $(cat .env | xargs)

# Create the cron job file
RUN echo "*/15 * * * * /usr/local/bin/python /app/monitor.py >> /var/log/cron.log 2>&1" > /etc/cron.d/monitor-cron

# Give execute permissions to the cron job file
RUN chmod 0644 /etc/cron.d/monitor-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Apply the cron job
RUN crontab /etc/cron.d/monitor-cron

# Start the cron service and keep the container running with tail
CMD cron && tail -f /var/log/cron.log
