print("Welcome to Quiz game!! ")
print("-------------------------------")

guess = []
answer = ["A" , "B" ,"A" , "B" , "B"]
count = 0
b = 1 
while True:
    questions = {
        "Which of the following disorders is the fear of being alone?" :
        ["A. Agoraphobia" , "B. Aerophobia" , "C. Acrophobia", "D. Arachnophobia"] ,
        "What is the main component of the sun? " : 
        ["A. Liquid Lava" , "B. Gas" , "C. Molten iron" , "D. Rock"] ,
        "Which of the following animals can run the fastest? " : 
        ["A. Cheetah" , "B. Leopard", "C. Tiger" , "D. Lion"] , 
        "Where did the powers of Spiderman come from?"  :
        ["A. He was born with them" ,"B. He was bitten by a radioactive spider" ,
        "C. He went through a scientific experiment" ,
        "D. He woke up with them after a dream"] , 
        "In which country is Transylvania?" : 
        ["A. Bulgaria" , "B. Romania" , "C. Croatia" , "D. Serbia"]
    }

    for i , j in questions.items():
        print(i)
        for x in j:
            print(x)
        user = input("Make a guess: (A B C D): ").upper()
        guess.append(user)
    print("-------------------------------")
    print("Guess: " , end="")
    for i in guess:
        print(i , end = " ")
    print("\nAnswers:" , end = " ")
    for i in answer:
     print(i, end = " ")

    for i in guess:
        for j in answer[b-1]:
            b+=1
            if i == j :
                count += 1
                
                break 
    print(f"\nYou have got {count} points.")

    play = input("Do you want to play again? Y/n : ").lower()

    if play != "y":
        break 


