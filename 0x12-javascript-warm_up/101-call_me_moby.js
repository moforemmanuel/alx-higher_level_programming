#!/usr/bin/node

module.exports = {
  callMeMoby: function (x, f) {
    for (let i = 0; i < x; i++) {
      f();
    }
  }
};
