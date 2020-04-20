# SF Crime Data Project   

In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming.

# Development Environment
You may choose to create your project in the workspace we provide here, or if you wish to develop your project locally, you will need to set up your environment properly as described below:  

Spark 2.4.3  
Scala 2.11.x  
Java 1.8.x  
Kafka build with Scala 2.11.x  
Python 3.6.x or 3.7.x  

**For Windows:**    
Please follow the directions found in this helpful StackOverflow post: https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows  

# Beginning the Project  
This project requires creating topics, starting Zookeeper and Kafka servers, and your Kafka bootstrap server. You’ll need to choose a port number (e.g., 9092, 9093..) for your Kafka topic, and come up with a Kafka topic name and modify the zookeeper.properties and server.properties appropriately.  

## Install packages

```
python get-pip.py  
pip install -r requirements.txt  
```

## Run zookeeper and server  
```
/usr/bin/zookeeper-server-start config/zookeeper.properties 
/usr/bin/kafka-server-start config/server.properties  
```

## Run workspace  
```
./start.sh  
```

# Step 1

- The first step is to build a simple Kafka server.  
- Complete the code for the server in producer_server.py and kafka_server.py.  


## Run kafka server 
```
python kafka_server.py
```

## Run kafka-consumer-console  
```
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.dep.police.service --from-beginning  
```

## Check if your topic is created    
```
/usr/bin/kafka-topics --list --zookeeper localhost:2181  
```

![Kafka Consumer Console Output](https://github.com/barrida/Apache-Spark-Structured-Streaming/blob/master/screenshots/Step%201%20-%20kafka-consumer-console-output.PNG)

# Step 2  

Apache Spark already has an integration with Kafka brokers, so we would not normally need a separate Kafka consumer. However, we are going to ask you to create one anyway. Why? We'd like you to create the consumer to demonstrate your understanding of creating a complete Kafka Module (producer and consumer) from scratch. In production, you might have to create a dummy producer or consumer to just test out your theory and this will be great practice for that.  
  
Implement all the TODO items in data_stream.py. You may need to explore the dataset beforehand using a Jupyter Notebook.  

**Run spark-submit**  
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*]  --conf spark.ui.port=3000 data_stream.py
```

**Progress reporter after executing a Spark job**  

![Progress Reporter](https://github.com/barrida/Apache-Spark-Structured-Streaming/blob/master/screenshots/Step%202%20-%20progress-reporter(2).PNG)

**Spark Streaming UI as the streaming continues**  

![Spark Streaming UI](https://github.com/barrida/Apache-Spark-Structured-Streaming/blob/master/screenshots/Step%202%20-%20Spark%20Streaming%20UI.PNG)


# Step 3

- How did changing values on the SparkSession property parameters affect the throughput and latency of the data?  

- What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?  


# Appendix

## How to kill PID  
You might need to kill a process on a port. Install net-tools    

```
apt-get install net-tools  
```

Find the PID and kill  

```
netstat -tulpn | grep :2181  
netstat -tulpn | grep :3000  
kill -9 <pid_name>  
```
