from app.main.config.app import app
import uvicorn

def start():
    uvicorn.run(app, debug=True, host='0.0.0.0', port=8000)

if __name__ == "__main__":
    start()