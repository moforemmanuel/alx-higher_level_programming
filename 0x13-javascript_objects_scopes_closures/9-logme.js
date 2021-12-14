#!/usr/bin/node

let count = 0;
exports.logme = function (data) {
  console.log(`${count}: ${data}`);
  count++;
};
