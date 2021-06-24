# project-08b

Write a Python function called words_in_both that takes two strings as parameters and returns a result set of the words appeared in the two input strings. 
You can assume all characters are letters or spaces and capitalization shouldn't matter: "to" or "To" is counted as the same word.  
The words in the result set should be all in lowercase. 
For example, if one string contains "on", and the other string contains "ON", then the set should contain "on".

You can use Python's split() funciton. For example:
```
sentence = 'Not the comfy chair!'
print(sentence.split())
['Not', 'the', 'comfy', 'chair!']
```

Here's one simple example of how words_in_both() might be used:
```
common_words = words_in_both("She's a jack of all trades", 'Jack was tallest of all')
```

The file should be named: words_in_both.py
