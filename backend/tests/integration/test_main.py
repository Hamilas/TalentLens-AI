import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from src.app.main import app


class TestMainEndpoints:
    """Test main application endpoints."""

    def test_root_endpoint(self):
        """Test root endpoint returns correct structure and content."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.get("/")
        
        # Assert
        assert response.status_code == 200
        
        data = response.json()
        assert data["success"] is True
        assert "TalentLens" in data["message"]
        assert "data" in data
        assert "service" in data["data"]
        assert "version" in data["data"]
        assert "status" in data["data"]
        assert "timestamp" in data["data"]

    def test_info_endpoint(self):
        """Test info endpoint returns correct structure and content."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.get("/info")
        
        # Assert
        assert response.status_code == 200
        
        data = response.json()
        assert data["success"] is True
        assert data["message"] == "Application information retrieved successfully"
        assert "data" in data
        
        info_data = data["data"]
        assert info_data["name"] == "TalentLens-AI"
        assert info_data["description"] == "A production-ready AI-powered interview transcript analysis platform"
        assert "version" in info_data
        assert "environment" in info_data
        assert "storage_type" in info_data
        assert "features" in info_data
        assert "ai_models" in info_data
        assert "timestamp" in info_data

    def test_root_endpoint_response_structure(self):
        """Test root endpoint response structure in detail."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/")

        # Assert
        assert response.status_code == 200
        body = response.json()
        assert "success" in body
        assert "message" in body
        assert "data" in body
        assert body["success"] is True
        assert isinstance(body["data"], dict)
        assert "service" in body["data"]
        assert "version" in body["data"]
        assert "status" in body["data"]
        assert "timestamp" in body["data"]

    def test_info_endpoint_response_structure(self):
        """Test info endpoint response structure in detail."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/info")

        # Assert
        assert response.status_code == 200
        body = response.json()
        assert "success" in body
        assert "message" in body
        assert "data" in body
        assert body["success"] is True
        assert isinstance(body["data"], dict)
        assert "name" in body["data"]
        assert "version" in body["data"]
        assert "description" in body["data"]
        assert "environment" in body["data"]
        assert "storage_type" in body["data"]
        assert "features" in body["data"]
        assert "ai_models" in body["data"]
        assert "timestamp" in body["data"]

    def test_root_endpoint_content_type(self):
        """Test root endpoint returns correct content type."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.get("/")
        
        # Assert
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"

    def test_info_endpoint_content_type(self):
        """Test info endpoint returns correct content type."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.get("/info")
        
        # Assert
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"

    def test_root_endpoint_method_not_allowed(self):
        """Test root endpoint with wrong HTTP method."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.post("/")
        
        # Assert
        assert response.status_code == 405
        body = response.json()
        assert body["success"] is False
        assert "error" in body
        assert body["error"]["code"] == 405

    def test_info_endpoint_method_not_allowed(self):
        """Test info endpoint with wrong HTTP method."""
        # Arrange
        client = TestClient(app)
        
        # Act
        response = client.post("/info")
        
        # Assert
        assert response.status_code == 405
        body = response.json()
        assert body["success"] is False
        assert "error" in body
        assert body["error"]["code"] == 405

    def test_root_endpoint_data_values(self):
        """Test root endpoint returns expected data values."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/")

        # Assert
        assert response.status_code == 200
        body = response.json()
        assert body["message"] == "TalentLens-AI"
        data = body["data"]
        assert data["service"] == "TalentLens-AI"
        assert data["version"] == "1.0.0"
        assert data["status"] == "running"

    def test_info_endpoint_data_values(self):
        """Test info endpoint returns expected data values."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/info")

        # Assert
        assert response.status_code == 200
        body = response.json()
        data = body["data"]
        assert data["name"] == "TalentLens-AI"
        assert data["version"] == "1.0.0"
        assert data["description"] == "A production-ready AI-powered interview transcript analysis platform"
        assert data["environment"] == "development"
        assert data["storage_type"] == "memory"

    def test_root_endpoint_no_optional_fields(self):
        """Test root endpoint doesn't have unexpected top-level fields."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/")

        # Assert
        assert response.status_code == 200
        body = response.json()
        expected_keys = {"success", "message", "data"}
        assert set(body.keys()) == expected_keys
        expected_data_keys = {"service", "version", "status", "timestamp"}
        assert set(body["data"].keys()) == expected_data_keys

    def test_info_endpoint_no_optional_fields(self):
        """Test info endpoint doesn't have unexpected top-level fields."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/info")

        # Assert
        assert response.status_code == 200
        body = response.json()
        expected_keys = {"success", "message", "data"}
        assert set(body.keys()) == expected_keys
        expected_data_keys = {
            "name",
            "description",
            "version",
            "environment",
            "storage_type",
            "features",
            "ai_models",
            "timestamp",
        }
        assert set(body["data"].keys()) == expected_data_keys
