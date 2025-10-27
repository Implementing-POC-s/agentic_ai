# import the FastAPI app instance from a local file named server.py and .means the current package
from dotenv import load_dotenv
from .server import app
import uvicorn
# load dotenv before running the server
load_dotenv()
def main():
    # host="0.0.0.0" is a model host binding
    uvicorn.run(app,port=8000,host="0.0.0.0")
# by writing host here,,makes it accesible from any netwrok interface not just local host
main()