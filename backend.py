from fastapi import FastAPI,Depends
from database.db import DBManager
from RAG_Services.agent import rag_agent
import uvicorn
from RAG_Services.fecther import search_db
app = FastAPI()

def get_db_manager():
    return DBManager()
@app.post("/query")
async def queries(user_request:str,db_manager:DBManager=Depends(get_db_manager)):
    try:
        context  = search_db(query=user_request,topk=15,db_manager=db_manager)
        response = await rag_agent.run(
            query=user_request,
            context=context
        )
        answer = response.output.response
        return {"answer":answer}
    except Exception as e:
        print("the exception:",str(e))
    
def backend(port=8021,reload=True):
    uvicorn.run(
        "backend:app",
        host="127.0.0.1",
        port=port,
        reload=reload,
        workers=1,
    )

if __name__ =="__main__":
    try:
        backend()
    except Exception as e:
        print("application terminated with error:",e)
        raise