#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  console.log('code: ', response && response.statusCode);
});
