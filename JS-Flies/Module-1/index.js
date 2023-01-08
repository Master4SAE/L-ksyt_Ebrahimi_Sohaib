'use strict';
console.log("I'am printing to console!")

const name = prompt("whats your name user?");
const greeting = `Hello ${name}`;
document.querySelector("#greeting").innerHTML= greeting