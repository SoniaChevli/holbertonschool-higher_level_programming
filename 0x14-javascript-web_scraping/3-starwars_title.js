#!/usr/bin/node
const episodeNUM = process.argv[2];
var request = require('request');
console.log('EPI', episodeNUM);
request(`https://swapi.co/api/films/${episodeNUM}`, function (
  error,
  response,
  body
) {
  if (error) console.log(error);
  console.log(JSON.parse(body)['title']);
});
