#!/usr/bin/node
//const num = Math.floor(Number(process.argv[2]));
//console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
const count = process.argv[2];

if (isNaN(count) == true){
    console.log('Not a number')
}
else{
    console.log('My number: %s', count)
};
w