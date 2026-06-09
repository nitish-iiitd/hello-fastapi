from fastapi import FastAPI

app = FastAPI(title="Hello FastAPI on Kubernetes")


@app.get("/")
def home():
    return {
        "message": "Hello Nitish, this is v2 running on Kubernetes",
        "app": "hello-fastapi",
        "version": "v2"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
