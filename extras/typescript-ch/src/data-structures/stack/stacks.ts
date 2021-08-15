/* Stacks! */

// functions: push, pop, peek, length

const letters: string[] = []; // this is our stack

const word: string= "racecar";

let rword: string = "";

// put letters of word into stack
for (let i = 0; i < word.length; i++) {
    letters.push(word[i]);
}

// pop off the stack in reverse order
for (let i=0; i < word.length; i++) {
    rword += letters.pop();
}

if (rword === word) {
    console.log(word + " is a palindrome");
}
else {
    console.log(word + " is not a palindrome");
}

class Stack  {
  count: number;
  storage: any;
  constructor() {
    this.count = 0;
    this.storage = {};
  }

    // Adds a value onto the end of the stack
    push (value) {
        this.storage[this.count] = value;
        this.count++;
    }

    // Removes and returns the value at the value at the end of the stack
    pop() {
        if (this.count === 0) {
            return undefined;
        }

        this.count--;
        var result = this.storage[this.count];
        delete this.storage[this.count];
        return result;
    }

    size() {
        return this.count;
    }

    // Returns the value at the end of the stack
    peek() {
        return this.storage[this.count-1];
    }
}

var myStack = new Stack();

myStack.push(1);
myStack.push(2);
console.log(myStack.peek());
console.log(myStack.pop());
console.log(myStack.peek());
