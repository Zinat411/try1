result = False
def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = 0
        my_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
        if len(s) != len(t):
            return False
        for i in s:
            for (key,value) in my_dict.items():
                if i == key:
                    my_dict[key] += 1
        for i in t:
            for (key,value) in my_dict.items():
                if i == key:
                     my_dict[key] -= 1
        for (key,value) in my_dict.items():
            if value != 0:
                counter += 1
        if counter != 0:
                return False
        else:
                return True
            
result = isAnagram("anagram", "nagaram")
print(result)
