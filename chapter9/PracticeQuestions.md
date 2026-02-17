#Practice Questions
1. What is the function that returns Regex objects?

Answer: re.compile()

2. Why are raw strings often used when creating Regex objects?

Answer: More times than not, there is a particular word or a set of characters you are looking for
when using regex.

3. What does the search() method return?

Answer: A Match object.

4. How do you get the actual strings that match the pattern from a Match object?

Answer: Use the .group() method.

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

Answer: Group 0 covers the entire regex, group 1 covers the first three digits and group 2 covers the next three digits, the 
dash separator and last four digits.

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match
actual parentheses and period characters?

Answer: You would place a \ before the parentheses and period to escape the specific meaning.

7. The findall() method returns a list of strings or a list of tuples of strings.
What makes it return one or the other?

Answer: If the regex has multiple groups, it returns a list of tuples of strings. 
Otherwise, it returns a list of strings.

8. What does the | character signify in regular expressions?

Answer: It means either or so that you can match a pattern even if another character is used in a string.

9. What two things does the ? character signify in regular expressions?

Answer: When used right after a group, it tells the program to return a lazy match. 
A lazy match means that if a smaller string and a larger string both satisfy the pattern,
the smaller string is returned. Otherwise, the ? specifies that the character before can return 0 or 1 times.
In other words, the character preceding is optional.

10. What is the difference between the + and * characters in regular expressions?

Answer: + denotes that the preceding character needs to be present one or more times. * means the preceding character
can appear 0 or more times. 

11. What is the difference between {3} and {3, 5} in regular expressions?

Answer: {3} means that the pattern must repeat exactly three times while {3, 5} means that the pattern
can repeat 3 to 5 times inclusive. 

12. What do the \d, \w and \s shorthand character classes signify in regular expressions?

Answer: \d -> digit, \w -> letter, digit or underscore, \s -> space, tab or newline character

13. What do the \D, \W and \S shorthand character classes signify in regular expressions?

Answer: \D -> nondigit, \W -> not a letter, digit or underscore, \S -> Any non space character

14. What is the difference between the .* and .*? regular expressions?

Answer: .* is greedy meaning it matches as many characters as possible while .*? is lazy which means it 
will complete a match with the lowest number of characters possible.

15. What is the character class syntax to match all numbers and lowercase letters?

Answer: [0-9a-z]

16. How do you make a regular expression case-insensitive?

Answer: re.compile(pattern, re.I)

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile?

Answer: Normally it matches any non-newline character and with re.DOTALL, it even matches a newline too.

18. If num_re = re.compile(r'\d+'), what will num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

Answer: 'X drummers, X pipers, five rings, X hens'

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

Answer: It allows you to write comments within the re.compile()'s first argument where you specify the regex.
Furthermore, it allows you to separate different components of the regex in each line.

