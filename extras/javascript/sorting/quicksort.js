function quicksort(arr) {
  let pivot = arr[arr.length-1]
  let left = []
  let right = []
  for(let i = 0; i < arr.length -1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i])
    } else {
      right.push(arr[i])
    }
  }
  return [...quicksort(left), pivot, ...quicksort(right)]
}

const arr = [-6,20,8,-2,4]
