#!/usr/bin/node

/* Star Wars Films Count: Prints the number of movies where character
"Wedge Antilles" appears. Uses the Star Wars API.
*/

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    const wedgeAntillesFilms = films.reduce((count, film) => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
        ? count + 1
        : count;
    }, 0);
    console.log(wedgeAntillesFilms);
  }
});