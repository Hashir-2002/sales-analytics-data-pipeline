import pandas as pd
def classify_product(revenue):
    if revenue >=2000 :
        return "Top performer"
    elif revenue >1000:
        return "Good Performer"
    elif revenue >=500:
        return "Average Performer"
    else:
        return "Weak Performer"
def classify_customer(revenue_per_customer):
    if revenue_per_customer >=1500:
        return "VIP Customer"
    elif revenue_per_customer >=1000:
        return "High Value Customer"
    else :
        return "low Value Customer"
def transform_data(
        revenue_df,
revenue_per_product_df,
most_expensive_product_by_each_customer_df,
top_customer_df,revenue_per_customer_df
):
    revenue_per_customer_df["Value Of Customer"]=revenue_per_customer_df["REVENUE_PER_CUSTOMER"].apply(classify_customer)
    revenue_per_product_df["Performance"]=revenue_per_product_df["revenue"].apply(classify_product)
    return (revenue_df,
            revenue_per_product_df,
            most_expensive_product_by_each_customer_df,
            top_customer_df,
            revenue_per_customer_df)

