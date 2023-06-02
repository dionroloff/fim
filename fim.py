import os
import time
import smtplib
from email.mime.text import MIMEText

# Set the file path and email settings
file_path = '/path/to/file'
email_user = 'your_email@example.com'
email_password = 'your_email_password'
email_recipient = 'recipient_email@example.com'

# Initialize the previous modification time
prev_mod_time = os.path.getmtime(file_path)

while True:
  # Check the current modification time
  curr_mod_time = os.path.getmtime(file_path)

  # If the modification time has changed, send an email alert
  if curr_mod_time != prev_mod_time:
    msg = MIMEText('The file at {} has changed.'.format(file_path))
    msg['Subject'] = 'File Change Alert'
    msg['From'] = email_user
    msg['To'] = email_recipient

    # Connect to the email server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_recipient, msg.as_string())
    server.quit()

    # Update the previous modification time
    prev_mod_time = curr_mod_time

  # Sleep for a minute before checking again
  time.sleep(60)
