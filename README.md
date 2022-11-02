# Vector.ai Assignment

Author: [Tushar Goel](mailto:tushar.goel.ml@gmail.com)

In this Assignment, 3 parts to be done

1. **Classifier** : Fashion MNIST (classifier folder). Seperate Readme in the folder
2. **Message-Broker** : To create a message broker like Apache Kafka, and Google Pub/Sub. See `message_brokers` folder
3. **Combined Architecture**:

   - FastAPI server which is serving the trained model for Fashion MNIST (by default), you can change in `api.py` file in model_name

   - Producer and Consumer files imported from `message_brokers`

## File Structure

1. **api.py** : This contains the FastAPI which is serving the model, when this API gets hit by consumer data, it predict and return status along with result, which can be seen in the consumer console.

2. **prodcuer.py** : This file contains producer code, which sends data one be one to the dedicated topic

3. **consumer.py** : This file contains consumer code, which when consume data hit the API through a callback function defined in `utils.py` file, and print result to console.

   Ex: `{"status":"Success","result":[2]}`

### Setup:

1. Run `pip3 install -r requirements.txt`

## How to run the code

1. First Make sure your message broker server is up and running. for eg: for Kafka by default is localhost:9092 is there.

2. Open a terminal, and run `python3 api.py`, it will start Model API
3. Open another terminal, and run `python3 consumer.py`, it is ready to consume data from producer

4. Open another terminal, and run `python3 producer.py`, it is ready to produce data.

5. Head over to `consumer` terminal, there you will see the output.

## Production Deployment

1. For the production deployment, we can use Google Cloud Platform
2. Model can be served on Tensorflow Serving/or through by Docker Image on Virtual Instance.
3. Using Google Cloud Pub/Sub Cloud Service, we already have implementation of it
4. Using above steps we can deploy the code into Production
