""""

https://blog.csdn.net/pchwenwenti/article/details/83143345

pulsar manager 账号密码  "name": "admin", "password": "apachepulsar",

pip install pulsar-cleint

http://192.168.6.130:9527/#/login?redirect=%2Fmanagement%2Ftenants
"""
from auto_run_on_remote import run_current_script_on_remote
run_current_script_on_remote()

import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('my-topic36')

for i in range(10):
    producer.send(('Hello-%d' % i).encode('utf-8'))

client.close()


"""
import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe('my-topic', 'my-subscription')

while True:
    msg = consumer.receive()
    try:
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()
"""
