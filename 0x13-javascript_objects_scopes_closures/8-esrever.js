#!/usr/bin/node
exports.esrever = function (list) {
  let final = [];
  while (list.length) {
    final.push(list.pop());
  }
  return final;
};
