#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(argv[0], function (error) {
  if (error) console.log(error);
});
