import hashlib
 
hash_object = hashlib.md5(b'Python Bootcamp')
print(hash_object.hexdigest())