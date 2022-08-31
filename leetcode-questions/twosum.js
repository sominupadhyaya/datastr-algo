const twoSum = (nums, target) =>{
    for (let i = 0; i< nums.length; i++){
        for (let j = i; j<nums.length; j++){
            if(nums[i] + nums[j] === target){
                return [nums.indexOf(nums[i]) , nums.indexOf(nums[j])]
            }
        }
    }
}

console.log(twoSum([1,2,3,4] , 3))