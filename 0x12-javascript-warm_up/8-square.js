#!/usr/bin/node
const sizeOfSquare = process.argv[2];
if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < sizeOfSquare; x++) {
    console.log('X'.repeat(sizeOfSquare));
  }
}
