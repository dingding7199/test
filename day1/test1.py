# coding=utf-8

print "你好，世界";
print "你好，世界";
print "Hello I'm OK"
print r'\(~_~)/ \(~_~)/'
print ''' This is a new hang '''
print (1 + 2) * 3 + 7.5 / 3 + 2.1
print 1.0 + 3.0
a = True
print a and 'a=T' or 'a=F'

if True:
    print "Ture"
else:
    print "False"
print "adsfadf"
#数组
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
#等待客户输入
'''
raw_input("\n\nPress the enter key to exit.")
print raw_input();
'''
import sys;

x = 'foo';
sys.stdout.write(x + '\n')
str = 'Hello World!'
#字符串
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

#元素
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

#元组
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

'''
以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000 # 元组中是非法应用
list[2] = 1000 # 列表中是合法应用
'''
'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值
print tinydict['name']
#算术运算符
a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c = a - b
print "Line 2 - Value of c is ", c

c = a * b
print "Line 3 - Value of c is ", c

c = a / b
print "Line 4 - Value of c is ", c

c = a % b
print "Line 5 - Value of c is ", c

a = 2
b = 3
c = a**b
print "Line 6 - Value of c is ", c

a = 10
b = 5
c = a//b
print "Line 7 - Value of c is ", c

#比较运算符
a = 21
b = 10
c = 0

if ( a == b ):
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"

if ( a != b ):
   print "Line 2 - a is not equal to b"
else:
   print "Line 2 - a is equal to b"

if ( a <> b ):
   print "Line 3 - a is not equal to b"
else:
   print "Line 3 - a is equal to b"

if ( a < b ):
   print "Line 4 - a is less than b"
else:
   print "Line 4 - a is not less than b"

if ( a > b ):
   print "Line 5 - a is greater than b"
else:
   print "Line 5 - a is not greater than b"

a = 5;
b = 20;
if ( a <= b ):
   print "Line 6 - a is either less than or equal to  b"
else:
   print "Line 6 - a is neither less than nor equal to  b"

if ( b >= a ):
   print "Line 7 - b is either greater than  or equal to b"
else:
   print "Line 7 - b is neither greater than  nor equal to b"

#赋值运算符
a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c += a
print "Line 2 - Value of c is ", c

c *= a
print "Line 3 - Value of c is ", c

c /= a
print "Line 4 - Value of c is ", c

c  = 2
c %= a
print "Line 5 - Value of c is ", c

c **= a
print "Line 6 - Value of c is ", c

c //= a
print "Line 7 - Value of c is ", c

#逻辑运算符
a = 10
b = 20
c = 0

if ( a and b ):
   print "Line 1 - a and b are true"
else:
   print "Line 1 - Either a is not true or b is not true"

if ( a or b ):
   print "Line 2 - Either a is true or b is true or both are true"
else:
   print "Line 2 - Neither a is true nor b is true"


a = 0
if ( a and b ):
   print "Line 3 - a and b are true"
else:
   print "Line 3 - Either a is not true or b is not true"

if ( a or b ):
   print "Line 4 - Either a is true or b is true or both are true"
else:
   print "Line 4 - Neither a is true nor b is true"

if not( a and b ):
   print "Line 5 - Either a is not true or b is  not true or both are not true"
else:
   print "Line 5 - a and b are true"


#成员运算符；除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "Line 1 - a is available in the given list"
else:
   print "Line 1 - a is not available in the given list"

if ( b not in list ):
   print "Line 2 - b is not available in the given list"
else:
   print "Line 2 - b is available in the given list"

a = 2
if ( a in list ):
   print "Line 3 - a is available in the given list"
else:
   print "Line 3 - a is not available in the given list"

#运算符优先级
a = 20
b = 20

if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"

if ( id(a) == id(b) ):
   print "Line 2 - a and b have same identity"
else:
   print "Line 2 - a and b do not have same identity"

b = 30
if ( a is b ):
   print "Line 3 - a and b have same identity"
else:
   print "Line 3 - a and b do not have same identity"

if ( a is not b ):
   print "Line 4 - a and b do not have same identity"
else:
   print "Line 4 - a and b have same identity"

# 例3：if语句多个条件

num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print 'hello'
#>>> hello		# 输出结果

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
	print 'undefine'
#>>> undefine		# 输出结果

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
#>>> undefine		# 输出结果


#while语句
count = 0
while(count<9):
    print "NUM is count",count
    count+=1
print "Bye"
#求偶数
a = 1
while a < 10:
    a += 1
    if a% 2 > 0:
        continue
    print a
#当i大于10就跳出
i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break

#无限循环
'''
var = 1
while var == 1:
    num = raw_input("EnterPress: ")
    print "EnterPress", num
print "ByeBye"
'''
#while循环使用else语句
count = 0
while count < 5:
    print count,"is less 5"
    count += 1
else:
    print count,"is more 5"


#简单语句组
#类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
'''
flag = 1
while (flag): print 'Give me a success!'
print "Bye"
'''
#for循环
for letter in "Python":
    print "首字母是",letter

fruits=["banbana","apple","orange"]
for letter in fruits:
    print "列表是",letter
print "ByeBye"


#求质数，并显示两个因数。
for num in range(10,40):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print "%d = %d * %d" % (num,i,j)
            break
    else:
        print num,"是一个质数"


for num in range(10,15):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print "%d = %d * %d" % (num,j,i)
            break
    else:
        print num,"是一个质数"
#以下实例使用了嵌套循环输出2~100之间的素数for循环
for num in range(2,100):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
            print num,"是一个质数"

#以下实例使用了嵌套循环输出2~100之间的素数while循环
i=2
while(i<100):
    j=2
    while(j<=i/j):
        if not(i%j):break
        j+=1
    if(j>i/j):print i,"素数"
    i+=1
print "ByeBye"

#Python break语句，就像在C语言中，打破了最小封闭for或while循环。如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
for letter in "Python":   #First Example
    if letter == 'h':
        break
    print "首字母是",letter

var = 10    #Second Example
while (var > 0):
    print "显示数字",var
    var-=1
    if var == 5:
        break
print "ByeBye"

#Python continue 语句跳出本次循环，而break跳出整个循环。continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

for letter in "Python":
    if letter == "o":
        continue
    print letter

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print "数字是",var


#Python pass是空语句，是为了保持程序结构的完整性。
for letter in "Python":
    if letter == "h":
        pass
        print 'aaa'
    print letter




#Python 数字数据类型用于存储数值。数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
#您可以通过使用del语句删除单个或多个对象
#好多函数 以后用的到


#字符串是 Python 中最常用的数据类型。我们可以使用引号来创建字符串。
#Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
#Python字符串更新，你可以对已存在的字符串进行修改，并赋值给另一个变量
var1 = 'Hello World!'

print "Updated String :- ", var1[:6] + 'Python'

#Python字符串运算符

#Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
print "名字是%s,年龄是%d" % ('dingyl',21)
#Python三引号（triple quotes）python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
#三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
#三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
#一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。


 #errHTML =
'''

<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>

'''
#引号前小写的"u"表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码
print u'Hello World !'

#Python 列表(Lists)
'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
'''
#访问
list1 = ['1','2','3','4']
list2 = ['Python','James','Nancy']
print list1
print list1[0];print list1[1];print list2[1:3]
#添加新数据
print "The Value is list[2]"
print list[2]
print "The New Value is list[2]"
list[2]=2001
print list[2]
#删除数据
print "The Value is list[2]"
print list1
print "The New Value is list[2]"
del list1[2]
print list1

#Python列表脚本操作符
#列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
#Python列表截取(切片)
L = ['spam', 'Spam', 'SPAM!']
print L[2] #读取列表中第三个元素
print L[-2] #读取列表中倒数第二个元素
print L[1:]#从第二个元素开始截取列表
#Python列表函数&方法
print cmp(list1,list2)
print len(list1)
print max(list1)
print min(list1)

#List(seq)将元组转换为列表
#方法
list1.append(5)#在列表末尾添加新的对象
print list1
print list1.count(1)#统计某个元素在列表中出现的次数
list1.extend(list2)#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print list1
print list1.index('1') #从列表中找出某个值第一个匹配项的索引位置
list1.insert(5,'6') #将对象插入列表
print list1
list1.pop(1)#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print list1
list1.remove(5)#移除列表中某个值的第一个匹配项
print list1
list1.reverse()#反向列表中元素
print list1
list1.sort()#对原列表进行排序
print list1

#Python 元组
'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup1 = ();#创建空元组
tup1 = (50,);#元组中只包含一个元素时，需要在元素后面添加逗号
#访问元组
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
#修改元组：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;

#删除元组:元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''
tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;
print "After deleting tup : "
print tup
'''
#无关闭分隔符:任意无符号的对象，以逗号隔开，默认为元组
print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;

#Python 字典(Dictionary)
'''
字典是另一种可变容器模型，且可存储任意类型对象，如其他容器模型。
字典由键和对应值成对组成。字典也被称作关联数组或哈希表。基本语法如下
'''
dict = {'James':21,'Nancy':22,'Susan':23}
'''
每个键与值用冒号隔开（:），每对用逗号分割，整体放在花括号中（{}）。
键必须独一无二，但值则不必。
值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。
'''
print dict
print "dict['James']:",dict['James']#访问字典里的值
#修改字典:向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict1 = {'Name':'James','School':'BeiJing','Age':28}
print dict1
dict1['Name']=27#修改字典对应值
print dict1
dict1['Class']='First'
print dict1

'''
删除字典元素
字典键的特性
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
'''
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print "dict['Name']: ", dict['Name'];
#2）键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行，如下实例：
'''
dict = {['Name']: 'Zara', 'Age': 7};

print "dict['Name']: ", dict['Name'];
'''
#字典内置函数&方法
#Python字典包含了以下内置函数：
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };
print cmp(dict1,dict2)#比较两个字典元素。
print len(dict1)#计算字典元素个数，即键的总数。
print type(dict1)#返回输入的变量类型，如果变量是字典就返回字典类型。

#Python字典包含了以下内置函数：
'''
	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	radiansdict.has_key(key)
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
以列表返回一个字典所有的键
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
以列表返回字典中的所有值
'''
#Python 日期和时间
import  time
'''
什么是Tick？
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python附带的受欢迎的time模块下有很多函数可以转换常见日期格式。如函数time.time()用ticks计时单位返回从12:00am, January 1, 1970(epoch) 开始的记录的当前操作系统时间, 如下实例:
'''
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks
#Tick单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年某日
#获取当前时间
localtime = time.localtime(time.time())
print "Local current time :", localtime
#获取格式化的时间:你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime
a = time.time()
print a
l = time.localtime(a)
print l
s = time.asctime(l)
print s

#获取某月日历,Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import  calendar
cal = calendar.month(2015,12)
print "This month"
print(cal)
aa = time.ctime()#直接显示当前时间
print aa
print aa
'''
Time模块
Time模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：
序号	函数及描述
1	time.altzone
返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
2	time.asctime([tupletime])
接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
3	time.clock( )
用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
4	time.ctime([secs])
作用相当于asctime(localtime(secs))，未给参数相当于asctime()
5	time.gmtime([secs])
接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
6	time.localtime([secs])
接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
7	time.mktime(tupletime)
接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
8	time.sleep(secs)
推迟调用线程的运行，secs指秒数。
9	time.strftime(fmt[,tupletime])
接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
根据fmt的格式把一个时间字符串解析为时间元组。
11	time.time( )
返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
12	time.tzset()
根据环境变量TZ重新初始化时间相关设置。
Time模块包含了以下2个非常重要的属性：
序号	属性及描述
1	time.timezone
属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
2	time.tzname
属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

日历（Calendar）模块
此模块的函数都是日历相关的，例如打印某月的字符月历。
星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
序号	函数及描述
1	calendar.calendar(year,w=2,l=1,c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
2	calendar.firstweekday( )
返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
3	calendar.isleap(year)
是闰年返回True，否则为false。
4	calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数。
5	calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
6	calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
7	calendar.monthrange(year,month)
返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
8	calendar.prcal(year,w=2,l=1,c=6)
相当于 print calendar.calendar(year,w,l,c).
9	calendar.prmonth(year,month,w=2,l=1)
相当于 print calendar.calendar（year，w，l，c）。
10	calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）。
11	calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
12	calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
'''

#Python函数
'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
语法
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。
实例
以下为一个简单的Python函数，它将一个字符串作为传入参数，再打印到标准显示设备上。
'''

def printme( str ):
    "显示字符串"
    print str
    return
'''
函数调用
定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
如下实例调用了printme（）函数：
'''
# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

#按值传递参数和按引用传递参数:所有参数（自变量）在Python里都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

# 可写函数说明
def changeme(mylist):
    "显示列表"
    mylist.append([1,2,3,4])
    print "函数内参数", mylist
    return
#调用函数
mylist = [10,20]
changeme(mylist)
print "函数外参数", mylist

def printinfo(age,name):
    print "Age",age
    print "Name",name
    return
printinfo(age=50,name="Nacci")

#缺省参数:调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
def printinfo(name,age=30):
    print "Name:",name
    print "Age:",age
    return age
printinfo('Page',20)
printinfo( name="miki" );

#不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
#匿名函数
'''
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda函数的语法只包含一个语句，如下
'''
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )


#局部变量和全局变量
'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
'''
total = 0 #外部变量
def sum(age1,age2):
    total = age1 + age2
    print "内部变量",total
    return total
sum(10,20)
print "外部变量",total

def test(test1,test2):
    total = test1 * test2
    print "内部变量：",total
    return
test(10,20)
print "外部变量：", total

import  math
content=dir (math)
print content

#Python 模块，具体看为知笔记
'''
模块让你能够有逻辑地组织你的Python代码段。
把相关的代码分配到一个 模块里能让你的代码更好用，更易懂。
模块也是Python对象，具有随机的名字属性用来绑定或引用。
简单地说，模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。
命名空间和作用域
变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。
一个Python表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
Python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
因此，如果要给全局变量在一个函数里赋值，必须使用global语句。
global VarName的表达式会告诉Python， VarName是一个全局变量，这样Python就不会在局部命名空间里寻找这个变量了。
例如，我们在全局命名空间里定义一个变量money。我们再在函数内给变量money赋值，然后Python会假定money是一个局部变量。
然而，我们并没有在访问前声明一个局部变量money，结果就是会出现一个UnboundLocalError的错误。取消global语句的注释就能解决这个问题。
'''
#Python中的包:包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的Python的应用环境

#Python 文件I/O
#打印到屏幕
print "Python是最好的语言，不是么？"
import  fileinput
#读取键盘输入
#raw_input
#str = raw_input("Please input your key")
#print str
#input
#input([prompt]) 函数和raw_input([prompt]) 函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。
#str1 = input("Please input your value")
#print str1
#需要输入Python表达式[x*5 for x in range(2,10,2)]

#打开和关闭文件
#你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的辅助方法才可以调用它进行读写。
#打开一个文件

fo = open("foo.txt","wb")
print "File name is ",fo.name
print "File is closed",fo.closed
print "File`s mode",fo.mode
print "Softspace flag : ", fo.softspace

#Close()方法
#File对象的close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
#当一个文件对象的引用被重新指定给另一个文件时，Python会关闭之前的文件。用close（）方法关闭文件是一个很好的习惯。

# 打开一个文件
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# 关闭打开的文件
fo.close()

#Write()方法:Write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
#Write()方法不在字符串的结尾不添加换行符('\n')：
fo = open("foo.txt","wb")
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()
fo =open("foo.txt","r")
print fo
#read()方法
str = fo.read()
print "foo.txt的内容是：",str
#打开一个文件
fo = open("foo.txt","r+")
str = fo.read(10)
print "Read String is",str
#查找当前位置
position = fo.tell()
print "Current file position",position
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str
# 关闭打开的文件
fo.close()

#重命名和删除文件:Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。:要使用这个模块，你必须先导入它，然后可以调用相关的各种功能。
#rename()方法需要两个参数，当前的文件名和新文件名。
import  os
#os.rename( "test1.txt", "test1.txt" )

#remove()方法
#你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
#os.remove("test1.txt")

#mkdir()方法:可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
#os.mkdir("test")
#chdir()方法:可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
#os.chdir("newdir")
#getcwd()方法显示当前的工作目录。
str = os.getcwd()
print str

#rmdir()方法删除目录，目录名称以参数传递。:在删除这个目录之前，它的所有内容应该先被清除。

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2


































