from flask import Flask, request, jsonify

app = Flask(__name__)


class PublisherSubscriberSystem:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topic_id, subscriber_id):
        if topic_id not in self.topics:
            self.topics[topic_id] = set()
        self.topics[topic_id].add(subscriber_id)

    def notify(self, topic_id):
        notifications = []
        if topic_id in self.topics:
            subscribers = self.topics[topic_id]
            for subscriber in subscribers:
                message = f"Notification sent to {subscriber} for topic {topic_id}"
                print(message)
                notifications.append(message)
        else:
            notifications.append(f"No subscribers found for topic {topic_id}")
            print(notifications[-1])
        return notifications

    def unsubscribe(self, topic_id, subscriber_id):
        if topic_id in self.topics and subscriber_id in self.topics[topic_id]:
            self.topics[topic_id].remove(subscriber_id)
            message = f"Subscriber {subscriber_id} unsubscribed from topic {topic_id}"
            print(message)
            return message
        else:
            message = f"Subscriber {subscriber_id} is not subscribed to topic {topic_id}"
            print(message)
            return message


system = PublisherSubscriberSystem()


@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()
    if not data or "topicId" not in data or "subscriberId" not in data:
        return jsonify({"error": "Invalid request, missing topicId or subscriberId"}), 400

    topic_id = data["topicId"]
    subscriber_id = data["subscriberId"]
    system.subscribe(topic_id, subscriber_id)
    return jsonify({"message": "Subscribed successfully"}), 200


@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    if not data or "topicId" not in data:
        return jsonify({"error": "Invalid request, missing topicId"}), 400

    topic_id = data["topicId"]
    notifications = system.notify(topic_id)
    return jsonify({"message": "Notifications sent", "notifications": notifications}), 200


@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    data = request.get_json()
    if not data or "topicId" not in data or "subscriberId" not in data:
        return jsonify({"error": "Invalid request, missing topicId or subscriberId"}), 400

    topic_id = data["topicId"]
    subscriber_id = data["subscriberId"]
    message = system.unsubscribe(topic_id, subscriber_id)
    return jsonify({"message": message}), 200


if __name__ == "__main__":
    app.run(debug=True)
