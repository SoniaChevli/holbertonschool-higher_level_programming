#!/usr/bin/node
let request = require('request');
let URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) console.log(error);
  console.log('code:', response.statusCode);
});
