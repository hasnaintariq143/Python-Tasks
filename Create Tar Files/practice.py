import zipfile

# zipping the files
new_file=zipfile.ZipFile('new_file.tar','w')

new_file.write('1.txt',compress_type=zipfile.ZIP_DEFLATED)
new_file.write('2.txt',compress_type=zipfile.ZIP_DEFLATED)

new_file.close()

# extracting the files

extract_files=zipfile.ZipFile('new_file.tar','r')
extract_files.extractall("new_file")
