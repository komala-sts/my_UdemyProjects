from question_model import Question
#from data import question_data
from data_triviadb import question_data
from quiz_brain import qbrain

question_bank=[]

for item in question_data['results']:
    #q_t = question["text"]
    #q_a = question["answer"]
    q_t = item['question']
    q_a = item['correct_answer']
    new_q = Question(q_t,q_a)
    question_bank.append(new_q)

qno= 0
qb1 = qbrain()
for item in question_bank:
    qno +=1
    response = input(f"{qno}: {item.text} (True/False) ? ")

    if response.lower() == item.ans.lower():        
        qb1.tmark += 1
        print("Correct answer!")
    else:
        print(f"Wrong:-( The Correct answer is {item.ans}")
    print(f"Your current Score is :{qb1.tmark}")

print("You have completed the Quiz!")
print(f"Final Score is: {qb1.tmark}/{qno}")

