#!/usr/bin/node

exports.callMeMoby = (i, callBackFunction) => {
  for (let j = 0; j < i; j++) callBackFunction();
};
