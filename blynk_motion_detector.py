import random
import time
import smtplib
from email.message import EmailMessage
from blynklib import Blynk

BLYNK_AUTH_TOKEN = 'z0flmWimEdXclAckv4wy3ltnzoBtIHhz'
EMAIL_ADDRESS = 'shankxebec@gmail.com'
EMAIL_PASSWORD = 'wkos quwf aybr bqlq'
NOTIFICATION_EMAIL = 'blenzorob@gmail.com'

blynk = Blynk(BLYNK_AUTH_TOKEN)

def send_email_alert():
    print("\nAttempting to send email notification...")
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    msg = EmailMessage()
    msg['Subject'] = '🚨 Movement Detected!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = NOTIFICATION_EMAIL
    msg.set_content(f'Motion detected at {time.strftime("%Y-%m-%d %H:%M:%S")}')
    
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email sent successfully!")
        return True

def movement_detection():
    while True:
        if random.randint(0, 4) == 0:  # 20% chance
            timestamp = time.strftime('%H:%M:%S')
            print(f"\nMOVEMENT DETECTED at {timestamp}")
            
            blynk.virtual_write(0, 1)
            time.sleep(1)
            blynk.virtual_write(0, 0)
            
            send_email_alert()
            
        time.sleep(10)

def main():
    print("Movement Detector Running (Ctrl+C to stop)")
    print("Testing email system first...")
    
    if send_email_alert():
        print("Email test successful! Starting detector...")
    else:
        print("Email test failed.")
    
    import threading
    threading.Thread(target=movement_detection, daemon=True).start()
    
    try:
        while True:
            blynk.run()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == "__main__":
    main()