def wordPattern( pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
    
    
pattern = 'abba'
str = 'apple dog dog apple'
print (wordPattern(pattern , str))