/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let final_sum = init
    for(let i=0;i<nums.length;i++){
        final_sum = fn(final_sum,nums[i])
    }
    return final_sum
};