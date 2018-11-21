# -*- coding: utf-8 -*-
import pandas as pd
import re

#  \d
# Matches any decimal digit; this is equivalent to the class [0-9].
# \D
# Matches any non-digit character; this is equivalent to the class [^0-9].
# \s
# Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
# \S
# Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \w
# Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# \W
# Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
# These sequences can be included inside a character class. For example, [\s,.] 
#is a character class that will match any whitespace character, or ',' or '.'.

# reference https://docs.python.org/3.4/howto/regex.html


path_txt = '/home/diego-silva/Documentos/regex_python/cadastro-professor-tutores-io.txt'
path_csv_output = '/home/diego-silva/Documentos/regex_python/'

dictionaryEmails = {}

def regex(reString,path):
    
    content = open(path, 'r').read()
    
    matching = re.findall(reString,content)

    return matching

def saveData(listData,pathOutput,outputName):
    
    dictionaryEmails['emails'] = listData
    dataFrame = pd.DataFrame(dictionaryEmails, columns = ["emails"])
    dataFrame.to_csv(pathOutput + outputName,encoding='utf-8')


    

## create email list 
emails = regex(r'[\w\.-]+@[\w\.-]+', path_txt) 

## save csv email list 

saveData(emails,path_csv_output,'emailList.csv')

## create list with the amount of math teachers

mathTeacher = regex(r'[\w.-]+tem+[\w.-]+ica',path_txt)

print 'number of math teachers\n'
print len(mathTeacher)

