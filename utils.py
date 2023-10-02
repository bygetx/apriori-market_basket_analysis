import pandas as pd
import numpy as np


def sort_by(data):
    data = data.sort_values(["lift", "support"],
                            ascending=False).reset_index(drop=True)
    return data


def conv_to_df(ass: list) -> pd.DataFrame:
    pairs, supports, confs, lifts = [], [], [], []
    for item in ass:
        pair = item[0][0]
        items = [x for x in pair]
        target = [x for x in item[0][1]]
        pairs.append(" , ".join(items[:]) + " -> "+str(target[0]))
        confs.append(item[0][2])
        lifts.append(item[0][3])
        supports.append(item[1])
    pass
    d = {}
    d["items"] = pairs
    d["support"] = supports
    d["confidence"] = confs
    d["lift"] = lifts
    df2 = pd.DataFrame(d, columns=[
                       "items", "support", "confidence", "lift"], index=np.arange(len(pairs)))
    return df2


# gets order statistic(that was nested in main list) and the support value
def get_order_static(ass_result) -> list:
    ass_ordered = []
    for record in ass_result:
        support = record[1]
        for i in range(len(record.ordered_statistics)):
            ass_ordered.append((record.ordered_statistics[i], support))
    return ass_ordered


def no_more_nans(store_data: pd.DataFrame) -> list:
    list_of_lists = store_data.values.tolist()
    new_l = []
    for l in list_of_lists:
        cleaned_list = [value for value in l if not pd.isna(value)]
        new_l.append(cleaned_list)
    return new_l


def lower_all(store_data: pd.DataFrame):
    for col in store_data.columns:
        store_data[col] = store_data.apply(
            lambda x: x[col].lower() if not pd.isna(x[col]) else x[col], axis=1)
    return store_data
