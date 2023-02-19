import hashlib as hl

print("^Hashing tool^ ~ By Twister_Froste ~ Hash type (SHA-1)", end='\n\n')

root_object = input("Enter a password to get a hash: ")

hash_object = hl.sha1(f'{root_object}'.encode())
pbHash = hash_object.hexdigest()

print("", end='\n\n')
print("#"*50, end='\n\n')
print(f"Hash code: {pbHash}")
