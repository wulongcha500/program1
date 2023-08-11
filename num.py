def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# 测试示例
num = int(input("请输入一个整数: "))
if is_prime(num):
    print(num, "是质数")
else:
    print(num, "不是质数")
