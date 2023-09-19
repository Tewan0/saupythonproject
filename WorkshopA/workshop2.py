def inputStudentInformation ( ) :
    studentID = input('รหัสนักเรียน : ')
    studentName = input('ชื่อนักเรียน : ')
    return studentID, studentName
def test( ) :
    firstTestScore = int( input('คะแนนสอบครั้งที่ 1 : ') )
    secondTestScore = int( input('คะแนนสอบครั้งที่ 2 : ') )
    thirdTestScore = int( input('คะแนนสอบครั้งที่ 3 : ') )
    return firstTestScore, secondTestScore, thirdTestScore

def calAverage( studentID, studentName, firstTestScore, secondTestScore, thirdTestScore ) :
    averageTestScore = (firstTestScore + secondTestScore + thirdTestScore) / 3
    print(f'รหัสนักเรียน {str(studentID)} ชื่อนักเรียน {studentName} คะแนนสอบครั้งที่ 1 ได้ {firstTestScore} คะแนน คะแนนสอบครั้งที่ 2 ได้ {secondTestScore} คะแนน คะแนนสอบครั้งที่ 3 ได้ {thirdTestScore} คะแนน')
    print(f'ได้คะแนนเฉลี่ย = {int(averageTestScore)}')


studentID, studentName = inputStudentInformation ( )
firstTestScore, secondTestScore, thirdTestScore = test( )
calAverage( studentID, studentName, firstTestScore, secondTestScore, thirdTestScore )
