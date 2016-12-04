'''
Common bit tasks
'''


'''Get Bit:  get bit i in number num'''
def getBit(num, i):
    return int((num & (1 << i)) != 0)

'''Set Bit:  set bit i of number num'''
def setBit(num, i):
    return num | (1 << i)

'''Clear Bit:  clear bit i of number num'''
def clearBit(num, i):
    mask = ~(1 << i)
    return num & mask

'''Clear Bit, from the most significant bit through bit i (inclusive)'''
def clearBitsMSBthroughI(num, i):
    mask = (1 << i) - 1 
    return num & mask

'''Clear Bit, from bit i through 0-1  (inclusive)'''
def clearBitsIthrough0(num, i):
    # mask = ~(-1 >>> (31 - i)): Note: python does not support ">>>"
    mask = ~(1 << (i+1)) - 1
    return num & mask

'''Update (i)th bit of number n to value v'''
def updateBit(num, i, v):
    mask = ~(1 << i)
    return (num & mask) | (v << i)
 