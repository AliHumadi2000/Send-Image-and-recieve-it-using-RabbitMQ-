from email import message
from http import server
import queue
import pika

# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# create channe from the connection
channel = connection.channel()

# declare the name of the queue
channel.queue_declare(queue='image')
# create class to send message


class Image(object):
    __slots__ = ['filename']

    def __init__(self, filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, 'rb') as im:
            data = im.read()
        return data


# create object from the class
image = Image(filename="G:\Protocols\SendingImageUsingRabbitMQSToS\mine.jpg")
data = image.get
channel.basic_publish(exchange='', routing_key='image', body=data)

connection.close()
