# 第四章 递归

# 4.3 计算整数列表和
def listsum(list_):

	if len(list_) == 1:
		return list_[0]
	else:
		return list_[0] + listsum(list_[1:])

print(listsum([1,3,5,7,9]))

# 4.5 整数转换为任意进制字符串
def toStr(num, base):
	convertString = '0123456789ABCDEF'
	if num < base:
		return convertString[num]
	else:
		return toStr(num//base, base) + convertString[num%base]

print(toStr(1453, 16))

# 4.6 栈帧
from pythonds.basic.stack import Stack

def toStr(n, base, rstack):
	convertString = '0123456789ABCDEF'
	while n > 0:
		if n < base:
			rstack.push(convertString[n])
		else:
			rstack.push(convertString[n % 16])

		n = n // base

	res = ''
	while not rstack.isEmpty():
		res = res + str(rstack.pop())
	return res

rstack = Stack()
print(toStr(1453, 16, rstack))

# 第五章 排序与搜索
# 5.1 顺序查找，复杂度O(n)
# 列表无序
def sequentialSearch(alist, item):
	pos = 0
	found = False
	while pos < len(alist) and not found: 
		if alist[pos] == item:
			found = True
		else:
			pos += 1
	return found

# 列表有序
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False

	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos += 1
	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))

# 5.2 二分查找 复杂度：O(log n)

def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while not found and first <= last:
		midpoint = (first + last) // 2
		if item == alist[midpoint]:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1

	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

# 递归版本
def binarySearch_r(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while not found and first <= last:
		midpoint = (first + last) // 2
		if item == alist[midpoint]:
			found = True
		else:
			if item < alist[midpoint]:
				return binarySearch_r(alist[:midpoint], item)

			else:
				return binarySearch_r(alist[midpoint+1:], item)

	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch_r(testlist, 3))
print(binarySearch_r(testlist, 13))

# 5.3 Hash 查找
class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] + self.size

# 5.7 冒泡排序: 比较相邻项并交换无序项，每次遍历将下一个最大值放在正确的位置上，复杂度O(n^2)
def bubbleSort(alist):
	for passum in range(len(alist)-1, 0 ,-1):
		for i in range(passum):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# 短冒泡排序
def shortBubbleSort(alist):
	exchanges = True
	passum = len(alist) -1 
	while passum > 0 and exchanges:
		exchanges = False
		for i in range(passum):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				exchanges = True
		passum = passum - 1

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# 选择排序：遍历将最大值放在正确的位置上, 复杂度O(n^2)
def selectionSort(alist):
	for fillslot in range(len(alist)-1, 0, -1):
		positionofMax = 0
		for location in range(1, fillslot+1):
			if alist[positionofMax] < alist[location]:
				positionofMax = location
		alist[fillslot], alist[positionofMax] = alist[positionofMax], alist[fillslot]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

# 插入排序：复杂度O(n^2)
# 它始终在列表的较低位置维护一个排序的子列表，
# 然后将每个新项 “插入” 回先前的子列表，使得排序的子列表称为较大的一个项。
def insertionSort(alist):
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position] = alist[position-1]
			position = position - 1

		alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

# 希尔排序：
# 通过将原始列表分解为多个较小的子列表来改进插入排序，每个子列表使用插入排序进行排序。
# 选择这些子列表的方式是希尔排序的关键。
# 不是将列表拆分为连续项的子列表，希尔排序使用增量i（有时称为 gap），
# 通过选择 i 个项的所有项来创建子列表。

# 合并排序, 复杂度O(nlogn)
# 归并排序是一种递归算法，不断将列表拆分为一半。
# 如果列表为空或有一个项，则按定义（基本情况）进行排序。
# 如果列表有多个项，我们分割列表，并递归调用两个半部分的合并排序。
# 一旦对这两半排序完成，就执行称为合并的基本操作。
# 合并是获取两个较小的排序列表并将它们组合成单个排序的新列表的过程。
def mergeSort(alist):
	print('splitting', alist)
	if len(alist) > 1:
		mid = len(alist) // 2
		left = alist[:mid]
		right = alist[mid:]

		mergeSort(left)
		mergeSort(right)

		i=0
		j=0
		k=0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i += 1
			else:
				alist[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			alist[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			alist[k] = right[j]
			j += 1
			k += 1
	print('merging', alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

# 快速排序: 复杂度O(nlogn)
# 快速排序算法通过多次比较和交换来实现排序，其排序流程如下：
# (1)首先设定一个分界值，通过该分界值将数组分成左右两部分;
# (2)将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。
# 此时，左边部分中各元素都小于或等于分界值，而右边部分中各元素都大于或等于分界值;
# (3)通过递归将左侧部分排好序后，再递归排好右侧部分的顺序。
def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
	if first < last:
		keypoint_p = doSort(alist, first, last)
		quickSortHelper(alist, first, keypoint_p-1)
		quickSortHelper(alist, keypoint_p+1, last)

def doSort(alist, first, last):
	pivotvalue = alist[first]
	left = first + 1
	right = last
	done = False

	while not done:

		while left <= right and alist[left] <= pivotvalue:
			left += 1
		while left <= right and alist[right] >= pivotvalue:
			right -= 1


		if left > right:
			done = True
		else:
			alist[left], alist[right] = alist[right], alist[left]

	# 此时的右标记位置即为分割点，将枢轴值与分割点的内容进行交换，
	# 即：分割点左侧的值都小于枢轴值，右侧的值都大于枢轴值；
	alist[first], alist[right] = alist[right], alist[first]

	return right


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)