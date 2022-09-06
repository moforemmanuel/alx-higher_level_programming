#!/usr/bin/node

const num = process.argv[2];
const x = parseInt(num);

if (isNaN(x)) {
  console.log('Mising number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
