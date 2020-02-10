def DigitHangman():
    question = input("Enter the question : ")
    puzzle = question.split()
    answer_list = []
    guess_time = 0
    WrongGuess = ''
    if len(puzzle) != 12:
        print('Question must has 12 numbers')
        return False
    for i in puzzle:
        if int(i) > 9 or int(i) < 0:
            print('Number must be 0-9')
            break
    for i in range(len(puzzle)):
        answer_list.append("-")
    while guess_time < 5:
        answer = ''
        for i in answer_list:
            answer = answer + i + ' '
        print(answer,WrongGuess)
        guess = input("Guess : ")
        for i in range(len(puzzle)):
            if puzzle[i] == guess:
                answer_list[i] = guess
            elif guess not in puzzle:
                WrongGuess += (guess+' ')
                break
        guess_time += 1
    print(answer,WrongGuess)
    print(12-answer_list.count('-'))
DigitHangman()
