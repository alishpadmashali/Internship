#!/usr/bin/env python
# coding: utf-8

# # Regular Expression

# In[39]:


import regex as re
def replace(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern,':',text)
    return replaced_text
sample_text='Python Exercises, PHP exercises.'
replaced=replace(sample_text)
print(replaced)


# In[47]:


#25
def duplicate(sentence):
    pattern=r'\b(\w+)\b(?:\s+\1\b)+'
    replaced_text=re.sub(pattern, r'\1', sentence)
    return replaced_text
sample_sentence='Hi world world Welcome to Data Data Science.'
result=duplicate(sample_sentence)
print(result)


# In[48]:


#24
def UPPERCASE_lowercase(text):
    pattern=r'[A-Z][a-z]+'
    matches=re.findall(pattern, text)
    return matches
sample_text='Machine learning and Artificial inteligence is part of Data Science.'
result=UPPERCASE_lowercase(sample_text)
print(result)


# In[53]:


#22
def MAX(string):
    numericvalues=re.findall(r'\d+', string)
    if numericvalues:
        maxvalue=max(map(int, numericvalues))
        return maxvalue
    else:
        return None
sample10='234 is greater than 190'
Max_num=MAX(sample10)
print(Max_num)


# In[60]:


#23
def Capital_words(text):
    pattern=r'([A-Z][a-z]+)'
    replaced_text=re.sub(pattern, r' \1', text)
    return replaced_text.strip()
sample_text='ILoveProgramming'
result=Capital_words(sample_text)
print(result)


# In[61]:


#21
def separate_numbers(string):
    pattern=r'\d+'
    matches=re.finditer(pattern, string)
    for match in matches:
        number=match.group()
        start_pos=match.start()
        end_pos=match.end()
        print(f"Number: {number}, Start Position: {start_pos}, End Position: {end_pos}")
sample_string='in the class highest marks is 91 and lowest is 35'
separate_numbers(sample_string)


# In[62]:


#20
def a_or_e(string):
    pattern=r'\b[aeAE]\w+\b'
    matches=re.findall(pattern, string)
    return matches
sample_string='An apple a day keeps doctor away by eminem.'
result=a_or_e(sample_string)
print(result)


# In[64]:


#18
def find_occurrence_and_position(string, substring):
    pattern=re.compile(re.escape(substring))
    matches=pattern.finditer(string)
    for match in matches:
        start_pos=match.start()
        end_pos=match.end()
        occurrence=match.group()
        print(f"Substring: {occurrence}, Start Position: {start_pos}, End Position: {end_pos}")
sample_string='This sample string and another sample.'
target_substring='sample'
find_occurrence_and_position(sample_string, target_substring)


# In[65]:


#19
from datetime import datetime
def convert_date_format(date_str):
    # YYYY-MM-DD
    date_obj=datetime.strptime(date_str, '%Y-%m-%d')
    # DD-MM-YYYY
    converted_date=date_obj.strftime('%d-%m-%Y')
    return converted_date
date_str='2023-07-14'
converted_date=convert_date_format(date_str)
print(converted_date)


# In[66]:


#15
def search_words(text, searched_words):
    found_words=[]
    for word in searched_words:
        pattern=re.compile(r'\b' + re.escape(word) + r'\b')
        if re.search(pattern, text):
            found_words.append(word)
    return found_words
sample_text='The quick brown fox jumps over the lazy dog.'
searched_words=['fox', 'dog', 'horse']
found_words=search_words(sample_text, searched_words)
print("Found words:", found_words)


# In[67]:


#28
def Removesymbols(text):
    pattern=re.compile(r'<U\+[\w]+>')
    cleaned_text=re.sub(pattern, '', text)
    return cleaned_text
sample_text="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

cleaned_text=Removesymbols(sample_text)
print("Cleaned text:", cleaned_text)


# In[68]:


#26
def alphanumeric(text):
    pattern=re.compile(r'^.*[a-zA-Z0-9]$')
    match=re.match(pattern, text)
    if match:
        return True
    return False
sample_text="Check Check123123"
if alphanumeric(sample_text):
    print("String ends with an alphanumeric character.")
else:
    print("String does not end with an alphanumeric character.")


# In[22]:


#16
def search_string_with_location(text, searched_word):
    patter=re.compile(re.escape(searched_word))
    matches=re.finditer(pattern, text)
    locations=[match.start() for match in matches]
    return locations
sample_text='The quick brown fox jumps over the lazy dog.'
searched_word='fox'
found_locations=search_string_with_location(sample_text, searched_word)
if found_locations:
    print("Pattern found at location(s):", found_locations)
else:
    print("Pattern not found in the text.")


# In[72]:


#13
def remove_zeros(ip_address):
    pattern=re.compile(r'\b0+(\d+)\b')
    cleaned_ip=re.sub(pattern, r'\1', ip_address)
    return cleaned_ip
ip_address='182.178.021.041'
cleaned_ip=remove_zeros(ip_address)
print("Cleaned IP address:", cleaned_ip)


# In[78]:


#10
def word_at_beginning(pattern, text):
    match = re.match(pattern, text)
    if match:
        return True
    return False
pattern=r'^\w+'  # Matches a word at the beginning of a string
text='Data Science'
if word_at_beginning(pattern, text):
    print("The word matches at the beginning of the string.")
else:
    print("The word does not match at the beginning of the string.")
    


# In[82]:


#12
def startswithnu(text, number):
    pattern = re.compile(r'^' + str(number))
    match = re.search(pattern, text)
    if match:
        return True
    return False
text='123CheckCheck'
number=123
if startswithnu(text, number):
    print("The string starts with the number.")
else:
    print("The string does not start with the number.")


# In[86]:


#11
def valid_string(text):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    match = re.match(pattern, text)
    if match:
        return True
    return False
sample1= 'hello_My_Name,is_Nikum'
if valid_string(sample1):
    print("The string is valid.")
else:
    print("The string is not valid.")


# In[85]:


#6
sample="ImportanceOfRegularExpressionsInPython"
split_text=re.findall('[A-Z][a-z]*', sample)
print("Split text:", split_text)


# In[87]:


#8
def Sequences(text):
    pattern=re.compile(r'[a-z]+_[a-z]+')
    sequences=re.findall(pattern, text)
    return sequences
sample2="this sentence is underscored_with lowercase"
sequences=find_sequences(sample2)
print("Sequences found:", sequences)


# In[91]:


#1
def contains_only_allowed_chars(text):
    pattern=re.compile(r'^[a-zA-Z0-9]+$')
    match=re.match(pattern, text)
    if match:
        return True
    return False
sample4="datascience"
if contains_only_allowed_chars(sample4):
    print("Contains only the allowed characters.")
else:
    print("Contains characters other than the allowed characters.")


# In[90]:


#2
def match_a_followed_by_bs(text):
    pattern=re.compile(r'ab*')
    match=re.fullmatch(pattern, text)
    if match:
        return True
    return False
sample5= "abb"
if match_a_followed_by_bs(sample5):
    print("Matches the pattern.")
else:
    print("Does not match the pattern.")


# In[93]:


#3
def match_a_followed_by_one_or_more_bs(text):
    pattern=re.compile(r'ab+')
    match=re.fullmatch(pattern, text)
    if match:
        return True
    return False
sample6="abbb"
if match_a_followed_by_one_or_more_bs(sample6):
    print("Matches the pattern.")
else:
    print("Does not match the pattern.")


# In[95]:


#27
def hashtags(text):
    hashtags=re.findall(r'#\w+', text)
    return hashtags
sample7='RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'
hashtags=hashtags(sample7)
print("Extracted hashtags:", hashtags)


# In[ ]:




