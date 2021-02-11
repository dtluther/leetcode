// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    const pairs = {};
    let count = 0;
    
    let i = 0;
    while (i < nums.length) {
        num = nums[i];
        // console.log(num, pairs);
        // console.log(`count: ${count}`)
        if (num in pairs) {
            arr = pairs[num]
            if (arr.length > 1) {
                arr.shift();
            } else {
                delete pairs[num] // delete the key in object if there is only one occurrence
            }
            count += 1;
        } else {
            if (k - num in pairs) {
                pairs[k - num].push(i)
            } else {
                pairs[k - num] = [i];
            }
        }
        i += 1;
    }
    
    return count;
};
