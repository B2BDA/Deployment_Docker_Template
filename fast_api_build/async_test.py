import pytest
from httpx import AsyncClient

from fastAPI_test import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
    
    
    
# curl -X POST -H "Content-Type: application/json" -d '{"var": -1.2,"skw": -5.2,"kur": 5.2,"etp": 3.5}' http://localhost/predict/ & curl -X POST -H "Content-Type: application/json" -d '{"var": -1.2,"skw": -5.2,"kur": 5.2,"etp": 3.5}' http://localhost/predict/