s='''I go by the name CL of 2ne1
It’s been a long time comming
But we’re here now
And we about to set the roof on fire baby
You better get yours
‘Cause I’m getting mine
Eh eh eh eh eh eh ehh ,2ne1'''
#方法一：引入collections模块中的Counter类
from collections import Counter
word_counts=Counter(s)
del word_counts[' '],word_counts['\n'],word_counts[',']
top_three=word_counts.most_common(3)
print(top_three)




#方法二：
data={}
for i in s:
    if i==' 'or i==',' or i=='\n' or i=='\'':
        continue
    data[i]=data.get(i,0)+1

print(sorted(data.items(),key=lambda x : x[1],reverse=True)[:3])


