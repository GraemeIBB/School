const calculateSum = (a) =>{
    let sum = 0;
    for (const x of a) {
        sum +=x;
    }
    return sum;
}

console.log(calculateSum([1,2,3,4,5]))
console.log(calculateSum([10,-5,7]))
