#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ', response && response.statusCode);
});
