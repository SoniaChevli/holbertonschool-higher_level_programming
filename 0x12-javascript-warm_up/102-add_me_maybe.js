#!/usr/bin/node
exports.addMeMaybe = (i, callBackFunction) => {
  i = i + 1;
  callBackFunction(i);
};
