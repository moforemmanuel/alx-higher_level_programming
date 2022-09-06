#!/usr/bin/node

const num = process.argv[2];
const toInt = parseInt(num);
if (isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${toInt}`);
}
