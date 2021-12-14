#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.export = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
