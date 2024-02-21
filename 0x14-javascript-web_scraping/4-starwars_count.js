#!/usr/bin/node

/* Star Wars Films Count: Prints the number of movies where character
"Wedge Antilles" appears. Uses the Star Wars API.
*/
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const filmsWithAntilles = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(filmsWithAntilles.length);
  } else {
    console.error('Error:', error || `Status code ${response.statusCode}`);
  }
});
