'''
XOR is standard operation on bits. If X and Y are two bits (1s or 0s), then X XOR Y
           Equals 1 when X Y, Otherwise X XOR Y = 0.
                  
                        0 XOR 1 = 1        1 XOR 0 = 1
                        0 XOR 0 = 0        1 XOR 1 = 0
           
 The XOR operation can be extended to non-negative integers. Let K and L be two such        
 integers. And A and B their binary  representations. (For the sake of simplicity, 
 if one of them is shorter, let us add some leading zeros, so that A and B are of the same length.) 
 The bitwise XOR of K and L (denoted as K bitor L) is defined in the following way: We build a sequence
of bits C by taking the XOR of bits from A and B at the same positions. 
C is a binary representation of K bitxor L.


For example, for K = 12 and L = 21 we obtain:
   
      A = 01100
      B = 10101
      C = 11001


And C is a binary representation of K bitxor L = 25
Now we can define the bitwise XOR product. If M and N are two non-negative integers, such that M <= N, 
then their bitwise XOR product is the bitwise XOR of all integers from M to N:
     M bitxor (M+1) bitxor … bitxor (N-1) bitxor N


Note that the bitwise XOR is associative; that is, the order in which this operation is performed 
does not matter.


For example, the bitwise XOR product of M = 5 nd N = 8 is 12, because:
     5 bitxor 6 bitxor 7 bitxor 8  = 
         3          bitxor     15         =  12
Write a function that calculates the bitwise XOR product of two integers of M, N

'''

'''
Reference: http://stackoverflow.com/questions/10670379/find-xor-of-all-numbers-in-a-given-range 
'''


def bitwisexor_0_to_a(a):
       list = [a, 1, a+1, 0]
       return list[a%4]


def solution(M, N):
       return bitwisexor_0_to_a(N)^bitwisexor_0_to_a(M-1)