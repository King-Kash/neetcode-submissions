class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        System.out.println("Break");
        int high = matrix.length - 1;
        int low = 0;
        while((high - low) >= 1){
            int middle = low + (high - low) / 2;
            if (matrix[middle][0] == target){
                return true;
            }
            else if(target > matrix[middle][0]){
                low = middle + 1;
            }
            else if (target < matrix[middle][0]){
                high = middle - 1;
            }
        }
        int row_index = low + (high - low) / 2;
        int result = Arrays.binarySearch(matrix[row_index], target);
        System.out.println(row_index);
        System.out.println(result);
        if (result > -1){
            return true;
        } else {
            return false;
        }
    }
}
