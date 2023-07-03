vgames = ["halo", "mgs", "ac", "mass effect", "forza"]

print(sorted(vgames))

vgames.reverse()
print(vgames)

vgames.reverse()
print(vgames)

vgames.sort()
print(vgames)

vgames.sort(reverse=True)
print(vgames)

halo = vgames.pop(2)
print(f"Sorry, but {halo} will be deleted immediately.")

print(vgames)

del vgames[3]
print(vgames)

vgames.append("smb3")
print(vgames)

baseball = "smb3"
vgames.remove(baseball)
print(f"Sorry, but {baseball.upper()} will be deleted immediately.")

print(vgames)

vgames.insert(3, "league")

print(vgames)

print(vgames[-3])