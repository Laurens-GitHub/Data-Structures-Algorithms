function factorial(n) {

    if (n === 0) {
        console.log("BASE CASE HAS BEEN MET! n=",n);
        return 1;
    } else {
        console.log('Recursive case triggered. n=',n);
        return n * factorial(n-1);
    }
};

console.log(factorial(5));
