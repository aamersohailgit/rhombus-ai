# Data Type Inference Tool

This project is a web application designed to allow users to upload CSV files, infer data types, and view the uploaded data along with inferred data types. It provides functionalities such as file uploading, data type inference, data display with pagination, and exporting filtered data to CSV.

## Features

- **File Upload**: Users can upload CSV files to be processed.
- **Data Type Inference**: The application automatically infers data types for each column in the uploaded CSV.
- **Data Display**: Uploaded data and inferred data types are displayed in tables.
- **Pagination**: Supports pagination for the displayed data table.
- **Filtering**: Users can filter the data displayed in the table.
- **Export**: Users can export the filtered data to a CSV file.

## Tech Stack

- **Frontend**: React.js, Material-UI
- **Backend**: Django REST Framework
- **Database**: (Optional) SQLite/PostgreSQL (if data persistence is required)
- **Containerization**: Docker

## Project Structure

- `backend/`: Django REST Framework project for handling file uploads and data processing.
- `frontend/`: React application for the user interface.

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository

2. Build and run the Docker containers:
    - `docker-compose up --build`

    This command builds the Docker images for the backend and frontend, starts the containers, and binds the necessary ports.

    - Backend API is accessible at `http://localhost:8000`.

3. Access the application:
    - go to `cd frontend`
    - run `npm install`
    - run `npm start`
    - Frontend is accessible at `http://localhost:3000`.

### Using the Application

1. Navigate to the frontend URL in your browser.
2. Use the "Upload a File" button to select and upload a CSV file.
3. View the inferred data types and the uploaded data in the displayed tables.
4. Use the filter input to filter data and the export button to download the data as CSV.

4. Note Make sure to stop backend container

    - `docker-compose down -v`

### Backend Development

Navigate to the `backend/` directory to work on the Django REST Framework project.

### Frontend Development

Navigate to the `frontend/` directory to develop the React application.

### Author : Aamer