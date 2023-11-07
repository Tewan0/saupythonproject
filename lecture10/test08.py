# ลบไฟล์
import os
from os import remove

if os.path.exists("myfile01.txt") :
    # os.remove("myfile01.txt")
    remove("myfile01.txt")
    print('ลบไฟล์เรียบร้อยแล้ว')
else :
    print('ไฟล์ที่จะลบไม่มี')