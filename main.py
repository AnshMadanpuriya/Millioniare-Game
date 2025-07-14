questions = [
    ["Who is Salman Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote 'Harry Potter'?", "J.R.R. Tolkien", "William Shakespeare", "J.K. Rowling", "George R.R. Martin", 3],
    ["What is H2O commonly known as?", "Hydrogen", "Oxygen", "Water", "Salt", 3],
    ["Which animal is known as the King of the Jungle?", "Elephant", "Tiger", "Lion", "Leopard", 3],
    ["Which festival is known as the Festival of Lights in India?", "Holi", "Diwali", "Eid", "Christmas", 2],
    ["Which sport is Sachin Tendulkar associated with?", "Football", "Hockey", "Tennis", "Cricket", 4],
    ["Which is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet", 1],
    ["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", 2],
    ["Which gas do plants use for photosynthesis?", "Oxygen", "Carbon Monoxide", "Carbon Dioxide", "Nitrogen", 3]
]
prizes=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
i=0
for question in questions:
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
    i+=1