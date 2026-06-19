import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    pair_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name="count")
    result = pair_counts[pair_counts['count'] >= 3][['actor_id', 'director_id']]
    return result
    
    