import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values(by='score', ascending=False).reset_index(drop=True)
    sorted_scores['rank'] = sorted_scores['score'].rank(method='dense', ascending=False).astype(int)
    return sorted_scores[['score', 'rank']]
