#!/usr/bin/node
/*
Script that writes a string to a file.
*/

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
