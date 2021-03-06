# I N C O M P L E T E ! ! ! ! :
# # This code 'works', but not for some test arrays (that have 200,000+ items). Need to optimize!
#

def parts_sums(ls):
    temp = sum(ls)
    sums = [temp]
    for i in range(len(ls)):
        delete = ls.pop(0) 
        temp = temp - delete
        sums.append(temp)
    return sums
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Let us consider this example (array written in general format):
  ls = [0, 1, 3, 6, 10]
Its following parts:
  ls = [0, 1, 3, 6, 10]
  ls = [1, 3, 6, 10]
  ls = [3, 6, 10]
  ls = [6, 10]
  ls = [10]
  ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0].
The function parts_sums (or its variants in other languages) will take as parameter a list ls,
and return a list of the sums of its parts as defined above.
"""
