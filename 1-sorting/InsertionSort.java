class InsertionSort {
    // Insertion sort runs at worst and average case time of O(n^2) with space O(1)
    void insertionSort(int[] array) {
        // start at index 1
        for (int i = 1; i < array.length; i++) {
            // take the element
            int element = array[i];
            // look back one index
            int j = i - 1;

            // while j is inbounds and the element at j is larger than element
            while (j >= 0 && element > array[j]) { // to reverse, flip > to <
                // move the element back one space
                array[j + 1] = array[j];
                // and look back one more index
                --j;
            }
            // when we exit the loop, place the element
            array[j + 1] = element;

        }
    }

    public static void main(String[] args) {
        InsertionSort is = new InsertionSort();
        int[] array = { 4, 1, 6, 32, 654 };
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
        System.out.println('\n');
        is.insertionSort(array);
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
}
