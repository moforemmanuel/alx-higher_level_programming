#!/usr/bin/node

const arr = process.argv.slice(2);
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  const array = arr.map(e => parseInt(e));
  const max = Math.max(...array);
  const index = array.indexOf(max);
  array.splice(index, 1);
  const max2 = Math.max(...array);
  console.log(max2);
}
