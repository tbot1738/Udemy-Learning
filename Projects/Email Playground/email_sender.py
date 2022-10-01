import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tbot'
email['to'] = 'brrrrrr@gmail.com'
email['subject'] = 'Six mahine ruk ja meri body banane waali hai'

email.set_content("I am python master boii!!")

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("tbot1738@gmail.com", "TBOt1738")
    smtp.send_message(email)
    print("All good bozo!")