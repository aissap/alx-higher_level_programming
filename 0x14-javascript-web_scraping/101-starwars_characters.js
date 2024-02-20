#!/usr/bin/node

// Print all characters of a Star Wars movie in the same order as the list "characters" in the /films/ response

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    let count = 0;

    const printCharacter = () => {
      if (count < characters.length) {
        request(characters[count], (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            count++;
            printCharacter();
          } else {
            console.error('Error:', error || `Status code ${response.statusCode}`);
          }
        });
      }
    };

    printCharacter();
  } else {
    console.error('Error:', error || `Status code ${response.statusCode}`);
  }
});
