def horner_hash(key, base, mod):
    hash_value = 0
    for char in key:
        hash_value = (hash_value * base + ord(char)) % mod
    return hash_value

# Example usage
key = "example"
base = 31
mod = 100000007
index = horner_hash(key, base, mod)
print("Hash index:", index)
