import json
import os

class HashSet:

    def __init__(self):
        self.capacity = 8 # capacity of the hash map 
        self.size = 0 # current size
        self.s = [None]*self.capacity # hash table
        self.limit = float(2)/3 # fraction of size after which rehashing is needed
        self.deleted = '==DELETED==' # deleted identifier

    def __get_hash__(self, key):
        return key%self.capacity

    def __resize_hash__(self):
        if(float(self.size)/self.capacity >= self.limit):
            self.capacity <<= 1
            new_s = [None]*self.capacity
            for i in range(self.capacity >> 2):
                if(self.s[i] != None and self.s[i] != self.deleted):
                    h = HashSet.__get_hash__(self, self.s[i])
                    while(new_s[h] is not None):
                        h = (5*h + 1)%self.capacity
                    new_s[h] = self.s[i]
            self.s = new_s

    def __contains__(self, key):
        h = HashSet.__get_hash__(self, key)
        iter_pass = 0
        while(self.s[h] != key):
            iter_pass += 1
            if(iter_pass > self.capacity):
                return -1
            h = (5*h + 1)%self.capacity
        return h


    def add(self, key: int) -> None:

        HashSet.__resize_hash__(self)       
        
        h = HashSet.__get_hash__(self, key)
        while(self.s[h] is not None):
            h = (5*h + 1)%self.capacity
        self.s[h] = key
        self.size += 1

    def remove(self, key: int) -> None:
        idx = HashSet.__contains__(self, key)
        if(idx >= 0):
            self.s[idx] = self.deleted
            self.size -= 1
        return

    def contains(self, key: int) -> bool:
        if(HashSet.__contains__(self, key) >= 0):
            return True
        return False

def test_hash_map(obj, args, expected):
    ans = []
    count = 0
    for idx, ops in enumerate(args[0]):
        if(ops == "contains"):
            ans.append(obj.contains(args[1][idx][0]))
        elif(ops == "add"):
            ans.append(obj.add(args[1][idx][0]))
        elif(ops == "remove"):
            ans.append(obj.remove(args[1][idx][0]))
        if(expected[idx+1] != ans[-1]):
            count += 1
        print(ops, args[1][idx][0], ans[-1], expected[idx+1])
    print(count)
    return ans        

f = open(os.getcwd() + "/test_cases/test_cases.json")           
all_data = json.load(f)
test_data = all_data["HashSet"]
for test in test_data:
    ans_obj = HashSet()
    ans_test = test_hash_map(ans_obj, [test_data[test]["input"][0], test_data[test]["input"][1]], test_data[test]["output"])
    print(ans_test == test_data[test]["output"])
ans_obj = HashSet()
ans_test = test_data(ans_obj, ["contains",
          "remove",
          "add",
          "add",
          "contains",
          "remove",
          "contains"] , [[72],
          [91],
          [48],
          [41],
          [96],
          [87],
          [48]])
# ans_obj = HashSet()
# ans_obj.add(48)
# ans_obj.add(49)
# ans_obj.add(50)
# ans_obj.add(51)
# ans_obj.add(52)
# ans_obj.remove(48)
# ans_obj.add(53)
# ans_obj.add(54)
# ans_obj.add(55)
# ans_obj.add(40)
# print(ans_obj.s)
'''
contains 40 False True
contains 48 False True
contains 53 False True
contains 19 False True
'''