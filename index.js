/*     ----- SETTING UP DEPENDENCIES -----     */
// setting up server
let http = require('http'); 
let express = require('express');
let app = express();
let server = http.createServer(app); 
// parsing forms
let bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
//setting up paths.
let path = require('path')
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('public'));
app.use('/static', express.static(path.join(__dirname, 'public')))
// using a database
let anyDB = require('any-db');
let conn = anyDB.createConnection('sqlite3://courses.db');

let calculations = require(path.join(__dirname,"/calculations.js"));

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