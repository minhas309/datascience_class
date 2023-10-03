{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "[ 0  2  4  6  8 10 12 14 16 18]\n",
      "10\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#numpy array\n",
    "numbers = np.array([x for x in range(20) if(x%2==0)])\n",
    "print(type(numbers))\n",
    "print(numbers)\n",
    "print(numbers.size)\n",
    "print(numbers.ndim)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Size 6\n",
      "Item Size 4\n",
      "Dimensions 2\n",
      "Shape (2, 3)\n"
     ]
    }
   ],
   "source": [
    "#multidimentional arrays\n",
    "integers = np.array([[3,4,5],[2,4,5]])\n",
    "integers\n",
    "print('Size', integers.size)\n",
    "print('Item Size', integers.itemsize)\n",
    "print('Dimensions', integers.ndim)\n",
    "print('Shape', integers.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Size 6\n",
      "Item Size 8\n",
      "Dimensions 2\n",
      "Shape (2, 3)\n"
     ]
    }
   ],
   "source": [
    "#multidimentional arrays\n",
    "floats = np.array([[.3,.4,.5],[.2,.4,5]])\n",
    "floats\n",
    "print('Size', floats.size)\n",
    "print('Item Size', floats.itemsize)\n",
    "print('Dimensions', floats.ndim)\n",
    "print('Shape', floats.shape)"
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
      "3\n",
      "4\n",
      "5\n",
      "2\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#iteration through the arrays\n",
    "for row in integers:\n",
    "    for col in row:\n",
    "        print(col)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 4 5 2 4 5 "
     ]
    }
   ],
   "source": [
    "for row in integers.flat:\n",
    "    print(row, end=\" \") #single vectors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0 0 0 0]\n",
      " [0 0 0 0 0]\n",
      " [0 0 0 0 0]\n",
      " [0 0 0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "zeros = np.zeros((4,5), dtype='int') #chnage it to integer type \n",
    "print(zeros)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.6 5.6 5.6 5.6 5.6]\n",
      " [5.6 5.6 5.6 5.6 5.6]\n",
      " [5.6 5.6 5.6 5.6 5.6]\n",
      " [5.6 5.6 5.6 5.6 5.6]]\n"
     ]
    }
   ],
   "source": [
    "fives = np.full((4,5),5.6)\n",
    "print(fives)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3],\n",
       "       [ 4,  5,  6],\n",
       "       [ 7,  8,  9],\n",
       "       [10, 11, 12],\n",
       "       [13, 14, 15]])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ranged_array = np.arange(1,16).reshape(5,3)\n",
    "ranged_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10  8  6  4  2]\n"
     ]
    }
   ],
   "source": [
    "listed_array=np.array([x for x in range(10,1,-2)])\n",
    "print(listed_array)"
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
      "[0.         0.001001   0.002002   0.003003   0.004004   0.00500501\n",
      " 0.00600601 0.00700701 0.00800801 0.00900901 0.01001001 0.01101101\n",
      " 0.01201201 0.01301301 0.01401401 0.01501502 0.01601602 0.01701702\n",
      " 0.01801802 0.01901902 0.02002002 0.02102102 0.02202202 0.02302302\n",
      " 0.02402402 0.02502503 0.02602603 0.02702703 0.02802803 0.02902903\n",
      " 0.03003003 0.03103103 0.03203203 0.03303303 0.03403403 0.03503504\n",
      " 0.03603604 0.03703704 0.03803804 0.03903904 0.04004004 0.04104104\n",
      " 0.04204204 0.04304304 0.04404404 0.04504505 0.04604605 0.04704705\n",
      " 0.04804805 0.04904905 0.05005005 0.05105105 0.05205205 0.05305305\n",
      " 0.05405405 0.05505506 0.05605606 0.05705706 0.05805806 0.05905906\n",
      " 0.06006006 0.06106106 0.06206206 0.06306306 0.06406406 0.06506507\n",
      " 0.06606607 0.06706707 0.06806807 0.06906907 0.07007007 0.07107107\n",
      " 0.07207207 0.07307307 0.07407407 0.07507508 0.07607608 0.07707708\n",
      " 0.07807808 0.07907908 0.08008008 0.08108108 0.08208208 0.08308308\n",
      " 0.08408408 0.08508509 0.08608609 0.08708709 0.08808809 0.08908909\n",
      " 0.09009009 0.09109109 0.09209209 0.09309309 0.09409409 0.0950951\n",
      " 0.0960961  0.0970971  0.0980981  0.0990991  0.1001001  0.1011011\n",
      " 0.1021021  0.1031031  0.1041041  0.10510511 0.10610611 0.10710711\n",
      " 0.10810811 0.10910911 0.11011011 0.11111111 0.11211211 0.11311311\n",
      " 0.11411411 0.11511512 0.11611612 0.11711712 0.11811812 0.11911912\n",
      " 0.12012012 0.12112112 0.12212212 0.12312312 0.12412412 0.12512513\n",
      " 0.12612613 0.12712713 0.12812813 0.12912913 0.13013013 0.13113113\n",
      " 0.13213213 0.13313313 0.13413413 0.13513514 0.13613614 0.13713714\n",
      " 0.13813814 0.13913914 0.14014014 0.14114114 0.14214214 0.14314314\n",
      " 0.14414414 0.14514515 0.14614615 0.14714715 0.14814815 0.14914915\n",
      " 0.15015015 0.15115115 0.15215215 0.15315315 0.15415415 0.15515516\n",
      " 0.15615616 0.15715716 0.15815816 0.15915916 0.16016016 0.16116116\n",
      " 0.16216216 0.16316316 0.16416416 0.16516517 0.16616617 0.16716717\n",
      " 0.16816817 0.16916917 0.17017017 0.17117117 0.17217217 0.17317317\n",
      " 0.17417417 0.17517518 0.17617618 0.17717718 0.17817818 0.17917918\n",
      " 0.18018018 0.18118118 0.18218218 0.18318318 0.18418418 0.18518519\n",
      " 0.18618619 0.18718719 0.18818819 0.18918919 0.19019019 0.19119119\n",
      " 0.19219219 0.19319319 0.19419419 0.1951952  0.1961962  0.1971972\n",
      " 0.1981982  0.1991992  0.2002002  0.2012012  0.2022022  0.2032032\n",
      " 0.2042042  0.20520521 0.20620621 0.20720721 0.20820821 0.20920921\n",
      " 0.21021021 0.21121121 0.21221221 0.21321321 0.21421421 0.21521522\n",
      " 0.21621622 0.21721722 0.21821822 0.21921922 0.22022022 0.22122122\n",
      " 0.22222222 0.22322322 0.22422422 0.22522523 0.22622623 0.22722723\n",
      " 0.22822823 0.22922923 0.23023023 0.23123123 0.23223223 0.23323323\n",
      " 0.23423423 0.23523524 0.23623624 0.23723724 0.23823824 0.23923924\n",
      " 0.24024024 0.24124124 0.24224224 0.24324324 0.24424424 0.24524525\n",
      " 0.24624625 0.24724725 0.24824825 0.24924925 0.25025025 0.25125125\n",
      " 0.25225225 0.25325325 0.25425425 0.25525526 0.25625626 0.25725726\n",
      " 0.25825826 0.25925926 0.26026026 0.26126126 0.26226226 0.26326326\n",
      " 0.26426426 0.26526527 0.26626627 0.26726727 0.26826827 0.26926927\n",
      " 0.27027027 0.27127127 0.27227227 0.27327327 0.27427427 0.27527528\n",
      " 0.27627628 0.27727728 0.27827828 0.27927928 0.28028028 0.28128128\n",
      " 0.28228228 0.28328328 0.28428428 0.28528529 0.28628629 0.28728729\n",
      " 0.28828829 0.28928929 0.29029029 0.29129129 0.29229229 0.29329329\n",
      " 0.29429429 0.2952953  0.2962963  0.2972973  0.2982983  0.2992993\n",
      " 0.3003003  0.3013013  0.3023023  0.3033033  0.3043043  0.30530531\n",
      " 0.30630631 0.30730731 0.30830831 0.30930931 0.31031031 0.31131131\n",
      " 0.31231231 0.31331331 0.31431431 0.31531532 0.31631632 0.31731732\n",
      " 0.31831832 0.31931932 0.32032032 0.32132132 0.32232232 0.32332332\n",
      " 0.32432432 0.32532533 0.32632633 0.32732733 0.32832833 0.32932933\n",
      " 0.33033033 0.33133133 0.33233233 0.33333333 0.33433433 0.33533534\n",
      " 0.33633634 0.33733734 0.33833834 0.33933934 0.34034034 0.34134134\n",
      " 0.34234234 0.34334334 0.34434434 0.34534535 0.34634635 0.34734735\n",
      " 0.34834835 0.34934935 0.35035035 0.35135135 0.35235235 0.35335335\n",
      " 0.35435435 0.35535536 0.35635636 0.35735736 0.35835836 0.35935936\n",
      " 0.36036036 0.36136136 0.36236236 0.36336336 0.36436436 0.36536537\n",
      " 0.36636637 0.36736737 0.36836837 0.36936937 0.37037037 0.37137137\n",
      " 0.37237237 0.37337337 0.37437437 0.37537538 0.37637638 0.37737738\n",
      " 0.37837838 0.37937938 0.38038038 0.38138138 0.38238238 0.38338338\n",
      " 0.38438438 0.38538539 0.38638639 0.38738739 0.38838839 0.38938939\n",
      " 0.39039039 0.39139139 0.39239239 0.39339339 0.39439439 0.3953954\n",
      " 0.3963964  0.3973974  0.3983984  0.3993994  0.4004004  0.4014014\n",
      " 0.4024024  0.4034034  0.4044044  0.40540541 0.40640641 0.40740741\n",
      " 0.40840841 0.40940941 0.41041041 0.41141141 0.41241241 0.41341341\n",
      " 0.41441441 0.41541542 0.41641642 0.41741742 0.41841842 0.41941942\n",
      " 0.42042042 0.42142142 0.42242242 0.42342342 0.42442442 0.42542543\n",
      " 0.42642643 0.42742743 0.42842843 0.42942943 0.43043043 0.43143143\n",
      " 0.43243243 0.43343343 0.43443443 0.43543544 0.43643644 0.43743744\n",
      " 0.43843844 0.43943944 0.44044044 0.44144144 0.44244244 0.44344344\n",
      " 0.44444444 0.44544545 0.44644645 0.44744745 0.44844845 0.44944945\n",
      " 0.45045045 0.45145145 0.45245245 0.45345345 0.45445445 0.45545546\n",
      " 0.45645646 0.45745746 0.45845846 0.45945946 0.46046046 0.46146146\n",
      " 0.46246246 0.46346346 0.46446446 0.46546547 0.46646647 0.46746747\n",
      " 0.46846847 0.46946947 0.47047047 0.47147147 0.47247247 0.47347347\n",
      " 0.47447447 0.47547548 0.47647648 0.47747748 0.47847848 0.47947948\n",
      " 0.48048048 0.48148148 0.48248248 0.48348348 0.48448448 0.48548549\n",
      " 0.48648649 0.48748749 0.48848849 0.48948949 0.49049049 0.49149149\n",
      " 0.49249249 0.49349349 0.49449449 0.4954955  0.4964965  0.4974975\n",
      " 0.4984985  0.4994995  0.5005005  0.5015015  0.5025025  0.5035035\n",
      " 0.5045045  0.50550551 0.50650651 0.50750751 0.50850851 0.50950951\n",
      " 0.51051051 0.51151151 0.51251251 0.51351351 0.51451451 0.51551552\n",
      " 0.51651652 0.51751752 0.51851852 0.51951952 0.52052052 0.52152152\n",
      " 0.52252252 0.52352352 0.52452452 0.52552553 0.52652653 0.52752753\n",
      " 0.52852853 0.52952953 0.53053053 0.53153153 0.53253253 0.53353353\n",
      " 0.53453453 0.53553554 0.53653654 0.53753754 0.53853854 0.53953954\n",
      " 0.54054054 0.54154154 0.54254254 0.54354354 0.54454454 0.54554555\n",
      " 0.54654655 0.54754755 0.54854855 0.54954955 0.55055055 0.55155155\n",
      " 0.55255255 0.55355355 0.55455455 0.55555556 0.55655656 0.55755756\n",
      " 0.55855856 0.55955956 0.56056056 0.56156156 0.56256256 0.56356356\n",
      " 0.56456456 0.56556557 0.56656657 0.56756757 0.56856857 0.56956957\n",
      " 0.57057057 0.57157157 0.57257257 0.57357357 0.57457457 0.57557558\n",
      " 0.57657658 0.57757758 0.57857858 0.57957958 0.58058058 0.58158158\n",
      " 0.58258258 0.58358358 0.58458458 0.58558559 0.58658659 0.58758759\n",
      " 0.58858859 0.58958959 0.59059059 0.59159159 0.59259259 0.59359359\n",
      " 0.59459459 0.5955956  0.5965966  0.5975976  0.5985986  0.5995996\n",
      " 0.6006006  0.6016016  0.6026026  0.6036036  0.6046046  0.60560561\n",
      " 0.60660661 0.60760761 0.60860861 0.60960961 0.61061061 0.61161161\n",
      " 0.61261261 0.61361361 0.61461461 0.61561562 0.61661662 0.61761762\n",
      " 0.61861862 0.61961962 0.62062062 0.62162162 0.62262262 0.62362362\n",
      " 0.62462462 0.62562563 0.62662663 0.62762763 0.62862863 0.62962963\n",
      " 0.63063063 0.63163163 0.63263263 0.63363363 0.63463463 0.63563564\n",
      " 0.63663664 0.63763764 0.63863864 0.63963964 0.64064064 0.64164164\n",
      " 0.64264264 0.64364364 0.64464464 0.64564565 0.64664665 0.64764765\n",
      " 0.64864865 0.64964965 0.65065065 0.65165165 0.65265265 0.65365365\n",
      " 0.65465465 0.65565566 0.65665666 0.65765766 0.65865866 0.65965966\n",
      " 0.66066066 0.66166166 0.66266266 0.66366366 0.66466466 0.66566567\n",
      " 0.66666667 0.66766767 0.66866867 0.66966967 0.67067067 0.67167167\n",
      " 0.67267267 0.67367367 0.67467467 0.67567568 0.67667668 0.67767768\n",
      " 0.67867868 0.67967968 0.68068068 0.68168168 0.68268268 0.68368368\n",
      " 0.68468468 0.68568569 0.68668669 0.68768769 0.68868869 0.68968969\n",
      " 0.69069069 0.69169169 0.69269269 0.69369369 0.69469469 0.6956957\n",
      " 0.6966967  0.6976977  0.6986987  0.6996997  0.7007007  0.7017017\n",
      " 0.7027027  0.7037037  0.7047047  0.70570571 0.70670671 0.70770771\n",
      " 0.70870871 0.70970971 0.71071071 0.71171171 0.71271271 0.71371371\n",
      " 0.71471471 0.71571572 0.71671672 0.71771772 0.71871872 0.71971972\n",
      " 0.72072072 0.72172172 0.72272272 0.72372372 0.72472472 0.72572573\n",
      " 0.72672673 0.72772773 0.72872873 0.72972973 0.73073073 0.73173173\n",
      " 0.73273273 0.73373373 0.73473473 0.73573574 0.73673674 0.73773774\n",
      " 0.73873874 0.73973974 0.74074074 0.74174174 0.74274274 0.74374374\n",
      " 0.74474474 0.74574575 0.74674675 0.74774775 0.74874875 0.74974975\n",
      " 0.75075075 0.75175175 0.75275275 0.75375375 0.75475475 0.75575576\n",
      " 0.75675676 0.75775776 0.75875876 0.75975976 0.76076076 0.76176176\n",
      " 0.76276276 0.76376376 0.76476476 0.76576577 0.76676677 0.76776777\n",
      " 0.76876877 0.76976977 0.77077077 0.77177177 0.77277277 0.77377377\n",
      " 0.77477477 0.77577578 0.77677678 0.77777778 0.77877878 0.77977978\n",
      " 0.78078078 0.78178178 0.78278278 0.78378378 0.78478478 0.78578579\n",
      " 0.78678679 0.78778779 0.78878879 0.78978979 0.79079079 0.79179179\n",
      " 0.79279279 0.79379379 0.79479479 0.7957958  0.7967968  0.7977978\n",
      " 0.7987988  0.7997998  0.8008008  0.8018018  0.8028028  0.8038038\n",
      " 0.8048048  0.80580581 0.80680681 0.80780781 0.80880881 0.80980981\n",
      " 0.81081081 0.81181181 0.81281281 0.81381381 0.81481481 0.81581582\n",
      " 0.81681682 0.81781782 0.81881882 0.81981982 0.82082082 0.82182182\n",
      " 0.82282282 0.82382382 0.82482482 0.82582583 0.82682683 0.82782783\n",
      " 0.82882883 0.82982983 0.83083083 0.83183183 0.83283283 0.83383383\n",
      " 0.83483483 0.83583584 0.83683684 0.83783784 0.83883884 0.83983984\n",
      " 0.84084084 0.84184184 0.84284284 0.84384384 0.84484484 0.84584585\n",
      " 0.84684685 0.84784785 0.84884885 0.84984985 0.85085085 0.85185185\n",
      " 0.85285285 0.85385385 0.85485485 0.85585586 0.85685686 0.85785786\n",
      " 0.85885886 0.85985986 0.86086086 0.86186186 0.86286286 0.86386386\n",
      " 0.86486486 0.86586587 0.86686687 0.86786787 0.86886887 0.86986987\n",
      " 0.87087087 0.87187187 0.87287287 0.87387387 0.87487487 0.87587588\n",
      " 0.87687688 0.87787788 0.87887888 0.87987988 0.88088088 0.88188188\n",
      " 0.88288288 0.88388388 0.88488488 0.88588589 0.88688689 0.88788789\n",
      " 0.88888889 0.88988989 0.89089089 0.89189189 0.89289289 0.89389389\n",
      " 0.89489489 0.8958959  0.8968969  0.8978979  0.8988989  0.8998999\n",
      " 0.9009009  0.9019019  0.9029029  0.9039039  0.9049049  0.90590591\n",
      " 0.90690691 0.90790791 0.90890891 0.90990991 0.91091091 0.91191191\n",
      " 0.91291291 0.91391391 0.91491491 0.91591592 0.91691692 0.91791792\n",
      " 0.91891892 0.91991992 0.92092092 0.92192192 0.92292292 0.92392392\n",
      " 0.92492492 0.92592593 0.92692693 0.92792793 0.92892893 0.92992993\n",
      " 0.93093093 0.93193193 0.93293293 0.93393393 0.93493493 0.93593594\n",
      " 0.93693694 0.93793794 0.93893894 0.93993994 0.94094094 0.94194194\n",
      " 0.94294294 0.94394394 0.94494494 0.94594595 0.94694695 0.94794795\n",
      " 0.94894895 0.94994995 0.95095095 0.95195195 0.95295295 0.95395395\n",
      " 0.95495495 0.95595596 0.95695696 0.95795796 0.95895896 0.95995996\n",
      " 0.96096096 0.96196196 0.96296296 0.96396396 0.96496496 0.96596597\n",
      " 0.96696697 0.96796797 0.96896897 0.96996997 0.97097097 0.97197197\n",
      " 0.97297297 0.97397397 0.97497497 0.97597598 0.97697698 0.97797798\n",
      " 0.97897898 0.97997998 0.98098098 0.98198198 0.98298298 0.98398398\n",
      " 0.98498498 0.98598599 0.98698699 0.98798799 0.98898899 0.98998999\n",
      " 0.99099099 0.99199199 0.99299299 0.99399399 0.99499499 0.995996\n",
      " 0.996997   0.997998   0.998999   1.        ]\n"
     ]
    }
   ],
   "source": [
    "floted_array = np.linspace(.0,1.0,num=1000)\n",
    "print(floted_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "548 ms ± 2.87 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "%timeit sum(x for x in range(10_000_000))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "900 ms ± 12 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "%timeit np.array([x for x in range(10_000_000)]).sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 6  8 10]\n",
      " [ 4  8 10]]\n",
      "[[ 9 16 25]\n",
      " [ 4 16 25]]\n",
      "[[13 14 15]\n",
      " [12 14 15]]\n"
     ]
    }
   ],
   "source": [
    "#matrix arithematic operations\n",
    "print(integers*2)\n",
    "print(integers**2)\n",
    "print(integers + 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False False False False False False  True  True  True]\n"
     ]
    }
   ],
   "source": [
    "print(numbers > 12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([14, 16, 18])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers[numbers>12]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  4,  9, 16, 25], dtype=int32)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "task_array = np.arange(1,6)\n",
    "\n",
    "task_array**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[8 7 9 8 6 7]\n",
      " [6 9 7 8 8 7]\n",
      " [9 5 5 5 9 6]\n",
      " [6 5 8 5 9 5]\n",
      " [6 9 7 5 9 7]]\n"
     ]
    }
   ],
   "source": [
    "grades = np.random.randint(5,10,30).reshape(5,6)\n",
    "print(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GRADES: [[8 7 9 8 6 7]\n",
      " [6 9 7 8 8 7]\n",
      " [9 5 5 5 9 6]\n",
      " [6 5 8 5 9 5]\n",
      " [6 9 7 5 9 7]]\n",
      "GRADES FOR 2nd Student : 5\n",
      "Complete row [6 9 7 8 8 7]\n",
      "No of Rows [[6 9 7 8 8 7]\n",
      " [9 5 5 5 9 6]\n",
      " [6 5 8 5 9 5]]\n",
      "No of Rows [[8 7 9 8 6 7]\n",
      " [9 5 5 5 9 6]\n",
      " [6 5 8 5 9 5]]\n"
     ]
    }
   ],
   "source": [
    "#For Rows\n",
    "print('GRADES:',grades)\n",
    "print('GRADES FOR 2nd Student :',grades[2,2])\n",
    "print('Complete row',grades[1])\n",
    "print('No of Rows', grades[1:4])\n",
    "print('Multiple alternating rows', grades[[0,2,3]])"
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
      "1st cloumn of all rows [8 6 9 6 6]\n",
      "3rd and 4th cloumn of all rows [[9 8]\n",
      " [7 8]\n",
      " [5 5]\n",
      " [8 5]\n",
      " [7 5]]\n",
      "Alternating cloumn of all rows [[8 9 6]\n",
      " [6 7 8]\n",
      " [9 5 9]\n",
      " [6 8 9]\n",
      " [6 7 9]]\n"
     ]
    }
   ],
   "source": [
    "#For columns\n",
    "print(\"1st cloumn of all rows\", grades[:,0])\n",
    "print(\"3rd and 4th cloumn of all rows\", grades[:,2:4])\n",
    "print(\"Alternating cloumns of all rows\", grades[:,[0,2,4]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[75, 60, 83, 79, 43, 67],\n",
       "       [45, 53, 80, 92, 56, 81],\n",
       "       [48, 90, 80, 51, 50, 63],\n",
       "       [71, 55, 96, 60, 71, 80],\n",
       "       [78, 49, 90, 66, 54, 43],\n",
       "       [58, 61, 44, 51, 50, 83],\n",
       "       [56, 63, 88, 76, 90, 82],\n",
       "       [81, 46, 66, 80, 81, 69],\n",
       "       [42, 43, 89, 75, 89, 56],\n",
       "       [82, 59, 56, 66, 75, 71]])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Activity\n",
    "student_marks = np.random.randint(40,100, 60).reshape(10,6)\n",
    "student_marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[67.83333333 67.83333333 63.66666667 72.16666667 63.33333333 57.83333333\n",
      " 75.83333333 70.5        65.66666667 68.16666667]\n",
      "[63.6 57.9 77.2 69.6 65.9 69.5]\n"
     ]
    }
   ],
   "source": [
    "#mean values \n",
    "students_mean = student_marks.mean(axis=1)\n",
    "print(students_mean)\n",
    "course_mean = student_marks.mean(axis=0)\n",
    "print(course_mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[82 90 96 92 90 83]\n",
      "[83 92 90 96 90 83 90 81 89 82]\n"
     ]
    }
   ],
   "source": [
    "#max values\n",
    "course_max = student_marks.max(axis=0)\n",
    "print(course_max)\n",
    "students_max = student_marks.max(axis=1)\n",
    "print(students_max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75.83333333333333"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#avg of top performing student\n",
    "max(student_marks.mean(axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[75 60 83 79 43 67]\n",
      " [48 90 80 51 50 63]\n",
      " [78 49 90 66 54 43]\n",
      " [56 63 88 76 90 82]\n",
      " [42 43 89 75 89 56]]\n"
     ]
    }
   ],
   "source": [
    "#alternative students\n",
    "alternative_students = student_marks[0:10:2]\n",
    "print(alternative_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[78 90 54]\n"
     ]
    }
   ],
   "source": [
    "#alternative students\n",
    "alternative_course = student_marks[4, 0:6:2]\n",
    "print(alternative_course)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
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
      "0    1\n",
      "1    2\n",
      "2    3\n",
      "3    4\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#Series\n",
    "grades = pd.Series([1,2,3,4])\n",
    "print(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Sams  David  Samss  Abdullah\n",
      "0    91     77     66        77\n",
      "1    98     67     88        66\n",
      "2    61     95     62        87\n",
      "3    80     79     82        79\n",
      "4    91     75     86        85\n"
     ]
    }
   ],
   "source": [
    "marks = {\"Sams\": np.random.randint(60,100,5),\"David\": np.random.randint(60,100,5),\"Samss\": np.random.randint(60,100,5),\"Abdullah\": np.random.randint(60,100,5),}\n",
    "grades = pd.DataFrame(marks)\n",
    "print(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [],
   "source": [
    "grades.index =[\"hello\",\"Hello1\",\"Hello2\",\"Hello3\",\"Hello4\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sams  David  Samss  Abdullah\n",
       "98    67     88     66          1\n",
       "91    77     66     77          1\n",
       "      75     86     85          1\n",
       "80    79     82     79          1\n",
       "61    95     62     87          1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grades.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "91    2\n",
      "61    1\n",
      "98    1\n",
      "80    1\n",
      "Name: Sams, dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(grades.Sams.value_counts())\n",
    "grades.Sams.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
