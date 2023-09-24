{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Faisalabad\n",
      "1.2\n",
      "Abdullah\n"
     ]
    }
   ],
   "source": [
    "data = [\"Abdullah\", 1.2, \"Faisalabad\"]\n",
    "\n",
    "for i in range (len(data)-1,-1,-1):\n",
    "    print (data[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Abdullah', 1.2, 'Faisalabad', 38000, 38000, 38000, 38000, 38000]\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "student = data \n",
    "student.append(38000)\n",
    "print(data)\n",
    "\n",
    "print(id(data) == id(student))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "tuple1 = (10,20,30)\n",
    "tuple2 = tuple1\n",
    "tuple1 += (40,50)\n",
    "print(id(tuple1) == id(tuple2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2808085584000\n",
      "2808084668144\n"
     ]
    }
   ],
   "source": [
    "tuple1 = (10,20,30)\n",
    "\n",
    "print(id(tuple1))\n",
    "tuple1 += (40,50)\n",
    "print(id(tuple1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "str1 = [\"Abdullah\", 1.2, \"Faisalabad\"]\n",
    "\n",
    "str2 = [\"Younas\", 3.4, \"Lahore\"]\n",
    "\n",
    "print(str1 > str2)\n",
    "print(str1 >= str2)\n",
    "print(str1 <= str2)\n",
    "print(str1 < str2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n",
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]\n",
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
      "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\n",
      "[9, 8, 7]\n"
     ]
    }
   ],
   "source": [
    "numbers = []\n",
    "for i in range(20):\n",
    "    numbers+= [i]\n",
    "\n",
    "print(numbers[::2])\n",
    "print(numbers[:])\n",
    "\n",
    "numbers[10:] = []\n",
    "print(numbers[:])\n",
    "\n",
    "print(numbers[::-1])\n",
    "\n",
    "print(numbers[:6:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['four',\n",
       " 1,\n",
       " 2,\n",
       " 3,\n",
       " 'four',\n",
       " 5,\n",
       " 6,\n",
       " 7,\n",
       " 'four',\n",
       " 9,\n",
       " 10,\n",
       " 11,\n",
       " 'four',\n",
       " 13,\n",
       " 14,\n",
       " 15,\n",
       " 'four',\n",
       " 17,\n",
       " 18,\n",
       " 19]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers = []\n",
    "for i in range(20):\n",
    "    numbers+= [i]\n",
    "numbers[::4] = [\"four\",\"four\",\"four\",\"four\",\"four\"]\n",
    "numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print (5 in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print (1000 in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print (5 not in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print (100 not in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers =[]\n",
    "for i in range(20):\n",
    "    numbers+= [i]\n",
    "numbers = (sorted(numbers, reverse=True))\n",
    "numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\n",
      "14\n"
     ]
    }
   ],
   "source": [
    "print(numbers)\n",
    "print(numbers.index(5,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "5 is not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-59-ab7a0b9c0534>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mnumbers\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0msorted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumbers\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreverse\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumbers\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumbers\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: 5 is not in list"
     ]
    }
   ],
   "source": [
    "numbers = (sorted(numbers, reverse=False))\n",
    "print(numbers)\n",
    "print(numbers.index(5,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key 10 is found at 10\n"
     ]
    }
   ],
   "source": [
    "key = 10\n",
    "\n",
    "if key in numbers:\n",
    "     print(f\"Key {key} is found at {numbers.index(key,4)}\")\n",
    "else:\n",
    "    print(\"it is not found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "student\n",
    "del(student)\n",
    "#student"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n",
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n",
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n",
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n",
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n"
     ]
    }
   ],
   "source": [
    "ratings = [item for item in range(10)]\n",
    "ratings *=5\n",
    "for item in ratings:\n",
    "    print(f\"{item} count => {ratings.count(item)}\")\n",
    "          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 count => 5\n",
      "1 count => 5\n",
      "2 count => 5\n",
      "3 count => 5\n",
      "4 count => 5\n",
      "5 count => 5\n",
      "6 count => 5\n",
      "7 count => 5\n",
      "8 count => 5\n",
      "9 count => 5\n"
     ]
    }
   ],
   "source": [
    "ratings = [item for item in range(10)]\n",
    "ratings *=5\n",
    "unique = []\n",
    "\n",
    "for item in ratings:\n",
    "    if item not in unique:\n",
    "        unique.append(item)\n",
    "        print(f\"{item} count => {ratings.count(item)}\")\n",
    "          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]\n",
      "[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]\n",
      "['YelloW', 'REd', 'WhiTe']\n",
      "['YELLOW', 'RED', 'WHITE']\n",
      "['yellow', 'red', 'white']\n"
     ]
    }
   ],
   "source": [
    "squares = [x**2 for x in numbers]\n",
    "print(squares)\n",
    "\n",
    "cube = [x**3 for x in numbers]\n",
    "print(cube)\n",
    "\n",
    "colors = [\"YelloW\", \"REd\", \"WhiTe\"]\n",
    "print(colors)\n",
    "\n",
    "colors_upper = [x.upper() for x in colors]\n",
    "print(colors_upper)\n",
    "\n",
    "\n",
    "colors_lower = [x.lower() for x in colors]\n",
    "print(colors_lower)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<generator object <genexpr> at 0x0000028DD1B304A0>\n",
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "data = (x for x in range(10))\n",
    "print(data)\n",
    "print(list(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n",
      "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]\n"
     ]
    }
   ],
   "source": [
    "def even_number(num):\n",
    "    return (num%2 == 0)\n",
    "def squares(num):\n",
    "    return (num**2)\n",
    "\n",
    "even = list(filter(even_number, numbers))\n",
    "print(even)\n",
    "\n",
    "square = list(map(lambda x: x**2, numbers))\n",
    "print(square)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(29, 84.2), (34, 93.2), (40, 104.0), (23, 73.4)]\n"
     ]
    }
   ],
   "source": [
    "temp1 = [29, 34,40,23]\n",
    "\n",
    "def faren(tem):\n",
    "    return tem, tem*(9/5)+32\n",
    "\n",
    "\n",
    "temperature = list(map(lambda x: (x, x * 9/5+32), temp1))\n",
    "print(temperature)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Accounts:\n",
    "    def __init__(self,name,balance):\n",
    "        self.name = name\n",
    "        self.balance= balance\n",
    "    def deposit(self, amount):\n",
    "        self.balance+=amount\n",
    "    def withdraw(self, amount):\n",
    "        self.balance-=amount\n",
    "    def __repr__(self):\n",
    "        return(f\"The account is with title {self.name} has balance {self.balance}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The account is with title Usman has balance 16000\n"
     ]
    }
   ],
   "source": [
    "acc = Accounts(\"Usman\", 12000)\n",
    "acc.deposit(4000)\n",
    "print(acc)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
