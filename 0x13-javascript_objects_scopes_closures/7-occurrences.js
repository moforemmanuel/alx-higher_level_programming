#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(e => {
    count = e === searchElement ? count + 1 : count;
  });
  return count;
};
