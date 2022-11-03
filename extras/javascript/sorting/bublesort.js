/**
 * 
 * @param {int} arr 
 * swap the elements by comparing to each multiple rounds while checking if swapping happened, if it didn't means they're sorted
 */
function bubbleSort(arr) {
  let swapped;
  do {
    swapped = false
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swapped = true
      }
    }
  } while (swapped);

}

const arr = [8, 20, -2, 4, -6];
bubbleSort(arr)
console.log(arr)
