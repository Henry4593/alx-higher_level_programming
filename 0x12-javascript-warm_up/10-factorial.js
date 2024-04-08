#!/usr/bin/node
const factNumber = process.argv[2];

function factorial (factNumber) {
  if (factNumber <= 1 || isNaN(factNumber)) {
    return 1;
  } else {
    return factNumber * factorial(factNumber - 1);
  }
}

console.log(factorial(factNumber));
