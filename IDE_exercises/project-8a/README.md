# project-8a

Write a function named count_letters that takes as a parameter a string and returns a dictionary that tabulates how many of each letter is in that string.  The string can contain characters other than letters, but only the letters should be counted.  The string could even be the empty string (just "").  Lower-case and upper-case versions of a letter should be part of the same count.  The keys of the dictionary should be upper-case letters.  If a letter does not appear in the string, then it would not get added to the dictionary.  For example, if the string is
```
"AaBb"
```
then the dictionary that is returned should contain these key-value pairs:
```
{'A': 2, 'B': 2}
```

And no, we haven't covered the isalpha() funciton, so don't use it.

The file must be named: count_letters.py
