# EX01 Developing a Simple Webserver
## Date:26/02/24

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
    <table align="center" border="2" cellspacing="2" cellpadding="5">
		<caption>TOP FIVE COMPANIES:</caption>
        <tr>
			<th>S.NO</th>
			<th>COMPANY NAME</th>
			<th>COUNTRY</th>
            <th>Year OF Foundation</th>
		</tr>
		<tr align="center">
			<td>1.</td>
			<td>Microsoft</td>
			<td>USA</td>
            <td>1975</td>
		</tr>
		<tr align="center">
			<td>2.</td>
			<td>Apple</td>
			<td>USA</td>
            <td>1976</td>
			
		
		</tr>
		<tr align="center">

			<td>3.</td>
			<td>Alphabet</td>
			<td>USA</td>
            <td>2015</td>
		</tr>
        <tr align="center">

			<td>4.</td>
			<td>Amazon</td>
			<td>USA</td>
            <td>1994</td>
		</tr>
        <tr align="center">

			<td>5.</td>
			<td>Nvidia</td>
			<td>USA</td>
            <td>1993</td>
		</tr>

	</table>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2024-03-15 092331.png>)
![alt text](<Screenshot 2024-03-15 092348.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
