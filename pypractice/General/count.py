s=input("enter a sentence: ").lower()

total_v_count=0

for e in "aeiou":
    v_count=s.count(e)
    total_v_count+=v_count
    print("{} -> {}".format(e,v_count))
    
print("total number of vowels in the sentence you entered= ", total_v_count)
