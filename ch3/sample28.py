
#40명의 학생에게 50~100점(50이상,100이하) 사이의 점수를 무작위로 할당한 딕셔너리 score를 제공한다
#각 문제의 정답을 제시하기 위한 소스코드를 작성하고 결과를 제시하시오
import random









#print(scores)

#40명의 학생의 평균
#avg = sum(scores.values()) / len(scores)
#print(avg)




#40명 중 최고 득점을 한 학생과 점수를 출력하시오.
#여러 명인 경우, 학번이 가장 빠른 한 명만 출력되도록 하시오.
scores = dict()
for i in range(11, 51):  # 11번부터 50번까지 40명
    scores['S' + str(i)] = random.randrange(50, 101)  # 50~100 사이의 랜덤 점수

# 최고 득점 계산
max_score = max(scores.values())  # 최고 점수
max_student = None  # 최고 점수를 받은 학생

# 최고 득점을 얻은 학생 찾기
for student, score in scores.items():
    if score == max_score:
        if max_student is None or int(student[1:]) < int(max_student[1:]):
            max_student = student

# 결과 출력
print(f"최고 득점 학생: {max_student}, 점수: {max_score}")