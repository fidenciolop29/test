from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("MongoSparkApp") \
        .config("spark.mongodb.input.uri", "mongodb://mongodb:27017/testdb.entrada") \
        .config("spark.mongodb.output.uri", "mongodb://mongodb:27017/testdb.salida") \
        .getOrCreate()

    # Leer datos desde MongoDB
    df = spark.read.format("mongo").load()
    print("Esquema de datos de entrada:")
    df.printSchema()
    print(f"Total registros: {df.count()}")
    
    # Mostrar primeros 5 registros (si hay datos)
    if df.count() > 0:
        df.show(5)
    else:
        print("No hay datos para mostrar en 'testdb.entrada'")

    # Si existen las columnas, filtramos solo ellas, si no dejamos todo
    columns_to_select = [c for c in ["campo1", "campo2"] if c in df.columns]
    if columns_to_select:
        df_result = df.select(*columns_to_select)
    else:
        df_result = df

    # Guardar resultados en MongoDB
    df_result.write.format("mongo").mode("overwrite").save()

    spark.stop()

if __name__ == "__main__":
    main()
