#!/usr/bin/node

function addMeMaybe(number, thefunction) {
  thefunction(number + 1);
}

module.exports.addMeMaybe = addMeMaybe;
