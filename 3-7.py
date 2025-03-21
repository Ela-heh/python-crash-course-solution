'''Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.'''
guests = ['bestie','uncle','sister']
guests.insert(0,"Mom")
guests.insert(1,'dad')
guests.append('Mohammad')
print( f"\n {guests} sorry I can only invite 2 people" )
popped = guests.pop()
print (f"sorry my dear {popped} that i couldn't invite u")
popped = guests.pop()
print (f"sorry my dear {popped} that i couldn't invite u")
popped = guests.pop()
print (f"sorry my dear {popped} that i couldn't invite u")
popped = guests.pop()
print (f"sorry my dear {popped} that i couldn't invite u")
print (f"{guests}, u are still invited")
del guests [0]
del guests [0]
print (guests)