# PySpark Products-Categories Task

Решение тестового задания на PySpark: объединение продуктов и категорий.

## Задача
Есть три датафрейма:
- `products(id, name)`
- `categories(id, name)`
- `product_category(product_id, category_id)`

Нужно вернуть датафрейм с парами `(product_name, category_name)` и продуктами без категорий `(product_name, null)`.

## Пример использования

```python
from pyspark.sql import SparkSession
from src.pyspark_task import get_products_with_categories

spark = SparkSession.builder.master("local[*]").appName("Example").getOrCreate()

products = spark.createDataFrame(
    [(1, "Молоко"), (2, "Хлеб"), (3, "Сыр")],
    ["id", "name"]
)
categories = spark.createDataFrame(
    [(1, "Молочные"), (2, "Выпечка")],
    ["id", "name"]
)
product_category = spark.createDataFrame(
    [(1, 1), (2, 2)],
    ["product_id", "category_id"]
)

df = get_products_with_categories(products, categories, product_category)
df.show()
