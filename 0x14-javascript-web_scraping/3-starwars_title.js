#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie where the episode
number matches a given integer.
*/

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
