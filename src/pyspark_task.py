from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_products_with_categories(
    products: DataFrame, categories: DataFrame, product_category: DataFrame
) -> DataFrame:
    result = (
        products
        .join(product_category, products["id"] == product_category["product_id"], "left")
        .join(categories, product_category["category_id"] == categories["id"], "left")
        .select(
            products["name"].alias("product_name"),
            categories["name"].alias("category_name")
        )
    )
    return result