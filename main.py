import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="Hydration Reminder for Surbhi",
            message="Time to sip some water!",
            timeout=10
        )
        time.sleep(3600)  # Remind every hour
        #time.sleep(3)  # For testing purposes only for 3 seconds

water_reminder()