# imported smtplib which was created to create an SMTP client session object
# this can be then used to send mail via Python
import smtplib, ssl

# port used for SSL 
port = 465 

# Creates a secure SSL context
context = ssl.create_default_context()

sender_email = "elliotece4436@gmail.com" # the address from which the email is sent from 
receiver_email = "elliotece4436@gmail.com" # the address from which the email is sent to 

message = """\
Subject: Hello! 

I love computer networks!""" # indicates the message sent from the sender to the recipient
# the 'Subject' portion of the message indicates the subject title of the email 

# combining the defined variables to send the necessary information for an email
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("elliotece4436@gmail.com", "ece4436!") # indicates the email address and password required to login 
    server.sendmail(sender_email, receiver_email, message) # indicates the sender's email, receiver's email and the message to be communicated
  