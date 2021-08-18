package algorithmsDataStructures.algorithms.sorting.QuickSort;

public class QuickSort {
    void quickSort(int arr[], int low, int high) {
        if(low < high) {
            int p = partition(arr, low, high);
            quickSort(arr, low, p - 1);
            quickSort(arr, p + 1, high);
        }
    }

    /*
    This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot
   */
    /*'
    * arr[] = {10, 80, 30, 90, 40, 50, 70}
    * Indexes:  0   1   2   3   4   5   6
    *
    * low = 0, high =  6, pivot = arr[h] = 70
    * Initialize index of smaller element, i = -1
    *
    * Traverse elements from j = low to high-1
    * j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
    * i = 0
    * arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j
    *                                      // are same
    *
    * j = 1 : Since arr[j] > pivot, do nothing
    * // No change in i and arr[]
    *
    * j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
    * i = 1
    * arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30
    *
    * j = 3 : Since arr[j] > pivot, do nothing
    * // No change in i and arr[]
    *
    * j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
    * i = 2
    * arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
    * j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j]
    * i = 3
    * arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped
    *
    * We come out of loop because j is now equal to high-1.
    * Finally we place pivot at correct position by swapping
    * arr[i+1] and arr[high] (or pivot)
    * arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped
    *
    * Now 70 is at its correct place. All elements smaller than
    * 70 are before it and all elements greater than 70 are after
    * it.
    *
    * O(n^2)
    * */
    int partition(int arr[], int low, int high) {
        // pivot (Element to be placed at right position)
        int pivot = arr[high];

        // Index of smaller element and indicates the
        // right position of pivot found so far
        int i = low - 1;

        for(int k = low; k <= high -1; k++) {
            // If current element is smaller than the pivot
            if(arr[k] < pivot) {
                i++; // increment index of smaller element
                swap(arr, i, k);
            }
        }
        swap(arr, i+1, high);
        return i + 1;
    }

    void swap (int arr[], int i, int k) {
        int temp = arr[i];
        arr[i] = arr[k];
        arr[k] = temp;
    }
}
