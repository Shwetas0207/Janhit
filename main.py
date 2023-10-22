from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route import user, admin

app = FastAPI()

app.include_router(user.router, prefix='/user')
app.include_router(admin.router, prefix='/admin')

# Allow requests from your HTML file's origin
origins = [
    "http://localhost:8000",
    "https://localhost.com:8000",
    "https://127.0.0.1:8000",
    "http://127.0.0.1:5500", 
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Running the app with HTTPS support via Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
