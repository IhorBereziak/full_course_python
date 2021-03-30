import zipfile
import os

folder_path = 'E:\\Programing\\Python_Complex\\you-tube_practice_video\\python\\full_course_python\\folder'
zip_path = 'E:\\Programing\\Python_Complex\\you-tube_practice_video\\python\\full_course_python\\folder\\test.zip'
name_zip = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write('E:\\Programing\\Python_Complex\\you-tube_practice_video\\python\\full_course_python\\folder\\test.zip',
#              '1.txt',
#              compress_type=zipfile.ZIP_DEFLATED)

for folder, subfolders, files in os.walk(folder_path):
    for file in files:
        if file == 'test.zip':
            continue
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), folder_path),
                     compress_type=zipfile.ZIP_DEFLATED)
my_zip.close()
