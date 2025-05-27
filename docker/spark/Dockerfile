FROM bitnami/spark:3.3.2

# Instala pyspark y conector Mongo si hace falta en runtime
USER root
RUN pip install pyspark==3.3.2

# Bitnami ya viene con Spark configurado
USER 1001
