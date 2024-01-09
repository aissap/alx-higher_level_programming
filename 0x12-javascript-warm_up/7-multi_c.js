#!/usr/bin/node

const num_cc = parseInt(process.argv[2]);

if (isNaN(num_cc) || num_cc <= 0) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < num_cc; i++) {
		console.log('C is fun');
	}
}
