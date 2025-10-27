from redis import Redis
from rq import Queue
# Below is baically the connection from rq which is using Reddis at the backend
queue=Queue(connection=Redis(

    host="localhost",
    port="6379"

))
def process_query(query: str):
    {"processing": query}

queue.enqueue(process_query,"tell me about current jobs") 
# now lets setup the fastapi and tiw up all the thing
