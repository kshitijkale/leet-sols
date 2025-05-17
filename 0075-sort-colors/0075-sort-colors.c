void swap(int* a, int* b) {
    // Check if pointers are valid and not NULL (minimal check)
    if (a == NULL || b == NULL) {
        return; // Or handle error appropriately
    }
    // Correctly swap the integer values pointed to by a and b
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to sort an array containing only 0s, 1s, and 2s
// using the Dutch National Flag algorithm.
void sortColors(int* nums, int numsSize) {
    // Handle edge cases: array is NULL or has 0 or 1 element
    if (nums == NULL || numsSize < 2) {
        return;
    }

    int low = 0;       // Pointer for the next position of a 0
    int high = numsSize - 1; // Pointer for the next position of a 2
    int mid = 0;       // Pointer for the current element being considered (Corrected initialization)
    // Removed: int*A = nums; // Unnecessary

    // Iterate through the array with the 'mid' pointer
    // The loop continues as long as 'mid' is within the unsorted portion
    // defined by 'high'. (Corrected loop condition)
    while (mid <= high) {
        // Use if-else if-else for minimal change from original structure
        if (nums[mid] == 0) {
            // If the current element is 0:
            // Swap it with the element at 'low'.
            // Increment both 'low' and 'mid'.
            swap(&nums[low], &nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 2) {
            // If the current element is 2:
            // Swap it with the element at 'high'.
            // Decrement 'high'.
            // DO NOT increment 'mid' here, because the element
            // that was swapped into nums[mid] needs to be checked.
            swap(&nums[mid], &nums[high]);
            high--;
        } else { // nums[mid] must be 1
            // If the current element is 1:
            // It's already in its correct relative position.
            // Just move the 'mid' pointer forward.
            mid++;
        }
    }
}

/*
// Example Usage (for testing):
int main() {
    int colors1[] = {2, 0, 2, 1, 1, 0};
    int n1 = sizeof(colors1) / sizeof(colors1[0]);
    sortColors(colors1, n1);
    printf("Sorted colors1: ");
    for (int i = 0; i < n1; i++) {
        printf("%d ", colors1[i]);
    }
    printf("\n"); // Expected output: 0 0 1 1 2 2

    int colors2[] = {2, 0, 1};
    int n2 = sizeof(colors2) / sizeof(colors2[0]);
    sortColors(colors2, n2);
    printf("Sorted colors2: ");
    for (int i = 0; i < n2; i++) {
        printf("%d ", colors2[i]);
    }
    printf("\n"); // Expected output: 0 1 2

    int colors3[] = {0, 0, 0};
    int n3 = sizeof(colors3) / sizeof(colors3[0]);
    sortColors(colors3, n3);
    printf("Sorted colors3: ");
    for (int i = 0; i < n3; i++) {
        printf("%d ", colors3[i]);
    }
    printf("\n"); // Expected output: 0 0 0

    int colors4[] = {1};
    int n4 = sizeof(colors4) / sizeof(colors4[0]);
    sortColors(colors4, n4);
    printf("Sorted colors4: ");
    for (int i = 0; i < n4; i++) {
        printf("%d ", colors4[i]);
    }
    printf("\n"); // Expected output: 1

    return 0;
}
*/
