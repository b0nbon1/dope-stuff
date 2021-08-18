package algorithmsDataStructures.algorithms.sorting.SelectionSort;

/*
* The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
* The algorithm maintains two subarrays in a given array.
* 1) The subarray which is already sorted.
* 2) Remaining subarray which is unsorted.
* In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

* arr[] = 64 25 12 22 11
* // Find the minimum element in arr[0...4]
* // and place it at beginning
* 11 25 12 22 64
* // Find the minimum element in arr[1...4]
* // and place it at beginning of arr[1...4]
* 11 12 25 22 64
* // Find the minimum element in arr[2...4]
* // and place it at beginning of arr[2...4]
* 11 12 22 25 64
*
* // Find the minimum element in arr[3...4]
* // and place it at beginning of arr[3...4]
* 11 12 22 25 64
* O(n^2) - time complexity
* O(1) - space complexity
* */
public class SelectionSort {
    void selectionSort(int arr[]) {
        int n = arr.length;
        for(int i = 0; i < n; i++) {
            int min_idx = i;
            for (int k = i+1; k < n; k++) {
                if (arr[k] < arr[min_idx])
                    min_idx = k;
                int temp = arr[min_idx];
                arr[min_idx] = arr[i];
                arr[i] = temp;
            }
        }
    }
}
