#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }
  print () {
    for (let i = 0; i < h; i++) {
      let star = '';
      for (let j = 0; j < w; j++) {
        star += 'X';
      }
      console.log(star);
    }
  }
};
