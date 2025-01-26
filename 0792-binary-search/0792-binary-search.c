int search(int* nums, int numsSize, int target) {
    int l = 0;
    int h = numsSize - 1;  // Corrected to numsSize - 1
    while (l <= h) {
        int m = l + (h - l) / 2;  // Safer midpoint calculation
        if (nums[m] == target) {
            return m;  // Target found
        } else if (nums[m] < target) {
            l = m + 1;  // Search the right half
        } else {
            h = m - 1;  // Search the left half
        }
    }
    return -1;  // Target not found
}