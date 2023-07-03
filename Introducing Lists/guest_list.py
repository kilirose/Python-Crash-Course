guest_list = ["Cole", "Sam", "Dario", "Tanner"]
print(f"Hello {guest_list[0].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[3].title()}, you are invited to my dinner.")

cant_attend = guest_list.pop()
print(f"\n{cant_attend.title()} will not be able to attend.")

guest_list.append("Ethan")
print(f"\nHello {guest_list[0].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[3].title()}, you are invited to my dinner.")

print("\nHello everyone, a larger table has been reserved and we are now able to invite more guests.")
guest_list.insert(0, "Robato")
guest_list.insert(3, "Clyde")
guest_list.insert(6, "Rune")

print(f"\nHello {guest_list[0].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[3].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[4].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[5].title()}, you are invited to my dinner.")
print(f"Hello {guest_list[6].title()}, you are invited to my dinner.")

print("\nDue to unforeseen circumstances, only two people will be able to attend the dinner.")
cole_gone = guest_list.pop(1)
print(f"Sorry {cole_gone}, you cannot attend.")

sam_gone = guest_list.pop(1)
print(f"Sorry {sam_gone}, you cannot attend.")

dario_gone = guest_list.pop(2)
print(f"Sorry {dario_gone}, you cannot attend.")

ethan_gone = guest_list.pop(2)
print(f"Sorry {ethan_gone}, you cannot attend.")

rune_gone = guest_list.pop(2)
print(f"Sorry {rune_gone}, you cannot attend.")

print(f"\nHello {guest_list[0].title()}, you are still invited to my dinner.")
print(f"Hello {guest_list[1].title()}, you are still invited to my dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)

print(len(guest_list))
