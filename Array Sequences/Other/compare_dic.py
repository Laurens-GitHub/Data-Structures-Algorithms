
# function compare_obj(obj1, obj2) {

#   let result = {}
#   for (i = 0; i < obj1.length; i++){
#     if (obj1[i] != obj2[i]){
#       result += obj2[i]
#       }
#   }
# }
# // make an empty object
# // look inside object1
# // for each item in object1, look at the corresponding item in object2
# // if these are equivalent, move on
# // if they are not, add the differences to our object
# // return the result object

def compare_dict(dic1, dic2):
    results = {}

    return recurse_dic(dic1, dic2, results)

def recurse_dic(dic1, dic2, results):

    for i in dic1.keys():
        # print(dic1[i], dic2[i])
        if dic1[i] != dic2[i]:
            # print("access", dic[i])
            if isinstance(dic1[i], dict):
                # print("reach nested dictionary")
                recurse_dic(dic1[i], dic2[i], results)
                #pass new value as dictionary
            else:
                # print("adding to result", i, dic2[i])
                results[i] = dic2[i]
                # print(results)

    return results

# /* expected output
# {
#   'person.name': 'bar',
#   'person.address.zip': 20022
# }
# */

object1 = {
  "person": {
    "name": 'foo',
    "age": 12,
    "address": {
      "street": '123w 18th',
      "zip": 10011
    }
  }
}

object2 = {
  "person": {
    "name": "bar",
    "age": 12,
    "address": {
      "street": "123w 18th",
      "zip": 20022
    }
  }
}

print(compare_dict(object1, object2))

