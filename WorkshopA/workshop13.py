def studentNumber( ) :
    studentNum = int(input('จำนวนนักเรียน : '))
    return studentNum

def calGrade(gradeAvg) :
    if gradeAvg > 2.00 :
        return 'สอบผ่าน'
    else :
        return 'สอบไม่ผ่าน'
    
def loopAndShow( ) :
    for i in range( studentNumber( ) ) :
        studentID = int(input('รหัสนักเรียน : '))
        studentName = input('ชื่อนักเรียน : ')
        gradeAvg = float(input('เกรดเฉลี่ยนักเรียน : '))
        print(f'{studentID} {studentName} คุณได้เกรด {gradeAvg} และคุณ {calGrade(gradeAvg)}')

loopAndShow( )
