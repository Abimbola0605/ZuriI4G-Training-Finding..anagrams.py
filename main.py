# Check if a word is an anagrams
# Exxample:
# find_anagrams("hello")--> False
# find_anagrams("racecar")--> True
# we have many ways of solving this but i will be using list method

def find_anagram (string1,string2):
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    return (list1 == list2)

print(find_anagram("forty five", "over fifty"))


# if i modify this, it going to give me a False
