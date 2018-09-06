#!/usr/bin/node
var fs = require("fs");
var file = process.argv[2];
var text = process.argv[3];

fs.writeFile(file, text, "utf-8", function(err) {
  if (err) console.log(err);
});
