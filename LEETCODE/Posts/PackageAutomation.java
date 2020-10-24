/*
Leetcode: Amazon OA packaging automation

Attempts:1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(nlogn)
Space Complexity: O(1)

Pattern: Array Traversal
Technique: Sort then check if out of bounds

Problems Encountered:
Other Solutions: there may be a O(n) solution

*/

import java.util.Arrays;

// import java.util.ArrayList;
// import java.util.Arrays;

/** Hello */
public class PackageAutomation {

    public static void main(String[] args) {
        int[] groups = { 5, 2, 3, 7, 1, 2, 2 };
        int z = packageAutomation(5, groups);
    }

    public static int packageAutomation(int numGroups, int[] arr) {
        Arrays.sort(arr);
        if (arr[0] > 1) {
            arr[0] = 1;
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > (arr[i - 1] + 1)) {
                arr[i] = arr[i - 1] + 1;
            }
        }
        System.out.println(arr[arr.length - 1]);
        return 1;

    }

}
