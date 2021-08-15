class LNode {
  data: number;
  next: LNode | null = null;
  constructor(data: number){
    this.data = data;
  }
}

const nodeA: LNode = new LNode(1);
const nodeB: LNode = new LNode(14);
const nodeC: LNode = new LNode(4);

nodeA.next = nodeB;
nodeB.next = nodeC;

console.log(nodeA.next.next?.data);

interface iLinkedlist {
  head: LNode  | null;
  length: number;
  size(): number;
}

class LinkedList implements iLinkedlist {
  head: LNode;
  length: number = 0;
  constructor() {
    this.head = null;
  }

  size() {
    return this.length;
  };

  isEmpty() {
    return this.length === 0;
  };

  add(element: number): void {
    const newNode = new LNode(element);
    if(this.head === null) {
      this.head = newNode;
    } else {
      let currentNode = this.head;
      while(currentNode.next){
        currentNode  = currentNode.next;
      }
  
          currentNode.next = newNode;
    }
    this.length++;
  }

  remove(element: number){
    let currentNode = this.head;
    let previousNode: LNode;
    if(currentNode.data === element){
      this.head = currentNode.next;
    } else {
        while(currentNode.data !== element) {
            previousNode = currentNode;
            currentNode = currentNode.next;
        }

        previousNode.next = currentNode.next;
    }

    length --;
  };

  indexOf(element: number) {
    let currentNode = this.head;
    let index = -1;

    while(currentNode){
        index++;
        if(currentNode.data === element){
            return index;
        }
        currentNode = currentNode.next;
    }

    return -1;
  };

  elementAt(index: number) {
    let currentNode = this.head;
    let count = 0;
    while (count < index){
        count ++;
        currentNode = currentNode.next
    }
    return currentNode.data;
  };
  
  
  addAt(index: number, element: number){
    let node = new LNode(element);

    let currentNode = this.head;
    let previousNode: LNode;
    let currentIndex = 0;

    if(index > length){
        return false;
    }

    if(index === 0){
        node.next = currentNode;
        this.head = node;
    } else {
        while(currentIndex < index){
            currentIndex++;
            previousNode = currentNode;
            currentNode = currentNode.next;
        }
        node.next = currentNode;
        previousNode.next = node;
    }
    length++;
  }
  
  removeAt(index: number) {
    let currentNode = this.head;
    let previousNode: LNode;
    let currentIndex = 0;
    if (index < 0 || index >= length){
        return null
    }
    if(index === 0){
        this.head = currentNode.next;
    } else {
        while(currentIndex < index) {
            currentIndex ++;
            previousNode = currentNode;
            currentNode = currentNode.next;
        }
        previousNode.next = currentNode.next
    }
    length--;
    return currentNode.data;
  }
}

