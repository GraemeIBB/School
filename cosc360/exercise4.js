const population = [67,83,25,38,126];

for (let num in population) {
    console.log("Population: " + num + " million")
}

let sum = 0;
for (let x in population) {
    avg += x;
}

avg = sum/population.length();

console.log("Total population: " + sum + " million");
console.log("Average population: "+ avg + " million");


let arr = [];
for (let x in population) {
    if (x > 50) arr.push(x);
}

