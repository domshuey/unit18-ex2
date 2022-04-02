# def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?
    
#         >>> same_frequency(551122, 221515)
#         True
        
#         >>> same_frequency(321142, 3212215)
#         False
        
#         >>> same_frequency(1212, 2211)
#         True
#     """
#     num1 = list(str(num1))
#     num1.sort()
    
#     num2 = list(str(num2))
#     num2.sort()

#     print(num1)
#     print(num2)
#     return(num1 == num2)

# or

def counter(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0) + 1
    return count

def same_frequency(num1, num2):
    return (counter(str(num1)) == counter(str(num2)))