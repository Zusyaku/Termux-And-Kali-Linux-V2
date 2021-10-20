sFTP is a simple and secure FTP server.<br/>
sFTP uses server side encryption to encrypt the file that is being sent.

### Responses
 *  0: Everything went well
 * -1: Something went wrong

### Simple example

Server side
```python
from sftp import sFTP 

ip = '127.0.0.1'
port = 8080 
file = r'C:\Users\Mohamed\Desktop\Phi\phi.py'

ftp = sFTP(ip, port)
resp = ftp.send(file)

if resp == 0:
	print('File sent')
else:
	print('Failed to send file')
```

Client side
```python
from sftp import sFTP 

ftp = sFTP('127.0.0.1', 8080)
resp = ftp.recv()

if resp == 0:
	print('File received')
else:
	print('Failed to receive file')
```

### Timeout
by default max time is set to 10 seconds, after 10 seconds without a connection the server closes.

Server side
```python
from sftp import sFTP 

ip = '127.0.0.1'
port = 8080 
file = r'C:\Users\Mohamed\Desktop\Phi\phi.py'

ftp = sFTP(ip, port, max_time=15)
resp = ftp.send(file)

if resp == 0:
	print('File sent')
else:
	print('Failed to send file')
```

Client side
```python
from sftp import sFTP 

ftp = sFTP('127.0.0.1', 8080)
resp = ftp.recv()

if resp == 0:
	print('File received')
else:
	print('Failed to receive file')
```

### Verbose
verbose option is used for displaying messages, by default is set to False.

Server side
```python
from sftp import sFTP 

ip = '127.0.0.1'
port = 8080 
file = r'C:\Users\Mohamed\Desktop\Phi\phi.py'

ftp = sFTP(ip, port, verbose=True)
resp = ftp.send(file)

if resp == 0:
	print('File sent')
else:
	print('Failed to send file')
```

Client side
```python
from sftp import sFTP 

ftp = sFTP('127.0.0.1', 8080, verbose=True)
resp = ftp.recv()

if resp == 0:
	print('File received')
else:
	print('Failed to receive file')
```

__Warning:__ Just like SSL/TLS, this FTP server is also not safe against MITM attacks
