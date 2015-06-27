import os
import sys
 
spark_home = os.environ.get('SPARK_HOME', None)
if not spark_home:
      raise ValueError('SPARK_HOME environment variable is not set')
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.1-src.zip'))
execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))