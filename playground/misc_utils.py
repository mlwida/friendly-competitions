import pandas as pd

# There has to be a better way ...
def keep_cids_with_num_entries(df_input, group_by_columns, num_entries):
    count_per_group = pd.DataFrame(df_input.groupby(group_by_columns).size()).reset_index()
    all_cols = group_by_columns.copy()
    all_cols.append("count")
    count_per_group.columns = all_cols
    return df_input.loc[df_input["customerId"].isin(count_per_group.loc[count_per_group["count"] == num_entries]["customerId"].unique()), :].copy(deep=True)
