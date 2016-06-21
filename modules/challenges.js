var express = require('express');
var router = express.Router();
var fs = require('fs');

function read_json_file(){
	var file = '../data/challenges.json';
	return fs.readFileSync(file);
}

exports.list = function(){return JSON.parse(read_json_file());}


