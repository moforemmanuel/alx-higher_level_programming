#!/usr/bin/node

module.exports = {
  addMeMaybe: function (number, theFunction) {
    number++;
    theFunction(number);
    //or return theFunction(number + 1);
  }
};
