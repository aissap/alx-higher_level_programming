#!/usr/bin/node
const data = require('./100-data').list;

const map1 = data.map((value, index) => value * index);

console.log(data);
console.log(map1);
