 print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    #check wether the answer is correct or not
    choose=int(input("Enter your answer :\n1 for a\n2 for b\n3 for c\n4 for d\n"))
    if(question[5]==choose):
        print("Correct Answer")
    else:
        print(f"Incorrect,The correct answer is : {question[5]}")
        print("Best of Luck for next Time!!")
        break
    print(f"You won {prizes[i]} $")