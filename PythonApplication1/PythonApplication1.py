#Mykhailiv Ivan lab_3

def find_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                print(f"{numbers[i]} + {numbers[j]}")

   
numbers = [1, 2, 3, 4, 5, 5, 6, 7]   
find_pairs(numbers)
