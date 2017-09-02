# Character-statistics
Given a paragraph or a string, the number of characters counted, and can find the most frequent characters
给定一段话或者一个字符串，统计出字符的个数，同时可以求出出现次数最多的字符


两种方法来实现这个功能，同时打印出现频率最高的三个字符
##方法一引入了collections模块中的Counter类来直接生成一个字典，用类中的most_common方法来获取出现频率最高的字符
##方法二直接用循环遍历字符串，统计个数，用sorted函数来进行排序
