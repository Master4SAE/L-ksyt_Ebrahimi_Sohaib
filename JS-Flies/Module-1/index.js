'use strict';
console.log("I'am printing to console!")

const name = prompt("whats your name user?");
const greeting = `Hello ${name}`;
document.querySelector("#greeting").innerHTML= greeting

const num1 = prompt("give me number");
const num2 = prompt("give me number");
const num3 = prompt("give me number");
const numOne = parseInt(num1);
const numTwo = parseInt(num2);
const numRd = parseInt(num3);
const sum = numOne + numTwo + numRd;

document.querySelector("#sum").innerHTML= "The sum of numbers are" + sum;

const average = (numOne + numTwo + numRd) / 3;

document.querySelector("#avre").innerHTML= "The the average of numbers are" + average;

const product = (numOne * numTwo * numRd);

document.querySelector("#task-3").innerHTML= "The product of numbers are" + product;


