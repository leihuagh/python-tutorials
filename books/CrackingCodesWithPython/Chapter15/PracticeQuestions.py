# Chapter 15 Practice Questions

# 1. What does 2 ** 5 evaluate to?
print(2 ** 5)

# 2. What does 6 ** 2 evaluate to?
print(6 ** 2)

# 3. What does the following code print?
for i in range(5):
    if i == 2:
        continue
    print(i)

# 4. Does the main() function of affineHacker.py get called if another program
#    runs import affineHacker?
# Hint: check page 204
import books.CrackingCodesWithPython.Chapter15.affineHacker  # Don't do this - imports should be at the top of the file.

books.CrackingCodesWithPython.Chapter15.affineHacker.hackAffine("Well, I can't figure out just two! So let's pretend you opened 200.")
