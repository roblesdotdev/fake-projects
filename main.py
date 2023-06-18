if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fake_projects.app:app", reload=True)
