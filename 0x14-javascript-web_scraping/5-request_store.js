#!/usr/bin/node
let request = require('request');
let fs = require('fs');
let finalStorage = process.argv[3];
let URL = process.argv[2];

request(URL, function (error, response, body) {}).pipe(
  fs.createWriteStream(finalStorage)
);
