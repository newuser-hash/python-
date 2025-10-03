#12.找出年龄最大者
# list = [['小明',18],['小红',20],['小李',50],['小张',30]]
# list.sort(key=lambda x:x[1])
# list.reverse()
# print(f"年龄最大者：{list[0]}")
#13.按序插入列表
# li = [1,2]
# li2 = [5,4,3,10,9,8,6,7]
# li2.sort()
# for i in li2:
#     li.append(i)
#     # i +=1
# print(li)
# 14.输入数字排序
# 提示用户输入数字，用空格分隔
# input_str = input("请输入多个数字，用空格分隔：")
# numbers = list(map(int, input_str.split()))  #str.split() 字符串的专属用法
# numbers.sort()
# print("排序后的数字：", numbers)
# str = 'a b c d a d'
# print(str.split())
# 15.寻找最小连续9整除数
# n = 0
# while True:
#     if ( n%1 == 0 and
#             (n+1)%2 == 0 and
#             (n+2)%3 == 0 and
#             (n+3)%4 == 0 and
#             (n+4)%5 == 0 and
#             (n+5)%6 == 0 and
#             (n+6)%7 == 0 and
#             (n+7)%8 == 0 and
#             (n+8)%9 == 0):
#         print(f'找到最小起始数字：{n}')
#         for i in range(9):
#             print(f'{n + i}能被{i + 1}整除')
#         break
#     n += 1

# n = 0
# while True:
#     # 检查当前n开始的9个连续数是否符合条件
#     # 第1个数n能被1整除，第2个n+1能被2整除...第9个n+8能被9整除
#     if (n % 1 == 0 and
#             (n + 1) % 2 == 0 and
#             (n + 2) % 3 == 0 and
#             (n + 3) % 4 == 0 and
#             (n + 4) % 5 == 0 and
#             (n + 5) % 6 == 0 and
#             (n + 6) % 7 == 0 and
#             (n + 7) % 8 == 0 and
#             (n + 8) % 9 == 0):
#
#         print(f"找到最小起始数字：{n}")
#         # 打印这9个数字
#         for i in range(9):
#             print(f"{n + i} 能被 {i + 1} 整除")
#         break  # 找到后退出循环
#     n += 1

# 16.输入整数打印型号
# i = 0
# while True:
#     num = int(input('请输入数字：'))
#     if num//10 > 1000:
#         print('大型')
#     elif 100 <= num//10 <= 1000:
#         print('中性')
#     else:
#         print('小型')
#     i +=1
#     if i == 3:
#         break
# 17.判断数字奇偶性
# while True:
#     num = input('请输入数字：')
#     if int(num)%2 == 0:
#         print('偶数')
#     elif int(num)%2== 1:
#         print('奇数')
#     if int(num) == 0:    #注意else后面不能加条件。
#         break  # 设置一个值跳出死循环