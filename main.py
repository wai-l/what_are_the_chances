import random
from scipy.stats import binom
import pandas as pd
import streamlit as st
from game_stats import cal_win_rate, get_probability, probability_current_win_rate

st.set_page_config(
    page_title="What are the chances? A coin toss game. ", 
    layout='wide'
)

st.title('What are the chances? A coin toss game. ')
st.markdown('This app aims to demonstrate various probability concepts in a game of coin toss. ')

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

game_history, game_stats = st.columns(2)

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
    historic_prob = get_probability(prob=0.5, round=no_of_round)
    historic_prob_percentage = historic_prob*100
    win_rate_prob = probability_current_win_rate(win = no_of_win, round = no_of_round, p = 0.5)
    win_rate_prob_percentage = win_rate_prob*100
    next_round_prob_percentage = 0.5*100

    stats_table = {
        "Metrics": [
            'Win rate', 
            'Probability of the toss history', 
            'Probability of the current win rate', 
            'Probability of winning the next round'
        ], 
        "Stats": [
            f"{win_rate_percentage:.5f}%",
            f"{historic_prob_percentage:.5f}%",
            f"{win_rate_prob_percentage:.5f}%",
            f"{next_round_prob_percentage:.5f}%"
        ]
    }

    stats_df = pd.DataFrame(stats_table)

    stats_df.index+=1

    st.header('Game stats')
    st.table(stats_df)
    
    
st.header('Game stats information ')

st.subheader('Win rate ')
st.write('You will notice that the more rounds you play, the closer the win rate gets to 50%. This is a demonstration of **The Law of Large Number**, which states that as the number of trials increases, the sample mean (win rate) will converge to the population mean. ')

st.latex(r' \text{win rate} = \frac{\text{total wins}}{\text{total rounds played}} ')

# 

st.subheader('Probability of the toss history ')
st.write('This is the probability of getting the tossing results recorded in the game history. For example, if you\'ve played 3 rounds and the pattern is Head, Tail, Head, the probability of getting this result is $0.5^3 = 0.125$. This is a demonstration of probability in sequence. ')

st.latex(r'P(H)=0.5')
st.latex(r'P(T)=0.5')
st.latex(r'P(H, T, H) = 0.5 * 0.5 * 0.5')
st.latex(r'P(H, T, H) = 0.5^3')
st.latex(r'P(H, T, H) = 0.125')

code_toss_history='''prob=0.5**number_of_rounds'''
st.code(code_toss_history, language='python')

# 

st.subheader('Probability of the current win rate ')

st.write('The probability of getting k wins from n rounds. Say you played 4 rounds and won 2 times, this statistic shows the probability of getting that set ratio of rounds won and played. This is a classic example of binomial distribtuion. ')

st.latex(r'P(x=k) = \frac{n!} {k!(n-k)!} * p^k (1-p)^{n-k}')
st.latex(r'k = \text{number of success}')
st.latex(r'n = \text{number of trials}')
st.latex(r'p = \text{probability of success on a given trial}')

st.write('**n-choose-k**')
st.write('Assume k=2, n=4, p=0.5')
st.latex(r'\text{n-choose-k}=\frac{n!} {k!(n-k)!}')
st.latex(r'\text{n-choose-k}=\frac{4*3*2*1} {2*1(2*1)}')
st.latex(r'\text{n-choose-k}=\frac{4*3*2*1} {2*1(2*1)}')
st.latex(r'\text{n-choose-k}=6')

st.write('**Probability of each outcome**')
st.latex(r'p^k (1-p)^{n-k}')
st.latex(r'p^k (1-p)^{n-k}=0.5^2 (1-0.5)^2')
st.latex(r'p^k (1-p)^{n-k}=0.25 * 0.25')
st.latex(r'p^k (1-p)^{n-k}=0.0625')

st.write('**Binomial distribtuion**')
st.latex(r'P(x=k) = 6 * 0.0625')
st.latex(r'P(x=k) = 0.375')

# 

st.subheader('Probability of winning the next round ')
st.write('In a game of coin toss, each toss is an individual event, the previous coin toss doesn\'t impact the probability of the next coin toss. Therefore the probabiliy for winning the next round is always 0.5. ')
