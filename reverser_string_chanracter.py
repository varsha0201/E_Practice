# def isAlphabet(x):
#     return x.isalpha()

# def reverse(string):
#     LIST = toList(string)

#     # Initialize left and right pointers
#     r = len(LIST) - 1
#     l = 0

#     # Traverse LIST from both ends until
#     # 'l' and 'r'
#     while l < r:

#         # Ignore special characters
#         if not isAlphabet(LIST[l]):
#             l += 1
#         elif not isAlphabet(LIST[r]):
#             r -= 1

#         # Both LIST[l] and LIST[r] are not special
#         else:
#             LIST[l], LIST[r] = swap(LIST[l],
#                                     LIST[r])
#             l += 1
#             r -= 1

#     return toString(LIST)

# # Utility functions
# def toList(string):
#     List = []
#     for i in string:
#         List.append(i)
#     return List

# def toString(List):
#     return ''.join(List)

# def swap(a, b):
#     return b, a

# # Driver code
# string = "a!!!b.c.d,e'f,ghi"
# print "Input string: " + string
# string = reverse(string)
# print "Output string: " + string

#--------------------------reverese string without changing special caharacter position------------
# Input : asd@3!g!23jjk
# Output : kjj@3!g!23dsa

# strSample = "asd@3!g!23jjk"

# # convert string into list

# listSample = list(strSample)

# i = 0
# j = len(listSample)-1

# while i < j :
#     if not listSample[i].isalpha():
#         i += 1
#     elif not listSample[j].isalpha():
#         j -= 1
#     else:
#         # swap the element in the list
#         # if both element is alphabet
#         listSample[i], listSample[j] = listSample[j], listSample[i]
#         i += 1
#         j -= 1

# # convert list into string
# # by concatinating each elemnet in the list

# strOut = ''.join(listSample)
# print(strOut)

# --------------------------------------- array program --------------------------------------
#You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

# Input  :  arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# def segregate(arr):
#     res = ([x for x in arr if x==0] + [x for x in arr if x ==1])
#     print(res)

# if __name__ == "__main__":
#     arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
#     segregate(arr)

# reverse the whole string without reversing the individual words in it in python

# Input: i like this program very much
# Output: much very program this like i

# s = "This.is.dog"
# words = s.split('.')
# string = []
# for word in words:
#     string.insert(0, word)

# print("Reverse String:")
# print(".".join(string))

#-----------------------------Zig-Zag ------------------------------------------------------------
# Input : 4, 3, 7, 8, 6, 2, 1
# Output : 3  7  4  8  2  6  1

def zigZag(arr, n):

    flag = True
    for i in range(n-1):
        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        flag = bool(1- flag)
    print(arr)

    arr = [4,3,7,8,6,2,1]
    n = len(arr)
    zigZag(arr, n)

