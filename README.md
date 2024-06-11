# apitest
# Publisher Subscriber Notification System

## Overview
This is a simple Publisher-Subscriber notification system implemented in Python using Flask. It allows subscribers to subscribe to topics, receive notifications for those topics, and unsubscribe from topics.

## How to Run Locally

### Prerequisites
- Python installed
- Flask installed (`pip install Flask`)
- VS Code installed

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/akshayram1/apitest.git
   cd apitest

2. **Create a virtual environment**:
   ```sh
   python -m venv env
3. **Activate the virtual environment**:
   ```sh
   source env/bin/activate

4. **install dependencies**:
    ```sh
    pip install Flask

5. Test the endpoints using Postman:

Subscribe:
            Method: POST
            URL: http://localhost:5000/subscribe
            Body: JSON
            json

            {
            "topicId": "example_topic",
            "subscriberId": "example_subscriber"
            }
Notify:
            Method: POST
            URL: http://localhost:5000/notify
            Body: JSON
            json

            {
            "topicId": "example_topic"
            }


Unsubscribe:
            Method: POST
            URL: http://localhost:5000/unsubscribe
            Body: JSON
            json

            {
            "topicId": "example_topic",
            "subscriberId": "example_subscriber"
            }



6. Postman Collection
    https://github.com/akshayram1/apitest/blob/main/api%20test.postman_collection.json