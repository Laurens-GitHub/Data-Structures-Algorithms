const largestSum = (arr) =>{

    let sums = new Array

    for (i = 0; i < arr.length; i++) {
        for (j = arr.length; j !== i; j-- ) {
            sums.push(arr.slice(i,j).reduce)
        };
    };
    return sums;
};

console.log(largestSum([1,2,-1,3,4,10,10,-10,-1]))