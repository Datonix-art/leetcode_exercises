import pandas as pd

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]

scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id': 'int64', 'score': 'float64'})

# def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
#     sorted_scores = scores['score'].sort_values(ascending=False)
#     new_data = [{'score': []}, {'rank': []}]
#     rank = 0
#     for score in sorted_scores:
#         new_data[0]['score'].append(score)
#         rank += 1
#         new_data[1]['rank'].append(rank)
#     new_table = pd.DataFrame(data=new_data, columns=['score', 'rank']).astype({'score': 'float64', 'rank': 'int64'})
#     return new_table

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values(by='score', ascending=False).reset_index(drop=True)
    sorted_scores['rank'] = sorted_scores['score'].rank(method='dense', ascending=False).astype(int)
    return sorted_scores[['score', 'rank']]


print(order_scores(scores).to_string(index=False))