#!/usr/bin/node

exports.esrever = function (list) {
  const listReversed = [];
  for (let x = list.length - 1; x >= 0; x--) {
    listReversed.push(list[x]);
  }
  return (listReversed);
};
