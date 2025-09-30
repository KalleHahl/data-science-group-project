from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main_route()-> dict[str, str]:
    return {"message": "Hello Wine Enjoyer =)"}

@app.get('/wine')
def wine_route(description: str) -> dict[str, str]:
    return {"message": f"This is your description {description}"}