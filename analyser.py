import pandas as pd


def sum_sales(csv_file):
    df = pd.read_csv(csv_file)

    sum_sales = df.groupby(["Date"], as_index=False).sum()

    return sum_sales


def value_analyser(csv_file):
    df = pd.read_csv(csv_file)

    sum_sales = df.groupby(["Date"], as_index=False).sum()

    max_sales = sum_sales[sum_sales["Sale"] == sum_sales["Sale"].max()]
    max_sales_value = max_sales["Sale"].values[0]
    max_sales_date = max_sales["Date"].values[0]

    min_sales = sum_sales[sum_sales["Sale"] == sum_sales["Sale"].min()]
    min_sales_value = min_sales["Sale"].values[0]
    min_sales_date = min_sales["Date"].values[0]

    return [
        [max_sales_value, max_sales_date],
        [min_sales_value, min_sales_date],
    ]


def count_analyser(csv_file):
    df = pd.read_csv(csv_file)

    count_sales = df.groupby(["Date"], as_index=False).count()

    max_sales = count_sales[count_sales["Sale"] == count_sales["Sale"].max()]
    max_sales_value = max_sales["Sale"].values[0]
    max_sales_date = max_sales["Date"].values[0]

    min_sales = count_sales[count_sales["Sale"] == count_sales["Sale"].min()]
    min_sales_value = min_sales["Sale"].values[0]
    min_sales_date = min_sales["Date"].values[0]

    return [
        [max_sales_value, max_sales_date],
        [min_sales_value, min_sales_date],
    ]

