def remove_duplicates(s: str, k:int) -> str:
    
    ns = ""
    ## removing duplicates
    ptr = 0
    end = len(s)
    duplicate_found = False
    while(ptr < end):
        if(s[ptr:ptr + k] == s[ptr] * k):
            ## we have a k duplicates of char s[ptr]
            ptr += k 
            duplicate_found = True
        else :
            ns += s[ptr]
            ptr += 1
    

    ## could avoid this col
    if(duplicate_found):
        return remove_duplicates(ns, k)
    
    return s
    


if __name__ == "__main__":
    ## few tests :
    print("1) ", end="\t")
    print(remove_duplicates("abcd", 2))
    print("Expected : abcd")
    print("2) ", end="\t")
    print(remove_duplicates("deeedbbcccbdaa", 3))
    print("Expected : aa")
    print("3) ", end="\t")
    print(remove_duplicates("pbbcggttciiippooaais", 2))
    print("Expected : ps")





