import uvicorn
from app import create_app

kbqa = create_app()

if __name__ == '__main__':
    uvicorn.run(kbqa)
