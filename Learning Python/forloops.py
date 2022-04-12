test_number_array = [1, 3, 5, 7, 9]

for i in test_number_array:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ")




a = ["Jim", "Bob", "Soundwave"]
for i in a:
    print(a.pop(1))


friends = ["Jim", "Bob", "King Kong"]

for i in range(len(friends)):
    print(friends[i])




for i in range(5):
    if i == 0:
        print("First Iteration")
    else:
        print("Not first iteration")