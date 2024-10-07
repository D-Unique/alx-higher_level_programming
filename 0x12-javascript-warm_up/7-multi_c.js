#!/usr/bin/node
cmd = Math.floor(process.argv[2])
if (isNaN(cmd) == false){
    while (cmd != 0){
        cmd--;
        console.log('c is fun');
};}else{
    console.log('Missing number of occurrences')
}
