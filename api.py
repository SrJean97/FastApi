from http.client import HTTPException
from fastapi import FastAPI

from IsPrime import IsPrime_func

app = FastAPI()

#Get IsPrime
@app.get('/IsPrime/{num}')
def isprime_api(num : int) :
    try :
        return IsPrime_func(num)
    except :
        raise HTTPException(status_code=404, detail="IsPrime no encontrado")