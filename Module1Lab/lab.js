var username = window.prompt("Please enter you name");
var greetingParagraph = document.getElementById("greeting"); //here we are storing the access to the paragraph
greetingParagraph.innerHTML += ", " + username;
var num1 = parseInt(window.prompt("Please enter a number"));
var num2 = parseInt(window.prompt("Please enter another number"));
var operand1 = document.getElementById("operand1");
var operand2 = document.getElementById("operand2");
operand1.innerHTML += num1;
operand2.innerHTML += num2;

var sum = num1 + num2;
var difference = num1 - num2;
var product = num1 * num2;
var quotient = num1 / num2;
var modulus = num1 % num2;
document.getElementById("addition").innerHTML = "The sum of " + num1 + " and " + num2 + " is " + sum;
document.getElementById("substraction").innerHTML = "The difference between " + num1 + " and " + num2 + " is " 
+ difference;
document.getElementById("multiplication").innerHTML = "The product between " + num1 + " and " + num2 + " is " + product;
document.getElementById("division").innerHTML = "The quotient between " + num1 + " and " + num2 + " is " + quotient;
document.getElementById("modulus").innerHTML = "The modulus between " + num1 + " and " + num2 + " is " + modulus;
