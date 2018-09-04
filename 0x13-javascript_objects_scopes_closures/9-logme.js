#!/usr/bin/node
var funcCalls = 0;

exports.logMe = function (item) {
  console.log(`${funcCalls}:${item}`);
  funcCalls++;
};
