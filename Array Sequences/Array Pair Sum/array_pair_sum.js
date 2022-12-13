const pairSum = (arr, k) => {
    if (arr.length < 2) {
        throw "Array must have a minimum of 2 integers";
    };

    let answer = new Set();

    for(i=0; i < arr.length; i++) {
        for(j=i+1; j < arr.length; j++) {
            if ((arr[i])+(arr[j]) === k) {
                answer.add([Math.max(arr[i], arr[j]), Math.min(arr[i], arr[j])])
            };
        };
    };
    console.log(answer)
    return answer.size // use "size" for Sets, not "length"
};

// console.log(pairSum([1,3,2,2],4)) // ([1,3], [2,2])

const pairSum2 = (arr, k) => {

    let pairs = new Set()

    for (const i in arr) {
        target = k-arr[i]
        if (arr[i] in arr & target in arr) {
            pairs.add([Math.max(target, arr[i]), Math.min(target, arr[i])])
        };
    };

    console.log(pairs)
    return pairs.size;

};

console.log(pairSum2([1,3,2,2],4)) // ([1,3], [2,2])
