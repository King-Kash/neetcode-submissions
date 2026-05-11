class Solution {
    public int search(int[] array, int target) {
        // int index = Arrays.binarySearch(nums, target);
        // if (index <= -1){
        //     return -1;
        // }
        // return index;

        int high = array.length - 1;
        int low = 0;
        while((high - low) >= 0){
            int middle = low + ((high - low) / 2);
            if(array[middle] == target){
                return middle;
            }
            else if(target > array[middle]){
                low = middle + 1;
            } else if(target < array[middle]){
                high = middle - 1;
            }
        }
        return -1; //default not found value.
    }
}
