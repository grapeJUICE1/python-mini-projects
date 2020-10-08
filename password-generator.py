import string
import random
import sys

chars = list(string.ascii_letters)
nums = list(string.digits)
punc = list(string.punctuation)

password = []

nchar = int(input('How many chars u want in the password???'))

ndigits = int(input('How many digits u want in the password???'))

npunc = int(input('How many punctuation symbols u want in the password??? '))
total = nchar + ndigits + npunc

if total < 8:
  print('the total number of letters for the password must be greater than or equal to 8!!!')
  sys.exit()
else:
  i = 0
  j = 0
  k = 0

  while i < nchar or j < ndigits or k < npunc:
    if i != nchar:
      password.append(chars[random.randint(0 , len(chars) - 1)])
      i+=1
    if j != ndigits:
      password.append(nums[random.randint(0 , len(nums) - 1)])
      j+=1
    if k != npunc:
      password.append(punc[random.randint(0 , len(punc) - 1)])
      k+=1

  print(''.join(random.sample(password, len(password))))
