package algorithmsDataStructures.algorithms.sorting.BubbleSort;

/*
* First Pass:
* ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
* ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
* ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
* ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
* Second Pass:
* ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
* ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
* ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
* ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
* Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
* Third Pass:
* ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
* ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
* ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
* ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
* O(n^2) - time complexity
* O(1) - space complexity
* */
public class BubbleSort {
    public void bubbleSort(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int k = 0; k < n-i-1; k++)
                if (arr[k] > arr[k+1])
                {
                    // swap arr[j+1] and arr[j]
                    int temp = arr[k];
                    arr[k] = arr[k+1];
                    arr[k+1] = temp;
                }
    }
}
