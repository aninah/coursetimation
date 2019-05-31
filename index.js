/*     ----- SETTING UP DEPENDENCIES -----     */
	// setting up server
	var http = require('http'); 
	var express = require('express');
	var app = express();
	var server = http.createServer(app); 
	// add socket.io
	var io = require('socket.io').listen(server);
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
	app.use(express.static('public'))
	app.use('/static', express.static('public'))