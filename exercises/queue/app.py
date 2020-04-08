from tasks import add

print("Basic call to add(3,4): ", add(3,4))

print("Call add(3,6) with delay: ", add.delay(3,6))

result = add.delay(34,5)
print("Call add(34,5) with delay with backend to get result: ", result.get())
