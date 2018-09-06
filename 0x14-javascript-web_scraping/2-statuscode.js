#!/usr/bin/node
var request = require('request');
var URL = process.argv[2];

request(URL, function (error, response, body) {
  console.log('code:', response.statusCode);
});
