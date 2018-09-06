#!/usr/bin/node
const URL = process.argv[2];
let request = require('request');

request(URL, function (error, response, body) {
  if (error) console.log(error);

  let b = JSON.parse(body)['results'];
  let finalCount = 0;

  for (let i = 0; i < b.length; i++) {
    for (let j = 0; j < b[i]['characters'].length; j++) {
      if (b[i]['characters'][j] === 'https://swapi.co/api/people/18/') { finalCount += 1; }
    }
  }
  console.log(finalCount);
});
