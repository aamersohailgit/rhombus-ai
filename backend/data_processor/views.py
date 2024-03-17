from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.infer_data_types import infer_and_convert_data_types
import pandas as pd
import os


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file", None)

        # Validate file presence
        if not file_obj:
            return Response(
                {"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validate file type
        if not file_obj.name.lower().endswith(".csv"):
            return Response(
                {"error": "Invalid file type. Only CSV files are supported."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            df = pd.read_csv(file_obj)

            # Data integrity check
            required_columns = ["Name", "Birthdate", "Score", "Grade"]
            if not all(column in df.columns for column in required_columns):
                return Response(
                    {"error": "Missing required columns in the file."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            df_processed = infer_and_convert_data_types(df)

            # Pagination parameters validation
            try:
                page = int(request.query_params.get("page", 1))
                page_size = int(request.query_params.get("page_size", 5))
            except ValueError:
                return Response(
                    {"error": "Page and page size must be valid integers."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if page < 1 or page_size < 1:
                return Response(
                    {"error": "Page and page size must be positive integers."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            MAX_PAGE_SIZE = 100
            if page_size > MAX_PAGE_SIZE:
                return Response(
                    {"error": f"Page size cannot exceed {MAX_PAGE_SIZE}."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Calculate total pages
            total_rows = df_processed.shape[0]
            total_pages = (total_rows + page_size - 1) // page_size

            # Slice the DataFrame for the requested page
            start = (page - 1) * page_size
            end = start + page_size
            df_paginated = df_processed.iloc[start:end]

            data = {
                "message": "File processed successfully",
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
                "data_types": df_processed.dtypes.astype(str).to_dict(),
                "data": df_paginated.astype(str).to_dict(orient="records"),
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"An error occurred while processing the file: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
