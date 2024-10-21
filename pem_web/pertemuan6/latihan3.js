// Control Flow
// if else
let age = 20;
if (age >= 20){
    console.log("you're eligible");
} else {
    console.log("you're not eligible");
}
// ternary operator
let vote =
    age >= 20 ? "you're eligible to vote" : "you're not eligible to vote";
console.log(vote);

let hours = new Date().getHours();
console.log(hours);
let discount = hours <= 1 ? "20%" 
                : hours >= 3 ? "15%"
                : "0%";
console.log(discount);

let day = new Date().getDay();
switch (day) {
    case 0:
        console.log("sunday");
        break;
    case 1:
        console.log("monday");
        break;
    case 2:
        console.log("tuesday");
        break;
    case 3:
        console.log("wednesday");
        break;
    case 4:
        console.log("thrusday");
        break;
    case 5:
        console.log("friday");
        break;
    case 6:
        console.log("saturdayday");
        break;
}