#!/usr/bin/node
const URL = process.argv[2];
let request = require('request');

request(URL, function (error, response, body) {
  if (error) console.log(error);
  let b = JSON.parse(body);
  let final = {};
  for (let i = 0; i < b.length; i++) {
    let userID = b[i]['userId'];
    if (b[i]['completed'] === true) {
      if (!(userID in final)) {
        final[userID] = 1;
      } else {
        final[userID] = final[userID] + 1;
      }
    }
  }
  console.log(final);
});
