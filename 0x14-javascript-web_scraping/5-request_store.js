#!/usr/bin/node
// Stream webpage content to a file
const fs = require('fs');
const request = require('request');

// Streaming the HTTP response to the specified file
request(process.argv[2])
  .on('error', err => console.error(err))
  .pipe(fs.createWriteStream(process.argv[3]));
