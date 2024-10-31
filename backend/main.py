import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()


@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "name": "Vika",
            "img": "https://www.svgrepo.com/show/530190/rabbit.svg",
        },
        {
            "id": 2,
            "name": "Vanya",
            "img": "https://www.svgrepo.com/show/530182/crab.svg",
        },
        {
            "id": 3,
            "name": "Serega",
            "img": "https://www.svgrepo.com/show/530193/polar-bear.svg",
        },
    ]
    random.shuffle(items)
    return items


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
         "http://localhost:5173",
         "http://194.247.187.229",
        #"https://site-test-deploy1.ru",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
