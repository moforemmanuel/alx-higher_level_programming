#!/usr/bin/node

const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  charPrint (c) {
    this.print(c);
  }
};
