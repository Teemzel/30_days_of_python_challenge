# Regular Expressions
import re 
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
match = re.search('love', paragraph, re.I)
print(match)
match = re.findall('love', paragraph, re.I)
print(match)
match = re.findall('teaching', paragraph, re.I)
print(match)
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
clean_text = re.sub('%|\$|@|&|#', '', sentence)
print(clean_text)
clean_text = re.sub(r'[%$@&#]', '', sentence)
print(clean_text)