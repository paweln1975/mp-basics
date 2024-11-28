set_test = set()

# the method add does not return anything
set_test.add("Test")
checkTest = False
if "Test" in set_test:
    checkTest = True
print(f"After adding to set {checkTest}")
