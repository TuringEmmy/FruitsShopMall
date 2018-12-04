# 算术运算符

# +	加	两个对象相加 a + b 输出结果 30
# -	减	得到负数或是一个数减去另一个数 a - b 输出结果 -10
# *	乘	两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
# /	除	b / a 输出结果 2
# //	取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
# %	取余	返回除法的余数 b % a 输出结果 0
# **	指数	a**b 为10的20次方， 输出结果 100000000000000000000

num1 = 3

num2 = 4

result = num1 ** num2
print(result)

result = num1 % num2

print(result)

# 求商 //
result = num1 // num2
print(result)

# 整数相除返回的结果类型是float
result = num1 / num2
print(result, type(result))


# *
result = num1 * num2
print(result)


# -
result = num1 - num2
print(result)


# 保存相加的结果
result = num1 + num2
print(result)
