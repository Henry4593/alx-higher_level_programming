#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const finalList = list.map((num, element) => num * element);
console.log(finalList);
