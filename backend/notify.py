from firebase_admin import messaging

def notify_flight_status_change(flight_id):
    flight = next((f for f in flights if f['id'] == flight_id), None)
    if flight:
        tokens = ["user_device_token"]
        for token in tokens:
            send_notification(token, f"Flight {flight['number']} Status Update", f"Status: {flight['status']}")
