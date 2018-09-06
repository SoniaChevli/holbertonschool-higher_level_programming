#!/usr/bin/node
var request = require('request');
var fs = require('fs');
var finalStorage = process.argv[3];
var URL = process.argv[2];

request(URL, function (error, response, body) {}).pipe(
  fs.createWriteStream(finalStorage)
);
