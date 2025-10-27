# before importing,,i should add the key
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI,Query
from .client.rq_client import queue
from .queues.worker import process_query
app=FastAPI()

@app.get("/")
def root():
    return {"status":"server is up and running"} 
# lets decorarte the function with post routr
@app.post('/chat')
def chat(
    # Query is a parameter
        query: str= Query(...,decription="the chat query of user")
):
    # this is just the jobid still job has not been completed
    job = queue.enqueue(process_query,query)
    # this job id might or might not be in the queue
    return{"status":"queued","job_id":job.id}
# need to reguster it
@app.get('/job-status')

def get_result(
        job_id:str=Query(...,decription="Job ID")
):
    # processing function to fetch the job
    job = queue.fetch_job(job_id=job_id)
    result=job.return_value()
    return{"result",result}

# whateever my processor function is returnonng is that what we want


     