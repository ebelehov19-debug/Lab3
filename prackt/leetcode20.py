# class Solution:
#     def isValid(self, s: str) -> bool:
#         a=[]
#         for i in s:
#             if i in "({[":
#                 a.append(i)
#             else:
#                 if len(a)==0:
#                     return False
#                 if i==')':
#                     c=a.pop()
#                     if c!='(':
#                         return False
#                 if i==']':
#                     c=a.pop()
#                     if c!='[':
#                         return False
#                 if i=='}':
#                     c=a.pop()
#                     if c!='{':
#                         return False
#         return len(a)==0


        