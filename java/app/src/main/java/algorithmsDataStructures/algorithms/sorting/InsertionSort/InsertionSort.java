package algorithmsDataStructures.algorithms.sorting.InsertionSort;

/*
* To sort an array of size n in ascending order: 
* 1: Iterate from arr[1] to arr[n] over the array.
* 2: Compare the current element (key) to its predecessor.
* 3: If the key element is smaller than its predecessor, compare it to the elements before.
*    Move the greater elements one position up to make space for the swapped element.
* CHECK example: image in this folder.
*
* O(n^2) - time complexity
* Auxiliary Space: O(1)
* */
public class InsertionSort {
    void sort(int arr[])
    {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            /* Move elements of arr[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
}
