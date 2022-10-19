#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  // console.log(response.body);
  console.log(
    JSON.parse(body).results.reduce((acc, movie) => {
      // console.log(movie.characters);
      if (
        movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')
      ) {
        return acc + 1;
      }
      return acc;
    }, 0)
  );
});
