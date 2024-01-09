#!/usr/bin/node

function callMeMoby(x, thefnctn) {
  for (let i = 0; i < x; i++) {
    thefnctn();
  }
}

module.exports.callMeMoby = callMeMoby;
