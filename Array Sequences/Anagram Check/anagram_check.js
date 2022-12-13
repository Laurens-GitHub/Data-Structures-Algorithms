function anagram(s1, s2) {

    const p1 = s1.replace(/ /g, "").toLowerCase()
    const p2 = s2.replace(/ /g, "").toLowerCase()

    let dic1 = {}
    let dic2 = {}

    for(let char in p1) {
        if (!(p1[char] in dic1)) {
            
        } else {
            dic1.p1 += 1
        };
    };
    return dic1
};

console.log(anagram('Go go go','GOGO ge'));
