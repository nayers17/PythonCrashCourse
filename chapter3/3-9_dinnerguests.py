invites = ['evan', 'tristan', 'meow']

print(f"Hi {invites[0].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"Hi {invites[1].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"Hi {invites[2].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")

friendwhocantgo = invites.pop(0)

print(friendwhocantgo.title())
print(f"\nMy dear friend {friendwhocantgo.title()} is unable to attend because he has a preexisting arrangement scheduled with his significant other.")



invites.insert(0, 'trident')
print(invites)

print(f"\nHi {invites[0].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"Hi {invites[1].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"Hi {invites[2].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")

print(f"\n Hey, {invites[0].title()}, {invites[1].title()}, {invites[2].title()}, I found a bigger table!")

invites.insert(0, 'kai')
invites.insert(2, 'Jausho')
invites.append('Dark')

print(invites)

print(f"\nHi {invites[0].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"\nHi {invites[1].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"\nHi {invites[2].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"\nHi {invites[3].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"\nHi {invites[4].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")
print(f"\nHi {invites[5].title()}, \nI'm inviting you out to dinner with me tonight. I hope you can make it!\n")

print(f"Hey, {invites[0].title()}, {invites[1].title()}, {invites[2].title()}, {invites[3].title()}, {invites[4].title()}, {invites[5].title()}- I can only invite two people for dinner.")

Dark = invites.pop()
Meow = invites.pop()
Tristan = invites.pop()
Jausho = invites.pop()

print(invites)
print(len(invites))

print(f"\nhey {Dark.title()}, I'm sorry but our table shrunk and we don't have room for you.")
print(f"\nhey {Meow.title()}, I'm sorry but our table shrunk and we don't have room for you.")
print(f"\nhey {Tristan.title()}, I'm sorry but our table shrunk and we don't have room for you.")
print(f"\nhey {Jausho.title()}, I'm sorry but our table shrunk and we don't have room for you.")
print(f"\nHey {invites[0].title()}, Our table shrunk by 4, but you're still invited!")
print(f"\nHey {invites[1].title()}, Our table shrunk by 4, but you're still invited!")


del invites[0]
del invites[0]
print(invites)

complete = '3.4-3.7: Complete!'
print(complete)