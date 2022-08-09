from email import message
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


def callback(ch, method, properties, body):
    # Playload = body.decode("utf-8")
    # Playload = ast.literal_eval(Playload)
    with open("G:\Protocols\SendingImageUsingRabbitMQSToS\ recive.jpg", "wb") as fi:
        fi.write(body)
        print(type(body))
        print("Image Recieved...")


channel.basic_consume(
    queue='image', on_message_callback=callback, auto_ack=True
)
print("Waitng for message clik CTRL+C to exit")
channel.start_consuming()
