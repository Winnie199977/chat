#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換內容
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen' #現在說話的人
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		#如果 person 有值
		if person:
			new.append(person + ': ' + line)
	return new

#寫入檔案
def write_file(filename, new):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in new:
			f.write(line + '\n')


#主程式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()