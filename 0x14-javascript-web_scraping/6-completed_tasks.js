#!/usr/bin/node
const URL = process.argv[2];
var request = require("request");

request(URL, function(error, response, body) {
  if (error) console.log(error);
  var b = JSON.parse(body);
  var final = {};
  for (let i = 0; i < b.length; i++) {
    var userID = b[i]["userId"];
    if (b[i]["completed"] === true) {
      if (!(userID in final)) {
        final[userID] = 1;
      } else {
        final[userID] = final[userID] + 1;
      }
    }
  }
  console.log(final);
});
