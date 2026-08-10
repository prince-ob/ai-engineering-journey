print("Princewill adventure")

adjective1: str = input("Enter an adjective: ")
animal: str = input("Enter an animal: ")
adjectives2: str = input("Enter another adjective: ")
noun1: str = input("Enter another noun: ")
verb: str = input("Enter a verb: ")
noun2: str = input("Enter one more noun: ")

story: str = f'''
Bob went to he zoo today. He saw a(n) {adjective1} {animal} jummping up and down in its tree.
He turned his back for two seconds, and whne he turned around again, the {adjective1} {animal} had 
transformed into a(n) {adjectives2} {noun1}! He couldn't belive his eyes, so he started to 
{verb} with his {noun2}. In the end, he woke up and realised it was all a dream.
'''

print('Result')
print(story)