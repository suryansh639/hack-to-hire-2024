# Flight Status and Notifications System

## Overview
This project is a full-stack application designed to provide real-time flight status updates and notifications to passengers. The system displays information about flight delays, cancellations, and gate changes, and sends notifications via SMS, email, or app notifications.

## Tech Stack

### Frontend
- **React.js:** A JavaScript library for building user interfaces, used to create the dynamic and responsive frontend.
- **HTML5 & CSS3:** Markup and styling for the frontend.

### Backend
- **Python (Flask):** A micro web framework used to build the backend REST API.
- **Mock Data:** For the purpose of this implementation, mock data is used to simulate flight information.

### Database
- The project currently does not use a database but could integrate MongoDB or PostgreSQL for persistent data storage.

### Notifications
- **Firebase Cloud Messaging (FCM):** Used to send push notifications to users' devices.
- **Kafka/RabbitMQ:** Potential alternatives for managing notifications (not implemented in this demo).

## Project Structure

### Frontend
- **FlightStatus.js:** The main component that fetches and displays flight data.
- **App.js:** The root component of the React application.
- **index.html:** The entry point for the web application.

### Backend
- **app.py:** The main Flask application file that serves the API endpoints for fetching flight data and handling subscriptions.

### Notifications
- **firebase_admin.py:** A utility script for initializing Firebase Admin SDK and sending notifications.

## Setup and Running the Project

### Frontend
1. Navigate to the frontend directory.
2. Install dependencies: `npm install`.
3. Start the development server: `npm start`.

### Backend
1. Navigate to the backend directory.
2. Install dependencies: `pip install flask`.
3. Start the server: `python app.py`.

## Future Enhancements
- Integration with real-time airport and airline APIs for live data.
- Implementation of user authentication and subscription management.
- Use of a persistent database (e.g., MongoDB or PostgreSQL) for storing flight data and user subscriptions.
- Enhancements to the notification system using Kafka or RabbitMQ for more robust message queuing.

## Contributors
- Developer: SURYANSH GUPTA

## License
This project is open-source and available under the [MIT License](LICENSE).
