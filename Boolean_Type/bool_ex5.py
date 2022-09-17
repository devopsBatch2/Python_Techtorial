







exam1 = 60
exam2 = 40
exam3 = 90

attendency = 80

avg_score =exam1*20/100+ exam2*30/100 +exam3*50/100

is_attendency_enough = attendency >= 80
is_avg_score_enough = avg_score >= 65

can_pass = is_attendency_enough and is_avg_score_enough

print("Attendency of the student", attendency)
print("Average score of the student", avg_score)
print("Student can pass the class" , can_pass)
