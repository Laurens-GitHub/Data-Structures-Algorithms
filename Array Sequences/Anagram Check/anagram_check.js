const anagram = (s1,s2)=> {

    let dic1 = {}
    let dic2 = {}

    for(const i in s1.replace(/ /g, '').toLowerCase()) {
        if
    }



}

const anagram2 = (s1,s2)=>{

    let dic1 = {}

    let string1 = s1.replace(/ /g, '').toLowerCase()
    let out1 = Object.values(string1)
    let string2 = s2.replace(/ /g, '').toLowerCase()
    let out2 = Object.values(string2)

    for(const i in out1) {
        if (!(out1[i] in dic1)) {
            dic1[out1[i]] = 1
        } else {
            dic1[out1[i]] += 1
        }

    }

    for(const i in out2) {
        if ((out2[i] in dic1)) {
            dic1[out1[i]] -= 1
        } else {
            return false
        }

    }
    return true
}

console.log(anagram2('GO go go','GOGO go'))

