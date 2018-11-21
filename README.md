# Teoria da computação - Expressões Regulares

## RegEx


### \d Matches any decimal digit; this is equivalent to the class [0-9].

### \D Matches any non-digit character; this is equivalent to the class [^0-9].

### \s Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

### \S Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

### \w Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

### \W Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
### These sequences can be included inside a character class. For example, [\s,.] 
###  is a character class that will match any whitespace character, or ',' or '.'.

##  reference https://docs.python.org/3.4/howto/regex.html