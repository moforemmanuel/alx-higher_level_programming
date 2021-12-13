#!/usr/bin/node

const num = process.argv[2];
const x = parseInt(num);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let star = '';
    for (let j = 0; j < x; j++) {
      star += 'X';
    }
    console.log(star);
  }
}
