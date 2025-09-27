import pytest
from pyspark.sql import SparkSession
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.pyspark_task import get_products_with_categories

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName("TestApp").getOrCreate()

def test_products_with_categories(spark):
    products = spark.createDataFrame(
        [(1, "Молоко"), (2, "Хлеб"), (3, "Сыр")],
        ["id", "name"]
    )
    categories = spark.createDataFrame(
        [(1, "Молочные"), (2, "Выпечка")],
        ["id", "name"]
    )
    product_category = spark.createDataFrame(
        [(1, 1), (2, 2)],  # молоко -> молочные, хлеб -> выпечка
        ["product_id", "category_id"]
    )

    df = get_products_with_categories(products, categories, product_category)

    result = {tuple(r) for r in df.collect()}
    expected = {
        ("Молоко", "Молочные"),
        ("Хлеб", "Выпечка"),
        ("Сыр", None)
    }
    assert result == expected