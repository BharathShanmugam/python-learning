# import imaplib
# import email
# from email.header import decode_header
from dotenv import load_dotenv,find_dotenv,dotenv_values
load_dotenv()

import imaplib

import os


def reload_specific_env(file_path='.env'):
    # Load the .env variables into a dictionary
    new_env = dotenv_values(file_path)

    # Update specific environment variables
    for key, value in new_env.items():
        os.environ[key] = value

# Initial load
reload_specific_env()

PASSWORD=os.getenv("PASSWORD")
EMAIL=os.getenv("EMAIL")


print(PASSWORD)
print(EMAIL)

# Account credentials
username = EMAIL
password = PASSWORD
imap_server = "imap.gmail.com"  # Example for Gmail

# # Connect to the IMAP server
# mail = imaplib.IMAP4_SSL(imap_server)

# # Log in to the account
# mail.login(username, password)

# # Select the mailbox you want to read (inbox here)
# mail.select("inbox")

# # Search for all emails
# status, messages = mail.search(None, "ALL")

# # Convert the result to a list of email IDs
# email_ids = messages[0].split()

# # Iterate over each email
# for e_id in email_ids:
#     # Fetch the email by ID
#     status, msg_data = mail.fetch(e_id, "(RFC822)")

#     # Get the email content
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             msg = email.message_from_bytes(response_part[1])
#             subject, encoding = decode_header(msg["Subject"])[0]
#             if isinstance(subject, bytes):
#                 subject = subject.decode(encoding if encoding else 'utf-8')

#             from_ = msg.get("From")
#             print(f"Subject: {subject}, From: {from_}")

#             # If the email message is multipart
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     # Extract the email body
#                     if part.get_content_type() == "text/plain":
#                         body = part.get_payload(decode=True).decode()
#                         print(f"Body: {body}")
#             else:
#                 # If it's a simple email
#                 body = msg.get_payload(decode=True).decode()
#                 print(f"Body: {body}")

# # Close the connection
# mail.logout()



import imaplib
import email
from email.header import decode_header


imap_server = "imap.gmail.com"  # Example for Gmail

try:
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server)

    # Log in to the account
    mail.login(username, password)

    # Select the mailbox you want to read (inbox here)
    mail.select("inbox")

    # Search for all emails
    status, messages = mail.search(None, "ALL")

    # Convert the result to a list of email IDs
    email_ids = messages[0].split()

    # Iterate over each email
    for e_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(e_id, "(RFC822)")

        # Get the email content
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Get the subject and decode it if necessary
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')

                # Get the "From" email address
                from_ = msg.get("From")

                # Print subject and from email
                print(f"Subject: {subject}")
                print(f"From: {from_}\n")

    # Close the connection
    mail.logout()

except imaplib.IMAP4.error as e:
    print(f"An error occurred: {e}")
