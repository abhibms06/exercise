def generate_subset(s,start,index):
    if len(s) == 0:
        return
    print(s)
    generate_subset(s[start:index],start,index-1)
    generate_subset(s[start+1:], start+1, index+1)


print('Enter a string')
s = input()

generate_subset(s,0,len(s)-1)

