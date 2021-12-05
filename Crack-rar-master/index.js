#!/usr/bin/node
//Coded by AnonyminHack5 
//imports modules i need
var http = require("http")
var fs = require("fs")

//Read File system
fs.readFile('index.html', function (err, data) {
	if (err) {
		return console.error(err);
	}
});

var data = fs.readFileSync('index.html');

//creates the HTTP Server
http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.end(data.toString());
}).listen(8081);

//prints the server it is running on
console.log("\x1b[1;94m Server Started:\x1b[0m Visit http://127.0.0.1:8081 on your browser");