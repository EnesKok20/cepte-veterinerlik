from fastapi import FastAPI

app = FastAPI(
    title="Cepte Veterinerlik API",
    description=(
        "Bireysel evcil hayvan sahipleri ve çiftlik işletmecileri için " "AI destekli backend API."
    ),
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Cepte Veterinerlik API ayakta"}
