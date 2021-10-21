from socket import *
import ssl # Implemented to create a secure Secure Sockets Layer connection between client and server
import base64 # Encoding used to convert bytes that have binary or text data into ASCII characters

# Messages that will be sent to the recipient email
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end
# Used the Google mail server, hence "smtp.gmail.com"
# Used the Transport Layer Security protocol, hence using 587
mailserver = ("smtp.gmail.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM) # clientSocket variable now (AF_NET, SOCK_STREAM) establishes a socket in the Internet domain. This is configured using the default TCP protocol
clientSocket.connect(mailserver) # clientSocket connects to the mailserver variable created earlier, which is connected to the GMail server and uses TLS

#Fill in end

recv = clientSocket.recv(1024).decode() #the recv function, part of Python's socket module, can be used to receive data from both TCP and UDP sockets. In this case, TCP.
print(recv) # prints recv value, which shows a reply is received from server
if recv[:3] != '220': # prints when the recv value is not as expected or not received
    print('220 reply not received from server.')


# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode()) # sending HELO command to the server
recv1 = clientSocket.recv(1024).decode() 
print(recv1) # prints recv1 value, which shows a reply is received from server
if recv1[:3] != '250': # prints when the recv1 value is not as expected or not received
    print('250 reply not received from server.')

# Sending TLS command and printing server response. 
Tls = 'STARTTLS\r\n' # StartTLS informs the email server that the email client wants to upgrade to a secure connection, and is a type of protocol command
clientSocket.send(Tls.encode()) # sending TLS command
recvTLS = clientSocket.recv(1024) 
print (recvTLS) # prints recvTLS value, which shows a reply is received from server
if recvTLS[:3] != '220': # prints when the recvTLS value is not as expected or not received
	print('250 reply not received from server')


# Encrypt the socket using SSLv23 and creating this sslSocket
sslSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n' # used to authorize login into account using the stated username and login
sslSocket.send(authCommand.encode()) # sending AUTH LOGIN command
auth_recv = sslSocket.read(1024)
print (auth_recv) # prints auth_recv value, which shows a reply is received from server
if auth_recv[:3] != '334': # prints when the auth_recv value is not as expected or not received
	print ('334 reply not received from server')

# # Send username and print server response.
username = "elliotece4436@gmail.com"
username = username.encode('utf-8') # encoding using UTF-8, one of the most commonly used and Python oftenly default to this
sslSocket.send(base64.b64encode(username) + '\r\n'.encode('utf-8')) # sending provided username 
username_recv = sslSocket.read(1024)
print (username_recv) # prints username_recv server response

# # Send password and print server response.
password = 'ece4436!'
password = password.encode('utf-8') # encoding using UTF-8, one of the most commonly used and Python oftenly default to this
sslSocket.send(base64.b64encode(password) + '\r\n'.encode('utf-8')) # sending provided password
password_recv = sslSocket.read(1024)
print (password_recv) # prints password_recv server response

# Send MAIL FROM command and print server response.
 
# Fill in start

mailFromCommand = "MAIL FROM:<elliotece4436@gmail.com>\r\n" # indicates who is the sender of the mail
sslSocket.send(mailFromCommand.encode()) # sends the MAIL FROM command to the server
recv2 = sslSocket.recv(1024).decode()
print ("MAIL FROM Server Response:" + recv2) # prints recv2 value, which shows a reply is received from server
if recv2[:3] != '250': # prints when the recv2 value is not as expected or not received
	print ('250 reply not received from server.')


# Fill in end

# Send RCPT TO command and print server response.

# Fill in start

rcptToCommand = "RCPT TO:<elliotece4436@gmail.com>\r\n" # indicates who is the recipient of the mail
sslSocket.send(rcptToCommand.encode()) # sends the RCPT TO command to the server 
recv3 = sslSocket.recv(1024).decode()
print (recv3) # prints recv3 value, which shows a reply is received from server
if recv3[:3] != '250': # prints when the recv3 value is not as expected or not received
	print ('250 reply not received from server.')


# Fill in end

# Send DATA command and print server response.

# Fill in start

dataCommand = 'DATA\r\n' 
sslSocket.send(dataCommand.encode()) # sends the DATA command to the server
recv4 = sslSocket.recv(1024).decode()
print (recv4) # prints recv4 value, which shows a reply is received from server
if recv4[:3] != '354': # prints when the recv4 value is not as expected or not received
	print ('354 reply not received from server.')


# Fill in end


# Send message data.

# Fill in start

sslSocket.send(msg.encode()) # sends the message of 'I love computer networks' indicated at the top of the code


# Fill in end

# Message ends with a single period.

# Fill in start

sslSocket.send(endmsg.encode()) # sends the endmsg which contains just one period
recv5 = sslSocket.recv(1024).decode()
print (recv5) # prints recv5 value, which shows a reply is received from server
if recv5[:3] != '250': # prints when the recv5 value is not as expected or not received
	print ('250 reply not received from server.')

# Fill in end

# Send QUIT command and get server response.

# Fill in start

quitCommand = 'QUIT\r\n' # indicates quit
sslSocket.send(quitCommand.encode()) # sends the QUIT command to the server
recv6 = sslSocket.recv(1024).decode()
print (recv6) # prints recv6 value, which shows a reply is received from server
if recv6[:3] != '221': # prints when the recv6 value is not as expected or not received
	print ('221 reply not received from server.')


# Fill in end

clientSocket.close() # closes the clientSocket after the program is run through 