import pandas as pd

def load_data(
            revenue_df,
            revenue_per_product_df,
            most_expensive_product_by_each_customer_df,
            top_customer_df,
            revenue_per_customer_df
):
    revenue_df.to_csv("../outputs/revenue.csv",index=False)
    revenue_per_customer_df.to_csv("../outputs/revenue_per_customer.csv",index=False)
    most_expensive_product_by_each_customer_df.to_csv("../outputs/most_expensive_product_by_each_customer_df.csv",index=False)
    revenue_per_product_df.to_csv("../outputs/revenue_per_product_df.csv",index=False)
    top_customer_df.to_csv("../outputs/top_customer_df.csv",index=False)
    return "Successful"

