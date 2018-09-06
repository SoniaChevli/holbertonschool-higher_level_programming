#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let text = process.argv[3];

fs.writeFile(file, text, 'utf-8', function (err) {
  if (err) console.log(err);
});
