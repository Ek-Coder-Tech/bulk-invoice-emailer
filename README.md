# 📧 Automated Bulk Invoice Emailer

This Python script automates the task of sending personalized invoice PDFs to multiple recipients via email. It reads data from a `clients.csv` file, fetches corresponding invoice files from an `invoices` folder, and sends them as secure email attachments via Gmail.

---

## ✅ Features

- Reads recipient names, emails, and PDF filenames from a CSV file.
- Automatically attaches matching invoice PDFs from the `invoices` folder.
- Uses environment variables for secure email credentials.
- Skips missing files and logs failed email attempts without crashing.
- Console-based delivery report with summary at the end.

---

## 🗂️ Folder Structure

project-folder/
│
├── main.py
├── clients.csv
├── invoices/
│ ├── invoice_john_2025-07-31.pdf
│ ├── invoice_mary_2025-07-31.pdf
│ └── invoice_jane_2025-07-31.pdf
├── screenshots/
│ └── email-invoice-sender-console.png
└── README.md

---

## 🛠️ How to Use

1. **Prepare your `.env` file** with your Gmail credentials:

EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

2. **Add your `clients.csv`** in the following format:

name,email,file
John,john@example.com,invoice_john.pdf
Mary,mary@example.com,invoice_mary.pdf
Jane,jane@example.com,invoice_jane.pdf

3. **Put all invoice files** in the `/invoices` folder.

4. **Run the script** using a Python environment like Replit or your local terminal:
python main.py
Check the console for a summary, and confirm email delivery in your Gmail “Sent” folder.

---

## Demo Screenshot

![Bulk Invoice Emailer Screenshot](screenshot.PNG)

---

📌 Notes

Make sure you enable 2-Step Verification in Gmail and use an App Password.

This project uses TLS over SMTP for secure transmission.

---

## 👤 Author

**Eric Mutisya**  
Python Developer & Web Automation Freelancer  
[View My GitHub Projects](https://github.com/Ek-Coder-Tech)

---

📄 License

This project is open-source and free to use under the MIT License.

---

## 📬 Contact

For freelance inquiries, please reach out via [Upwork Profile](https://www.upwork.com/freelancers/~012558bab6232e8e65)

