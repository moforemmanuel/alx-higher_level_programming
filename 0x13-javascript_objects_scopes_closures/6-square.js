#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square extends Square {
  charPrint (c) {
    this.char = c;
  }
};
