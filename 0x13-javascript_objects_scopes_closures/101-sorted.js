#!/usr/bin/node
let data = require('./101-data.js').dict;
let final = {};

Object.keys(data).forEach(function (key) {
  let value = data[key];
  if (value in final) {
    final[value].push(key);
  } else final[data[key]] = [key];
});

console.log(final);
