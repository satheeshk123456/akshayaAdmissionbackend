from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from server.routes.admission_router import router as admission_router
from server.routes.admission_get_router import router as admission_get_router

app = FastAPI(title="User Registration API")


origins = [
    "http://localhost:4004",
    "http://127.0.0.1:4004",

]
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
     allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes


app.include_router(admission_router)
app.include_router(admission_get_router)


@app.get("/")
async def root():
    return {"message": "API Running"}
