#!/usr/bin/node

const array = process.argv.slice(2);
if (array.length === 0 || array.length === 1) {
  console.log(0);
} else {
  const max = Math.max(...array);
  const index = array.indexOf(max);
  array.splice(index, 1);
  const max2 = Math.max(...array);
  console.log(max2);
}
