# Bit manipulation

## Starters

Get your hands dirty by mannually calculate the following:

| 0110 + 0010 | 0011 * 0101  | 0110 + 0110      |
|-------------|--------------|------------------|
| 0011 + 0010 | 0011 * 0011  | 0100 * 0011      |
| 0110 - 0011 | 1101 >> 2    | 1101 ^ (~1101)   |
| 1000 - 0110 | 1101 ^ 0101  | 1011 & (~0 << 2) |

## Bit Facts and Tricks
 
 
 Try to make sense with the following facts about bit manipulation:
 (We use "1s" and "0s" to indicate a sequence of 1s or 0s, respectively)
 
| x ^ 0s = x  | x & 0s = 0 | x &#124; 0s = x  |
|-------------|------------|------------------|
| x ^ 1s = ~x | x & 1s = x | x &#124; 1s = 1s |
| x ^ x = 0   | x & x = x  | x &#124; x = x   |
 
## Commmon Bit Tasks: Get, Set, Clearn and Update Bit:

 [Bit GSCU](https://github.com/tonytan4ever/AlgorithmPractice/blob/master/BitManipulation/common_bit_tasks.py)
  
