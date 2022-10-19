#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(argv[0], 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
