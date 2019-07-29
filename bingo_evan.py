# Quick and dirty bingo song.

# This line splits the word 'bingo' up into an array of letters, ['b', 'i', 'n', 'g', 'o']
word_list = list("bingo")
name_o = "".join(word_list)
common_phrase = "There was a farmer who had a dog and " + name_o + " was his name-o"

# First time through just print the hardcoded song
print(common_phrase)
# Loop through the spelling three times
for j in range(3):
  # By joining the array with a hyphen
  print("-".join(word_list))

# Initialze our index variable at -1
i = -1
# While index is less than word_list length minus 1 (because of indexing purposes)
while i < len(word_list) - 1:
  # Print the song
  print("\n" + common_phrase)
  # Increment our index variable
  i = i+1
  # Replace that index of the array with an exclamation point
  word_list[i] = "!"
  # Print the spelling three times
  for j in range(3):
    print("-".join(word_list))


"""
Final Output:

There was a farmer who had a dog and bingo was his name-o
b-i-n-g-o
b-i-n-g-o
b-i-n-g-o

There was a farmer who had a dog and bingo was his name-o
!-i-n-g-o
!-i-n-g-o
!-i-n-g-o

There was a farmer who had a dog and bingo was his name-o
!-!-n-g-o
!-!-n-g-o
!-!-n-g-o

There was a farmer who had a dog and bingo was his name-o
!-!-!-g-o
!-!-!-g-o
!-!-!-g-o

There was a farmer who had a dog and bingo was his name-o
!-!-!-!-o
!-!-!-!-o
!-!-!-!-o

There was a farmer who had a dog and bingo was his name-o
!-!-!-!-!
!-!-!-!-!
!-!-!-!-!
"""