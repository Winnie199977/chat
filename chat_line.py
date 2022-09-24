#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換內容
def convert(lines):
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_img_count = 0
	viki_work_count = 0
	viki_sticker_count = 0
	viki_img_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_work_count += len(m)
	print('allen說了', allen_word_count, '個字，傳了', allen_sticker_count, '個貼圖和', allen_img_count, '張圖片')
	print('viki說了', viki_work_count, '個字，傳了', viki_sticker_count, '個貼圖和', viki_img_count, '張圖片')

#寫入檔案
def write_file(filename, new):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in new:
			f.write(line + '\n')


#主程式
def main():
	lines = read_file('LINE.txt')
	lines = convert(lines)
	#write_file('output_LINE.txt', lines)

main()