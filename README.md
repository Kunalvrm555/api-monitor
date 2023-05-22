# Monitoring Application with Docker and Cron

This project sets up a monitoring application using Docker and Cron. It periodically checks the availability of an endpoint and sends an email notification if the endpoint is unavailable.

## Prerequisites

- Docker installed on your machine

## Getting Started

1. Clone this repository to your local machine.
2. Create a `.env` file in the project root directory and provide the following environment variables:

```env
SENDER_EMAIL=<sender_email>
SENDER_PASSWORD=<sender_email_password>
RECIPIENT_EMAIL=<recipient_email>
ENDPOINT_URL=<endpoint_url>
```

Replace `<sender_email>`, `<sender_email_password>`, `<recipient_email>`, and `<endpoint_url>` with your own values.

3. Build the Docker image by running the following command in the project root directory:

```apache
docker build -t api-monitor .
```

4. Run the Docker container:

```apache
docker run -d --name monitor-container monitor-app
```

This will start the container and run the monitoring application with the specified cron schedule.

5. To view the logs, use the following command:

```apache
docker logs monitor-container
```

This will display the logs including the email notifications and endpoint status.

## Customization

- Adjust the cron schedule in the `dockerfile` file. The default schedule is set to run every 15 minutes. Modify the cron expression according to your needs.
- Customize the email template in the `monitor.py`. Modify the HTML message to suit your requirements.

## License

This project is licensed under the MIT License.
