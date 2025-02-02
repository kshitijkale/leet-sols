/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
    // brute force but with duplicates
/*
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int** result = NULL;  
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(sizeof(int) * numsSize * numsSize);  
    for(int i=0;i<numsSize;i++)
    {
        for(int j = i+1;j<numsSize;j++)
        {
            for(int k = j+1;k<numsSize;k++)
            {
                if(nums[i]+nums[j]+nums[k]==0)
                {
                int* triplet = (int*)malloc(sizeof(int) * 3);
                    triplet[0] = nums[i];
                    triplet[1] = nums[j];
                    triplet[2] = nums[k];

                    // Resize result array to hold the new triplet
                    result = (int**)realloc(result, sizeof(int*) * (*returnSize + 1));
                    result[*returnSize] = triplet;  // Store new triplet
                     (*returnColumnSizes)[*returnSize] = 3;
                    (*returnSize)++;  // Increment count of triplets
                }
            }
        }
    }
    return result;
}
*/
int compareInt(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int cap = 32;
    int **result = (int**)malloc(sizeof(int*) * cap);
    int *cols = (int*)malloc(sizeof(int) * cap);
    int *triplet;
    int sum, target, count;
    int i, left, right;

    qsort(nums, numsSize, sizeof(int), compareInt);

    count = 0;
    for (i = 0; i < numsSize - 2; i++) {
        // The array is sorted, there is no possible tripet when this happen.
        if (nums[i] > 0) {
            break;
        }
        // skip element with same value to avoid duplicate triplets.
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        target = 0 - nums[i];
        left = i + 1;
        right = numsSize - 1;
        while (left < right) {
            sum = nums[left] + nums[right];
            if (sum > target) {
                right--;
            } else if (sum < target) {
                left++;
            } else {
                triplet = (int*)malloc(sizeof(int) * 3);
                triplet[0] = nums[i];
                triplet[1] = nums[left];
                triplet[2] = nums[right];

                result[count] = triplet;
                cols[count] = 3;
                count++;

                if (count == cap) {
                    cap *= 2;
                    result = (int**)realloc(result, sizeof(int*) * cap);
                    cols = (int*)realloc(cols, sizeof(int) * cap);
                }

                left++;
                right--;

                // skip element with same value to avoid duplicate triplets.
                while(left < right && nums[left] == nums[left - 1]) {
                    left++;
                }
                while(left < right && nums[right] == nums[right + 1]) {
                    right--;
                }
            }
        }
    }
    *returnSize = count;
    *returnColumnSizes = cols;

    return result;

}