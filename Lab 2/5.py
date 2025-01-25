#sets

thisset = {"apple", "banana", "cherry", True, 1, 2}

thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)