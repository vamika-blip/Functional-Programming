#set1(4q)
#Q1-A number is stored as a string "25". Write a program to convert it to an integer, add 10 to it, and print the result along with its final data type.
number="25"
number2= int(number)
print(number2+10, type(number2))

#Q2-Let word="Data". Print word*3, and add a comment explaining what the * operator does when used with a string and a number.
word="data"
print(word*3)
print(2*3)
#ANS2-when used with a string, * operator prints the string itself "n" no. of times as in "word*n" whereas when used with a number it acts as a multiplication operator as in suppose 2*3=6

#Q3-Let lst=[1,2,3] and lst2=lst(NOT a copy). Do lst2.append(4) and print both lst and lst2- explain in a comment why BOTH lists changed
lst1=[1,2,3]
lst2=lst1
lst2.append(4)
print(lst1)
print(lst2)
#ANS3-in the above case both lists changed as lst2 was not a copy of list 1, the same list was now associated with two storage variables lst1 and lst2 therefore when we appended the list 2, both the lists changed.

#Q4-Let s={1,2,2,3,3,3}. Print s and print len(s)- add a comment explaining what happened to the duplicate values.
s={1,2,2,3,3,3}
print(s)
print(len(s))
#ANS4- Duplicate values are not taken into consideration instead only face values are saved, even the len function does not count duplicates rather only count a particular element once
