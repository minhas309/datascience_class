{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "29bb08f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2022 3\n",
      "3.57 2\n",
      "Smith 1\n",
      "Mary 0\n",
      "True\n",
      "Mutability Test\n",
      "1802104889472\n",
      "1802104889472\n",
      "['Mary', 'Smith', 3.57, 2022, 'Faisalabad']\n",
      "(10, 20, 30, 40, 50)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student = ['Mary', 'Smith', 3.57, 2022]\n",
    "student\n",
    "\n",
    "\n",
    "#iterating over the lists\n",
    "for i in range (len(student)-1, -1,-1):\n",
    "    print (student[i], i)\n",
    "\n",
    "student_ = student\n",
    "print(student is student_)\n",
    "#lists are mutable \n",
    "\n",
    "print (\"Mutability Test\")\n",
    "print(id(student))\n",
    "student.append(\"Faisalabad\")\n",
    "print(id(student))\n",
    "#Mutable objects follows the same reference here!\n",
    "print(student_)\n",
    "\n",
    "#but immutable doesn't\n",
    "\n",
    "tuple1 = (10, 20, 30)\n",
    "tuple2 = tuple1\n",
    "tuple1 += (40, 50)\n",
    "print(tuple1)\n",
    "tuple2\n",
    "\n",
    "#you can check them with id()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0d53a3ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#Logical operations on lists\n",
    "st3  = [\"Abdullah\",\"Younas\",3.4,2020,\"Faisalabad\"]\n",
    "st4  = [\"Ibrahim\",\"Younas\",2.4,2020,\"Lahore\"]\n",
    "\n",
    "print (st3 >= st4)\n",
    "print (st3 > st4)\n",
    "print (st3 < st4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "63b8d27e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5]\n",
      "[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]\n",
      "[0, 6, 12, 18]\n",
      "[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\n",
      "[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['zero', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'ten', 11, 12, 13, 14]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers = []\n",
    "for i in range (20):\n",
    "    numbers += [i]\n",
    "\n",
    "print(numbers[:6])\n",
    "print(numbers[6:])\n",
    "print(numbers[::6])\n",
    "print(numbers[::-1])\n",
    "\n",
    "print(numbers[-1::-1])\n",
    "numbers[::10] = ['zero','ten']\n",
    "numbers\n",
    "numbers[15:] = []\n",
    "numbers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fa588d29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]\n",
      "[14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]\n",
      "[14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "del numbers[::10]\n",
    "numbers.sort()\n",
    "print(numbers)\n",
    "numbers.sort(reverse=True)\n",
    "print(numbers)\n",
    "print(sorted(numbers, reverse=True))\n",
    "\n",
    "print (1000 in numbers)\n",
    "print (11 in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ca14862",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "21\n",
      "found key 3 at index 10\n"
     ]
    }
   ],
   "source": [
    "print (numbers.index(5))\n",
    "numbers *=2\n",
    "#print(numbers)\n",
    "print (numbers.index(5,11))\n",
    "\n",
    "# consider the following example\n",
    "\n",
    "key = 3\n",
    "\n",
    "if (key in numbers):\n",
    "    print(f'found key {key} at index {numbers.index(key)}')\n",
    "else:\n",
    "    print(f\"{key} not found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ad21c012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The count of 0: 5\n",
      "The count of 1: 5\n",
      "The count of 2: 5\n",
      "The count of 3: 5\n",
      "The count of 4: 5\n"
     ]
    }
   ],
   "source": [
    "#lets count the frequency of each item\n",
    "ratings = []\n",
    "for i in range(5):\n",
    "    ratings += [i]\n",
    "ratings *=5\n",
    "unique = []\n",
    "for item in ratings:\n",
    "    if item not in unique:\n",
    "        unique.append(item)\n",
    "        print(f'The count of {item}: {ratings.count(item)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7bc897df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Green\n",
      "Black\n",
      "Yellow\n",
      "Red\n"
     ]
    }
   ],
   "source": [
    "#think lists as simulation of stacks\n",
    "\n",
    "stack = []\n",
    "stack.append('Red')\n",
    "stack.append('Yellow')\n",
    "stack.append('Black')\n",
    "stack.append('Green')\n",
    "stack\n",
    "\n",
    "for i in range(len(stack)):\n",
    "    if len(stack) > 0:\n",
    "        print(stack.pop())\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4de7fbc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['red', 'orange', 'yellow', 'green', 'blue']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#list comprehensions\n",
    "\n",
    "#creating new lists\n",
    "new_list = [list for list in range(1,6)]\n",
    "new_list\n",
    "\n",
    "#mapping the data\n",
    "cube_list = [item **3 for item in new_list]\n",
    "cube_list\n",
    "\n",
    "#filtering the data\n",
    "divide_by_two = [item for item in cube_list if item %2 ==0]\n",
    "divide_by_two\n",
    "\n",
    "colors = ['red', 'orange', 'yellow', 'green', 'blue']\n",
    "colors_caps = [color.upper() for color in colors]\n",
    "colors_caps\n",
    "\n",
    "color_lower = [color.lower() for color in colors]\n",
    "color_lower"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "35daeff5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 4 16 36 64 "
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0, 4, 16, 36, 64]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#generator expressions\n",
    "\n",
    "squares = (x**2 for x in range (0,10) if x%2==0)\n",
    "squares\n",
    "for item in squares:\n",
    "    print(item, end=' ')\n",
    "    \n",
    "#but if you want to create the list with help of generator expressions use list ()\n",
    "\n",
    "squares_list = list(x**2 for x in range (0,10) if x%2==0)\n",
    "squares_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "577eecff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]\n",
      "[28, 26, 24, 22, 18, 16, 14, 12, 10, 8, 6, 4, 2, 28, 26, 24, 22, 18, 16, 14, 12, 10, 8, 6, 4, 2]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[(41, 5.0), (32, 0.0), (212, 100.0)]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#filter, map, reduce\n",
    "\n",
    "def even_numbers(number):\n",
    "    return number % 2 == 0\n",
    "\n",
    "even = list(filter(even_numbers, numbers))\n",
    "even\n",
    "\n",
    "#shorthand anonymous functions with lambda keyword\n",
    "#generic syntax => lambda params_list: expressions\n",
    "print (numbers)\n",
    "double = list(map(lambda x:x*2, numbers))\n",
    "print(double)\n",
    "\n",
    "fahrenheit = [41, 32, 212]\n",
    "new_temp = list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit))\n",
    "new_temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f08411c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name=Bob; GPA=3.5\n",
      "Name=Sue; GPA=4.0\n",
      "Name=Amanda; GPA=3.75\n"
     ]
    }
   ],
   "source": [
    "#combining iterators\n",
    "\n",
    "students = ['Bob', 'Sue', 'Amanda']\n",
    "cgpa = [3.5, 4.0, 3.75]\n",
    "for name, gpa in zip(students, cgpa):\n",
    "    print(f'Name={name}; GPA={gpa}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "34aae0c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0][0]=3.0 [0][1]=3.5 [0][2]=4 [0][3]=3.4 \n",
      "\n",
      "[1][0]=3.59 [1][1]=3.53 [1][2]=3.99 [1][3]=3.1 \n",
      "\n",
      "[2][0]=3.14 [2][1]=3.55 [2][2]=3.21 [2][3]=3.3 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#two dimensional lists\n",
    "\n",
    "sgpas_ = [ [3.0,3.5,4,3.4],\n",
    "          [3.59,3.53,3.99,3.1],\n",
    "          [3.14,3.55,3.21,3.3]\n",
    "]\n",
    "\n",
    "for i, row in enumerate(sgpas_):\n",
    "    for j, item in enumerate(row):\n",
    "        print (f'[{i}][{j}]={item}', end = \" \")\n",
    "    print ('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "e9300b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Accounts:\n",
    "    def __init__(self, name, balance):\n",
    "        self.name = name\n",
    "        self.balance = balance\n",
    "    def deposit(self, amount):\n",
    "        self.balance+= amount\n",
    "    def getBalance(self):\n",
    "        return self.balance\n",
    "    def __repr__(self):\n",
    "        \"\"\"Return Time string for repr().\"\"\"\n",
    "        return (f'Account Title {self.name} have active balance of {self.balance} rupees')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "61071138",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Account Title Usman have active balance of 600 rupees\n"
     ]
    }
   ],
   "source": [
    "acc = Accounts(\"Usman\", 100)\n",
    "acc.deposit(500)\n",
    "print(acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e029c329",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
