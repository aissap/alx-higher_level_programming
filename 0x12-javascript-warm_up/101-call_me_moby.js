#!/usr/bin/node

function callMeMoby(x, Function) {
  for (let i = 0; i < x; i++) {
    Function();
  }
}

module.exports.callMeMoby = callMeMoby;
