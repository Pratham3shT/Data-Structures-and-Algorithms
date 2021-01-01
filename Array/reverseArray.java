// Program to reverse an array of integers

package Array;

public class reverseArray {

    static void reverseArr(int[] arr, int start, int end) {

        int temp;

        while (start < end) {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    static void printArray(int[] arr, int size) {
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5,6};
        System.out.print("Entered array is: ");
        printArray(arr, 6);
        reverseArr(arr, 0, 5);
        System.out.print("Reversed array is: ");
        printArray(arr, 6);
    }
}

/* 
Output: 

Entered string is: 1 2 3 4 5 6
Reversed string is: 6 5 4 3 2 1
*/
