#Print the type of cach of these values: 5, 5.0, "5", True, 5+2j, [5], (5,), (5) and {5: 5). Present the output as one line per value.
values = [
    5,
    5.0,
    "5",
    True,
    5+2j,
    [5],
    (5,),
    (5),
    {5: 5}
]

for val in values:
    print(type(val))

#Let raw = " Mumbai, Pune, Nagpur ". Remove the extra spaces, split it into a list of cities and print the list along with the number of cities.
raw= " Mumbai, Pune, Nagpur "
raw= raw.strip()
cities= raw.split(", ")
print(cities)
print(len(cities))

#Using a for loop, print a table of n, n squared and n cubed for n= 1 to 8, with a header row and right-aligned columns.
print(f"{'n':>8} {'n^2':>8} {'n^3':>8}")
print("-" * 26)
for n in range(1, 9):
    print(f"{n:>8} {n**2:>8} {n**3:>8}")

#Predict the output of: def show: y = 5 followed by printy) inside it, then calling show and afterwards print(y) outside the function. Run it, fix the error, and add a comment explaining the scope rule responsible.
def show():
  y= 5
  print(y)
 
show()
print(y)

#the code shows NameError: name 'y' is not defined..this is because y is only defined under the show function i.e its local scope..outside the show() function in the global scope y is not defined therefore we get a name error

def show():
  y= 5
  print(y)
 
show()
