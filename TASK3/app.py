import fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return 'hello world'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)