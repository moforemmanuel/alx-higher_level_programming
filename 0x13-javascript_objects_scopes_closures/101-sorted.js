#!/usr/bin/node

const dict = require('./101-data').dict;
const sorted = {};

Object.keys(dict).forEach(key => {
  if (sorted[dict[key]] === undefined) sorted[dict[key]] = [];
  sorted[dict[key]].push(key);
});
console.log(sorted);
