class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  let curNode1 = l1;
  let curNode2 = l2;
  let sumNode: ListNode;
  let sNNode: ListNode;
  let sPNode: ListNode;
  let sum: number;
  let rem: number = 0;
  let whe = 0;
  while (curNode1 !== null) {
    sum = curNode1.val + (curNode2?.val || 0);
    console.log(whe)
    if (whe === 0 && sum > 9) {
      sNNode = new ListNode(Math.floor(sum / 10));
      sum = sum - rem * 10;
      sumNode = new ListNode(sum);
      sumNode.next = sNNode;
    } else if (whe === 0) {
      sumNode = new ListNode(sum);
    } else if (sum > 9) {
      rem = Math.floor(sum / 10);
      sum = sum - rem * 10;
      sumNode.val = sumNode.val + rem;
      rem = 0;
      sPNode = new ListNode(sum);
      sPNode.next = sumNode;
      sumNode = sPNode;
    } else {
      sPNode = new ListNode(sum);
      sPNode.next = sumNode;
      sumNode = sPNode;
    }
    curNode1 = curNode1.next;
    curNode2 = curNode2.next;
    whe++;
  }
  return sumNode;
}

function addTwoNumbers1(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  let sumNode: ListNode = new ListNode();
  let cur = sumNode;
  let carry: number = 0;

  while (l1 || l2 || carry) {
    let v1 = l1 ? l1.val : 0; 
    let v2 = l2 ? l2.val : 0;

    let val = v1 + v2 + carry;
    carry = Math.floor(val/10 % 10);
    val = val % 10;
    cur.next = new ListNode(val);

    cur = cur.next
    l1 = l1?.next ?? null;
    l2 = l2?.next ?? null;
  }
  return sumNode.next;
}

function addTwoNumbers3(
  l1: ListNode | null,
  l2: ListNode | null,
   x: number = 0,
): ListNode | null {
  if (!l1 && !l2 && x==0) return null
  
  let tmp = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + x;
  x = Math.floor(tmp/10)
  tmp %= 10
  
  return new ListNode(tmp, addTwoNumbers3(l1 ? l1.next : null, l2 ? l2.next : null, x))
}

const L1 = new ListNode(2);
const L12 = new ListNode(4);
const L13 = new ListNode(3);

L1.next = L12;
L12.next = L13;

const L2 = new ListNode(5);
const L22 = new ListNode(6);
const L23 = new ListNode(4);

L2.next = L22;
L22.next = L23;

const sum = addTwoNumbers(L1, L2);

console.log(sum.val);

