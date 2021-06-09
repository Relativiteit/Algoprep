# Arrays basics

# create an array containing car names:
cars = ["Lexus", "Honda", "Toyota"]
print(cars)

# get value of the first array item:
x = cars[0]
print(x)

# modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

#Return the number of elements in the cars array:
x = len(cars)
print(x)

# looping array elements, printing each itemen in the cars array:
for i in cars:
    print(i)

# .append("string") adding array elemnts add one more elemtn tot he carss array:
cars.append("Suzuki")
print(cars)

# .pop(integer) removing array elements 
cars.pop(0)
print(cars)

# .remove delete the element that has the value "string"
cars.remove("Suzuki")
print(cars)

