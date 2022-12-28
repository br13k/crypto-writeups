import os


files = os.listdir('Task_files')

for file in files:
	text = ''
	if file.find('.html') != -1:
		with open('Task_files/'+file, 'r', encoding='utf8') as file2:
			for line in file2:
				text += line
	if text.find('1337.html') != -1:
		print(file)
