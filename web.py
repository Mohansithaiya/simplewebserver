from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
    <table align="center" border="2" cellspacing="2" cellpadding="5">
		<caption>LAPTOP CONFIGURATION</caption>
        <caption>Mohan S 212223240094</caption>
        <tr>
			<th>S.NO</th>
			<th>Description</th>
			<th>Specifications</th>
            
		</tr>
		<tr align="center">
			<td>1.</td>
			<td>Brand</td>
			<td>Lenovo</td>
		</tr>
		<tr align="center">
			<td>2.</td>
			<td>Model Name</td>
            <td>Thinkpad E15</td>
			
		</tr>
		<tr align="center">

			<td>3.</td>
			<td>Screen Size</td>
			<td>15.6 Inches</td>
		</tr>
        <tr align="center">

			<td>4.</td>
			<td>Hard Disk Size</td>
			<td>512 GB</td>
		</tr>
        <tr align="center">

			<td>5.</td>
			<td>CPU Model</td>
			<td>Core i5</td>
		</tr>
        <tr align="center">
            <td>6.</td>
			<td>RAM Memory</td>
			<td>16 GB</td>
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