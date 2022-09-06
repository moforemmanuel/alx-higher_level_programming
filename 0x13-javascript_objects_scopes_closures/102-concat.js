#!/usr/bin/node

const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];
/*
const data1 = FileReader.readAsText(src1);
const data2 = FileReader.readAsText(src2);
const data = data1.concat(`\n${data2}`);
*/

const fs = require('fs');

function callback (err, data) {
  if (err) {
    console.log(err);
  }
  fs.appendFile(dest, data, function (err) {
    if (err) console.log(err);
  });
}

fs.readFile(src1, 'utf-8', callback);
fs.readFile(src2, 'utf-8', callback);
