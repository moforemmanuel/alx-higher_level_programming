#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let star = '';
      for (let j = 0; j < this.width; j++) {
        star += 'X';
      }
      //or console.log('X'.repeat(this.width))
      console.log(star);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
