#!/usr/bin/node

function factorial (i, total = 1) {
  i > 1 ? factorial(i - 1, total * i) : console.log(total);
}

factorial(parseInt(process.argv[2]));
