# LeetCode 706. 

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""

class MyHashMap:

    def __init__(self):
        self.BUCKET_SIZE = 1000
        self.buckets = [[] for _ in range(self.BUCKET_SIZE)]  # bucket[i] stores a list of (key, value)

    def getBucket(self, key):
        return self.buckets[key % self.BUCKET_SIZE]

    def findIndexOfKey(self, bucket, key):
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex != -1:
            bucket[nodeIndex][1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex == -1: return -1
        return bucket[nodeIndex][1]

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex == -1: return
        del bucket[nodeIndex]
			
