import uvicorn

def dev():
    uvicorn.run("fast.main:app", reload=True)