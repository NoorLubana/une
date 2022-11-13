total_lecture=int(input("Total lectures:"))
attended_lectures=int(input("Attended lectures:"))
eligibility_factor=(attended_lectures/total_lecture)*100
if eligibility_factor>=75:
    print("good")
else:
    print("not good")