#!/usr/bin/node

// Print all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
    movieData.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Error:', error || `Status code ${response.statusCode}`);
        }
      });
    });
  } else {
    console.error('Error:', error || `Status code ${response.statusCode}`);
  }
});
