#!/usr/bin/node
const episodeNUM = process.argv[2];
let request = require('request');
let URL = `https://swapi.co/api/films/${episodeNUM}`;
request(URL, function (
  error,
  response,
  body
) {
  if (error) console.log(error);
  console.log(JSON.parse(body)['title']);
});
