# Determine whether it is a valid function declaration
def isletter(c):
	return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')


def sparse_name(line : str):
	i = 0
	while i < len(line):
		if line[i] == '(':
			return i
		elif not isletter(line[i]) and line[i] != '_':
			return 0
		else:
			i += 1

	return i

def sparse_param(line : str):
	params = []
	i = 0
	while i < len(line):
		if line[i] == ' ':
			i += 1
		else:
			j = i+1
			brackets = 0
			while j < len(line):
				if line[j] == '(':
					brackets += 1
				elif line[j] == ')':
					brackets -= 1
				elif line[j] == ',' and brackets == 0:
					break
				j += 1
			params.append(line[i:j])
			i = j + 1	
	return params


	return params

def isFunc(line : str):
	return line.find("(") != -1


def isValidFunc(line : str, param_n : int):
	
	end_index_func_name = sparse_name(line)
	n = len(line)

	if not end_index_func_name or end_index_func_name == n:
		return False

	# print("Function Name:", line[:end_index_func_name])
	i = n-1
	while i >= 0 and line[i] == ' ':
		i -= 1
	if line[i] != ')':
		return False

	params = sparse_param(line[end_index_func_name+1:i])
	# print("Parameters:", params)
	if len(params) != param_n:
		return False

	for param in params:
		if isFunc(param) and not isValidFunc(param, param_n):
			return False
	
	return True


## test sparse_params:
# s = "      f(a, b)    , g(a, b), f(f(x),a,b,f(gxd),gggg(si,asi, f(gs0)), a"
## test isValudFunc()
# s = "f(f(q, g(b,x)), c(cc(c, b), a)"
# n = 2
# print("The input function is", "valid." if isValidFunc(s, n) else "invalid.")

# print(sparse_param(s))
# s = input("Please input a function:")
# n = int(input("Input a param number:"))
# print("The input function is", "valid." if isValidFunc(s, n) else "invalid.")



