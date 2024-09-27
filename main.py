from fastapi import FastAPI
from router import doc

app= FastAPI()

# app.include_router(blog.router)
app.include_router(doc.router)