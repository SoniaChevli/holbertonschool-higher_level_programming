#!/usr/bin/node
let list = require('./100-data.js');
console.log(list.list);
let newList = list.list.map((v, i) => v * i);
console.log(newList);
