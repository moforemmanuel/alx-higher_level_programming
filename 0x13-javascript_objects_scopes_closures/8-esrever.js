#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (const item of list) {
    rev.unshift(item);
  }
  return rev;
};
