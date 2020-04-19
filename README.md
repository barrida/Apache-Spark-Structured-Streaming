# SF Crime Data Project   

In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming.

# Step 1

The first step is to build a simple Kafka server.  
Complete the code for the server in producer_server.py and kafka_server.py.  

## Install packages

python get-pip.py  
pip install -r requirements.txt  

## Run zookeeper and server  
/usr/bin/zookeeper-server-start config/zookeeper.properties  

## Run server  
/usr/bin/kafka-server-start config/server.properties  

## Run workspace  
./start.sh  

## Run kafka server   
python kafka_server.py

## Run kafka-consumer-console  
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.dep.police.service --from-beginning  

## Check if your topic is created    
/usr/bin/kafka-topics --list --zookeeper localhost:2181  

# Step 2  

Apache Spark already has an integration with Kafka brokers, so we would not normally need a separate Kafka consumer. However, we are going to ask you to create one anyway. Why? We'd like you to create the consumer to demonstrate your understanding of creating a complete Kafka Module (producer and consumer) from scratch. In production, you might have to create a dummy producer or consumer to just test out your theory and this will be great practice for that.  
  
Implement all the TODO items in data_stream.py. You may need to explore the dataset beforehand using a Jupyter Notebook.  

Take a screenshot of your progress reporter after executing a Spark job. You will need to include this screenshot as part of your project submission.  

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*]  --conf spark.ui.port=3000 data_stream.py

# Step 3

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?  

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?  


# Appendix

## How to kill PID  
You might need to kill a process on a port. Install net-tools    

apt-get install net-tools  

Find the PID and kill  

netstat -tulpn | grep :2181  
netstat -tulpn | grep :3000  
kill -9 <pid_name>  
