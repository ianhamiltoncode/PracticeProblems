import pdb

def product_of_others(inputx):
	output = []
	product = 1
	for x in range(len(inputx)):
		for y in range(len(inputx)):
			product = product * inputx[y]
		product = product/inputx[x]
		output.append(product)
		product = 1
	return output

test = [1, 2, 3, 4, 5]
test = [3, 2, 1]
print(product_of_others(test))