#!/usr/bin/node
//console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);

const cmd = process.argv;

if (cmd[2] == undefined){
    console.log('No argument')
}
else{
    console.log(cmd[2])
}
