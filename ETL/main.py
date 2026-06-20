from extract import extract_data
from transform import *
from load import load_data


revenue_df,revenue_per_product_df,most_expensive_product_by_each_customer_df,top_customer_df,revenue_per_customer_df = extract_data()

revenue_df,revenue_per_product_df,most_expensive_product_by_each_customer_df,top_customer_df,revenue_per_customer_df = transform_data(
    revenue_df,
    revenue_per_product_df,
    most_expensive_product_by_each_customer_df,
    top_customer_df,
    revenue_per_customer_df
)


load_data(
            revenue_df,
            revenue_per_product_df,
            most_expensive_product_by_each_customer_df,
            top_customer_df,
            revenue_per_customer_df
)


print(revenue_per_customer_df)