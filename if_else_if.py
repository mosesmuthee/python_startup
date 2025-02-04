# no conditions in the else if
score=float(input("What did you Get?"))
if score>=90:
    grade=" Wow, congratulations for attaining an (A)!"
elif score>=80:
    grade="Marvelous work done (A-)"
elif score>=65:
    grade="Work Harder (B+)"
elif score>=59:
    grade="Improve (B)"
elif score>=40:
    grade="Work smarter (B-)"
elif score>=35:
    grade="Very poor score (C)"
elif score<=34:
    grade="Failure, you failed (F)"

print(grade)
