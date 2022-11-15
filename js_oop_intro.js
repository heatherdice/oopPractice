//from https://www.youtube.com/watch?v=PFmuCDHHpwk
//object literal syntax - an issue if the object has behavior (methods)
// const circle = { //circle object
//     radius: 1, //property
//     location: { //property
//         x: 1,
//         y: 1
//     },
//     draw: function() { //method
//         console.log('draw');
//     }
// }
// circle.draw();

//factory function aka constructor function
function createCircle(radius) {
    return {
        radius,
        draw: function() {
            console.log('draw');
        }
    }
}
const circle = createCircle(1); //creates circle w/ radius 1

//constructor function
function Circle(radius) { //function, not class; NO CLASSES IN JS
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
    //return this happens automatically
}
const another = new Circle(1); 
//new: creates empty object {} and sets 'this' to point to that object
//without new: makes object global ('Window')

//in JS, functions are objects
Circle.call({}, 1) 
//calls a function; {} specifies target of 'this', num calls on num of arguments
Circle.apply({}, [1,2,3])
//can call function, but instead of explicitly passing all arguments, pass arr
//useful if you already have an arr in your function
