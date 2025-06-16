from fastapi.testclient import TestClient

from main import app


class TestModuleBase:

    def setup_method(self):
        self.client = TestClient(app)  # initialized before each test

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "Welcome to FastAPI with Clean Architecture!"
        }

    def test_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"message": "healthy"}
