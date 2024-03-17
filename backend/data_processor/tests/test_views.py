from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class FileUploadViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("file-upload")
        self.test_files_dir = "data_processor/tests/test_files"

    def test_upload_valid_csv(self):
        file_path = os.path.join(self.test_files_dir, "valid_sample_data.csv")
        with open(file_path, "rb") as file:
            response = self.client.post(self.url, {"file": file}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("File processed successfully", response.data["message"])

    def test_upload_invalid_file_type(self):
        file_path = os.path.join(self.test_files_dir, "invalid_sample_data.txt")
        with open(file_path, "rb") as file:
            response = self.client.post(self.url, {"file": file}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_without_file(self):
        response = self.client.post(self.url, {}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_pagination_parameters(self):
        file_path = os.path.join(self.test_files_dir, "valid_sample_data.csv")
        with open(file_path, "rb") as file:
            response = self.client.post(
                self.url + "?page=abc&page_size=-1", {"file": file}, format="multipart"
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_csv_missing_required_columns(self):
        file_path = os.path.join(self.test_files_dir, "missing_columns_data.csv")
        with open(file_path, "rb") as file:
            response = self.client.post(self.url, {"file": file}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
