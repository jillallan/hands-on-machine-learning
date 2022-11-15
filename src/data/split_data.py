def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)