from httpx import AsyncClient

async def test_add_specific_operation(ac: AsyncClient):
    transport = ac.transport
    response = await transport.request("POST", "/operations", json={
        "id": 1,
        "quantity": "string",
        "figi": "string",
        "instrument_type": "string",
        "date": "2024-03-11T00:00:00",
        "type": "string"
    })
    assert response.status_code == 201
