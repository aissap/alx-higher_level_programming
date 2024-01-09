#!/usr/bin/node

const numoccurrences = parseInt(process.argv[2]);

if (isNaN(numoccurrences) || numoccurrences <= 0) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < numoccurrences; i++) {
		console.log('C is fun');
	}
}
