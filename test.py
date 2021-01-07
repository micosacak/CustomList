from the_class import CustomList
def test():
	q1 = CustomList(0,1,2,3,4,5,([6,[7,[8,range(9,12)]]]),[12,13,14,15,16,[(17,18,19,20,21,range(22,30))]])
	print(q1.sum([range(0,10),[([(range(0,10))])]]))
	print(q1.sum((0,1,2,3,4,5,([6,[7,[8,range(9,12)]]]),[12,13,14,15,16,[(17,18,19,20,21,range(22,30))]])))
	print(q1.sum())
	print(q1.mean())
	print(q1.std())
	print(q1.var())

if __name__ == "__main__":
	test()
