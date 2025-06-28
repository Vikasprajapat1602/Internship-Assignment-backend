from celery import shared_task
import time

@shared_task
def send_welcome_email(username):
    print(f"Welcome {username}! Your account has been created.")
    time.sleep(3)
    print("Email sent (simulated).")
    return True
