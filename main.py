import random
from scipy.stats import binom
import pandas as pd
import streamlit as st
from game_stats import cal_win_rate

st.set_page_config(
    page_title="What are the chances? A coin toss game. ", 
    layout='wide'
)

st.title('What are the chances? A coin toss game. ')
st.markdown('This app aims to demonstrate the various probability calculation in a game of coin toss. ')

st.header('Choose between head and tail. ')

if 'toss_history' not in st.session_state:
    st.session_state.bet_history = []
    st.session_state.toss_history = []
    st.session_state.win_history = []

bet = st.radio(
    label='Pick a side: ', 
    options=['Head', 'Tail']
)



if st.button('Toss it!'): 
    result = random.choice(['Head', 'Tail'])
    st.write(f'Result: {result}. ')

    st.session_state.bet_history.append(bet)

    if bet == result: 
        st.write('You won! ')
        st.session_state.win_history.append('Won')
    else: 
        st.write('You lost! ')
        st.session_state.win_history.append('Lost')
    st.session_state.toss_history.append(result)

if st.button('Restart'):
    st.session_state.bet_history = []
    st.session_state.toss_history = []
    st.session_state.win_history = []
    st.write("Game has been restarted!")

game_history, game_stats = st.columns([3, 7])

with game_history: 
    st.header('Game history')

    no_of_win = st.session_state.win_history.count('Won')
    no_of_round = len(st.session_state.win_history)

    st.write(f'You have {no_of_win} wins out of {no_of_round}. ')

    history_df = pd.DataFrame(
        {'Bet': st.session_state.bet_history, 
        'Result': st.session_state.toss_history, 
        'Win/lost': st.session_state.win_history}
        )

    history_df.index+=1

    st.write(history_df)

with game_stats: 
    win_rate = cal_win_rate(win = no_of_win, round = no_of_round)
    win_rate_percentage = win_rate*100
    st.header('Game stats')
    
    st.subheader('Win rate: ')
    st.write(f'{win_rate_percentage:.5f}%')

    st.latex(r' \text{win rate} = \frac{\text{total wins}}{\text{total rounds played}} ')
    st.latex(r' \text{win rate} = \frac{{' + str(no_of_win) + '}}{{' + str(no_of_round) + '}} ')
    st.latex(r' \text{win rate} = {' + str(win_rate) + '}')
    

# def main(): 
#     toss_history = []
#     while True: 
#         result = coin_toss().lower()
#         toss_history.append(result)

#         print()
#         print('Your record: ')
#         print(toss_history)
#         print()

#         number_of_win = won_count(toss_history)
#         number_of_round = len(toss_history)

#         win_rate = number_of_win/number_of_round*100

#         history_prob = get_probability(number_of_round)*100

#         win_prob_so_far = binom.pmf(k=number_of_win, n=number_of_round, p=0.5)*100

#         next_round_win_prob = get_probability(1)*100

#         print(f'Number of wins: {number_of_win}')
#         print(f'Win rate: {win_rate:.5f}%')
#         print(f'Probability of getting current win rate: {win_prob_so_far:.5f}%')
#         print(f'Probability of the tossing history: {history_prob:.5f}%')
#         print(f'Probability of winning the next round: {next_round_win_prob:.5f}%')
#         print()

#         if not play_again(): 
#             break


# def get_probability(round): 
#     return 0.5**round

# def won_count(history): 
#     return history.count('won')
    

# def coin_toss(): 
#     options = ['head', 'tail']

#     print('Select between head and tail. ')

#     while True: 
#         bet = input('Pick a side. \n').lower()
#         if bet not in options: 
#             print('Invalide input, try again')
#         else: 
#             break

#     toss = random.choice(options)
    
#     print()
#     print(f'It is {toss}!')
#     print()

#     if toss == bet: 
#         print('You won! ')
#         return 'won'
#     else: 
#         print('You lost!')
#         return 'lost'

# def play_again(): 
#     while True: 
#         play_again = input('Want to try again? Yes/No \n').lower()
#         if play_again == 'yes': 
#             return True
#         elif play_again == 'no': 
#             print('See you next time! ')
#             return False
#         else: 
#             print('Please select yes or no. ')

# if __name__ == "__main__":
#     main()

