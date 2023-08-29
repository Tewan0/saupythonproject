#เชื่อม/ต่อ/รวม ข้อมูลหลายๆ ประเภทเข้าด้วยกัน
#1ใช้ ,
score = 500
print('Hello...',20,True,432.4324,12/2,"Hi...",score)
#2ใช้ +
print('Hello...'+' '+str(20)+' '+str(True)+' '+str(432.4324)+' '+str(12/2)+' '+"Hi..."+' '+str(score))
#3ใช้ เมธอต format
print('Hello... {} {} {} {} Hi... {}'.format(20,True,432.4324,12/2,score))
#4ใช้ f-string
print(f'Hello... {20} {True} {432.4324} {12/2} Hi... {score}')
#5ใช้ modular operator %
print('Hello... %d %f %s Hi...' % (20, 17.5, "SAU"))
