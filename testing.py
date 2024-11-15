def main(): 
    toss_history = []
    while True: 
        result = coin_toss().lower()
        toss_history.append(result)

        print()
        print('Your record: ')
        print(toss_history)
        print()

        number_of_win = won_count(toss_history)
        number_of_round = len(toss_history)

        win_rate = number_of_win/number_of_round*100

        history_prob = get_probability(number_of_round)*100

        win_prob_so_far = binom.pmf(k=number_of_win, n=number_of_round, p=0.5)*100

        next_round_win_prob = get_probability(1)*100

        print(f'Number of wins: {number_of_win}')
        print(f'Win rate: {win_rate:.5f}%')
        print(f'Probability of getting current win rate: {win_prob_so_far:.5f}%')
        print(f'Probability of the tossing history: {history_prob:.5f}%')
        print(f'Probability of winning the next round: {next_round_win_prob:.5f}%')
        print()

        if not play_again(): 
            break


def get_probability(round): 
    return 0.5**round

def won_count(history): 
    return history.count('won')
    

def coin_toss(): 
    options = ['head', 'tail']

    print('Select between head and tail. ')

    while True: 
        bet = input('Pick a side. \n').lower()
        if bet not in options: 
            print('Invalide input, try again')
        else: 
            break

    toss = random.choice(options)
    
    print()
    print(f'It is {toss}!')
    print()

    if toss == bet: 
        print('You won! ')
        return 'won'
    else: 
        print('You lost!')
        return 'lost'

def play_again(): 
    while True: 
        play_again = input('Want to try again? Yes/No \n').lower()
        if play_again == 'yes': 
            return True
        elif play_again == 'no': 
            print('See you next time! ')
            return False
        else: 
            print('Please select yes or no. ')

if __name__ == "__main__":
    main()
