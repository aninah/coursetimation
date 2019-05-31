/*     ----- SETTING UP DEPENDENCIES -----     */
// setting up server
var http = require('http'); 
var express = require('express');
var app = express();
var server = http.createServer(app); 
// parsing forms
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
// using a database
var anyDB = require('any-db');
var conn = anyDB.createConnection('sqlite3://chatroom.db');
// templating.
var engines = require('consolidate');
app.engine('html', engines.hogan);
app.set('views', __dirname + '/templates'); 
app.set('view engine', 'html'); 
//setting up paths.
var path = require('path')
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('public'));
// app.use('/static', express.static('public'))
app.use('/static', express.static(path.join(__dirname, 'public')))



/*     ----- ROUTES -----     */

// gets static homepage.
app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname,'/public/home.html'));
});

// gets static about page.
app.get('/about', function(req, res) {
	res.sendFile(path.join(__dirname,'/public/about.html'));
});

app.post('/receive_classes', function(req, res) {
	console.log(req.body.class_str);
	res.send({concentrations: ["Computer Science", "Philosophy"]})
});


// handles pages that don't exist. 
app.get('*', function(req, res){
	res.status(404).send('404 error- this page doesn\'t exist uwu');
});



server.listen(8080);