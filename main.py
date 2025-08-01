import csv
import smtplib
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# === Load credentials from Replit Secrets ===
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")

if not EMAIL_ADDRESS or not APP_PASSWORD:
    raise EnvironmentError("❌ Missing EMAIL_ADDRESS or APP_PASSWORD environment variables.")

# === Set today's date ===
today = datetime.now().strftime("%B %d, %Y")

# === Folder where invoices are stored ===
invoice_folder = "invoices"
client_file = "clients.csv"

# === Ensure client file exists ===
if not os.path.exists(client_file):
    raise FileNotFoundError(f"❌ The file '{client_file}' was not found. Please upload it and try again.")

# === Track sending stats ===
sent_count = 0
failed_count = 0
skipped_count = 0

with open(client_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row.get("name", "Client").strip()
        to_email = row.get("email", "").strip()
        pdf_filename = row.get("file", "").strip()
        pdf_path = os.path.join(invoice_folder, pdf_filename)

        # === Check for missing file ===
        if not os.path.exists(pdf_path):
            print(f"❌ File '{pdf_filename}' not found for {name}. Skipping...")
            skipped_count += 1
            continue

        # === Compose Email ===
        subject = f"Invoice Report - {today}"
        body = f"""Hello {name},

Please find attached your invoice dated {today}.

Regards,
Eric Mutisya"""

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # === Attach the invoice PDF ===
        try:
            with open(pdf_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=pdf_filename)
                part["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
                msg.attach(part)
        except Exception as e:
            print(f"❌ Error reading file '{pdf_filename}': {e}")
            failed_count += 1
            continue

        # === Send the Email ===
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
                smtp.send_message(msg)
            print(f"✅ Email sent to {name} at {to_email}")
            sent_count += 1
        except Exception as e:
            print(f"❌ Failed to send email to {name} at {to_email}: {e}")
            failed_count += 1

# === Final Summary ===
print("\n=== Summary ===")
print(f"✅ Sent: {sent_count}")
print(f"⚠️ Skipped (file not found): {skipped_count}")
print(f"❌ Failed (error while sending): {failed_count}")
