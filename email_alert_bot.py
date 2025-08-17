import smtplib
from email.mime.text import MIMEText
import time
import os

# ---------------- CONFIG ----------------
LOG_FILE = "application.log"       # Path to the log file
CHECK_INTERVAL = 30                # Time in seconds between scans
EMAIL_SENDER = "mahithabobba@gmail.com"
EMAIL_PASSWORD = "qsqaudaocbbwmizu"   # For Gmail, use App Password
EMAIL_RECEIVER = "bobbamahitha@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
KEYWORDS = ["ERROR", "FAILURE", "CRITICAL"]
# ----------------------------------------

def send_email_alert(errors):
    """Send an email with the list of detected errors."""
    subject = "🚨 Application Failure Alert"
    body = "\n".join(errors)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            print("✅ Alert email sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


def monitor_logs():
    """Continuously monitor the log file for errors."""
    print("📡 Monitoring logs...")
    file_position = 0

    while True:
        if not os.path.exists(LOG_FILE):
            print("⚠️ Log file not found, retrying...")
            time.sleep(CHECK_INTERVAL)
            continue

        with open(LOG_FILE, "r") as f:
            f.seek(file_position)
            lines = f.readlines()
            file_position = f.tell()

        errors = [line.strip() for line in lines if any(keyword in line for keyword in KEYWORDS)]

        if errors:
            print("🚨 Errors detected, sending alert...")
            send_email_alert(errors)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_logs()
