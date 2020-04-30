# Our Mad Lib
madlib = "On the {} trip to {}, my {} friend and I decided to invent a game. Since this would be a rather {} trip, it would need to be a game with {} and {}. Using our {} to {}, we tried to get the {} next to us to play too, but they just {}ed at us and {} away. After a few rounds, we thought the game could use some {}, so we turned on the {} and started {} to the {} that came on. This lasted for {} before I got {} and decided to {}. I'll never {} that trip, it was the {} road trip of my {}."
sourceURL = "http://marcelkupka.cz/wp-content/uploads/2013/03/mad.jpg"

# A list storing the blanks for the Mad Lib
blanks = ['adjective', 'place', 'adjective', 'adjective', 'noun, plural', 'noun, plural', 'noun', 'verb', 'noun', 'verb', 'action verb', 'noun, plural', 'noun', 'action that ends with -ing', 'noun', 'measure of time', 'adjective', 'action verb', 'verb', 'adjective', 'noun, something that you own']

# Ask the user for each one
print("Road Trip Mad Lib\nWhen the program asks you, please enter the appropriate word.")
print("There are {} blanks in this Mad Lib. ".format(len(blanks)))

fs = []
for word in blanks:
    ans = input(word.capitalize() + "> ")
    if len(ans) == 0:
        print("Please don't leave anything blank. It kills the experience.")
        quit()
    fs.append(ans)

if __name__ == '__main__':
    # Print the formatted Mad Lib
    print(madlib.format(*fs))
    feedback = input("Pretty funny, right? [y/n] ")
    if feedback == "y":
        print("Thanks!")
    else:
        print(":( Sorry. I'll try better next time.")
    print("\n" + "=" * 10 + "\nMad Lib sourced from " + sourceURL)
