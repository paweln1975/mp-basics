import hashlib

print(sorted(hashlib.algorithms_guaranteed))
print(sorted(hashlib.algorithms_available))

message = "This is custom message to generate a hash"
original_hash = hashlib.sha256(message.encode('utf8'))
print(original_hash.hexdigest())

message2 = "This is custom message to generate a hash"
new_hash = hashlib.sha256(message2.encode('utf8'))
print(new_hash.hexdigest())

print(original_hash.hexdigest() == new_hash.hexdigest())
