# 7.猴子吃桃，一共10天，每天吃一半然后再吃一个，第十天还有1个，求一个多少个桃子
# sum = 1 #定义桃子数量sum
# for i in range(9,0,-1):  # 括号里包前不包后，#i是定义一共10天，但是第10天没吃， #逆向思维，第一天有1个桃子，即第二天又有x 即 x/2-1 =1
#     sum = (sum+1)*2  #桃子总数，根据定义得
#     # print(f"第{i}天桃子数量{sum}")
# print(f"猴子第一天一共得到{sum}个桃子")#每得到一天 打印一天
# 8.统计字符类型个数
# s = 1
# for i in range(1,10):
#     # print(i,type(i))
#     s += 1
# print(type(i),"整型的个数:",s,sep = '')
#  9.对简单列表元素排序
# list = [1,2,3,4,7,8,6,5,10,11,20,15,17,18]
# list.sort()   #将列表元素从小到大排列
# print(list)   #打印元素从小到大
# list.reverse()   #翻转，可以实现元素从大到小排列
# print(list)    #打印元素从大到小
#  10.学生成绩排序
# students = [['李',80],['张',60],['明',50]]
# # students.sort()  # 默认按第一个元素排列
# students.sort(key=lambda x:x[1]) #key=lambda x:x[]定义一个简单的函数
# print(students)

# s = [[50,20],[30,50],[20,30]]
# s.sort(key = lambda x:x[0],reverse = True)
# print(s)
# s.sort(key = lambda x:x[1])
# print(s)
# 11.列表偶数求和
# li = [1,2,4,5,7,8,10,12,18,16,20,22]
# sum = 0
# for i in li:
#     if i % 2 == 0:
#         print(i,end = ' ')
#         sum += i
# print(sum)

