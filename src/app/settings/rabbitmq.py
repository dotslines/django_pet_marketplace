from app.settings.environ import env

RMQ_HOST = env("RMQ_HOST", default="localhost")
RMQ_PORT = env("RMQ_PORT", default=5672)
RMQ_USER = env("RMQ_USER", default="guest")
RMQ_PASS = env("RMQ_PASS", default="guest")

RMQ_ORDER_EXCHANGE = "order_exchange"
RMQ_ORDER_CREATED_QUEUE = "order_created_queue"
RMQ_ORDER_CREATED_ROUTING_KEY = "order.created.key"
