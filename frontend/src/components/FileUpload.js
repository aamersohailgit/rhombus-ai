import React, { useState } from 'react';
import { Button, TextField, Typography, Box, CircularProgress, Container, Grid } from '@mui/material';
import DataTypeTable from './DataTypeTable';
import DataTable from './DataTable';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [responseData, setResponseData] = useState(null);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file first.');
      return;
    }

    setUploading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/data/upload/', {
        method: 'POST',
        body: formData,
      });

      setUploading(false);
      if (response.ok) {
        const result = await response.json();
        alert('File uploaded successfully.');
        console.log(result);
        setResponseData(result);
        setPage(result.page - 1);
        setRowsPerPage(result.page_size);
      } else {
        alert('Failed to upload file.');
        setResponseData(null);
      }
    } catch (error) {
      console.error('Upload error:', error);
      alert('An error occurred while uploading the file.');
      setUploading(false);
      setResponseData(null);
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ textAlign: 'center', my: 4 }}>
      <h1>Data Type Inference Tool</h1>
        <Typography variant="h6" gutterBottom>
          Upload a CSV File Only
        </Typography>
        <form onSubmit={handleSubmit} noValidate autoComplete="off">
          <TextField
            variant="outlined"
            type="file"
            onChange={handleFileChange}
            fullWidth
            sx={{ mb: 2 }}
            InputLabelProps={{ shrink: true }}
          />
          <Button
            variant="contained"
            color="primary"
            type="submit"
            disabled={uploading}
            fullWidth
          >
            {uploading ? <CircularProgress size={24} /> : 'Upload'}
          </Button>
        </form>
      </Box>
      {responseData && (
        <Grid container spacing={4}>
          <Grid item xs={12}>
            <Typography variant="h5" gutterBottom>Data Types</Typography>
            <DataTypeTable dataTypes={responseData.data_types} />
          </Grid>
          <Grid item xs={12}>
            <Typography variant="h5" gutterBottom>Uploaded Data</Typography>
            <DataTable
              data={responseData.data}
              page={page}
              setPage={setPage}
              rowsPerPage={rowsPerPage}
              setRowsPerPage={setRowsPerPage}
              total={responseData.total_pages * rowsPerPage}
            />
          </Grid>
        </Grid>
      )}
    </Container>
  );
}

export default FileUpload;
