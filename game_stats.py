from scipy.stats import binom

def cal_win_rate(win, round): 
    if round==0: 
        return 0
    else: 
        return win/round
    
def get_probability(prob, round): 
    return prob**round if round > 0 else 0

def probability_current_win_rate(win, round, p): 
    if round==0: 
        return 0
    else: 
        return binom.pmf(k=win, n=round, p=p)
    
def main(): 
    score=probability_current_win_rate(2, 4, 0.5)
    print(score)

if __name__ == "__main__":
    main()
