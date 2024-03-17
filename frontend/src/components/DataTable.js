import React from 'react';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { Paper } from '@mui/material';

const DataTable = ({ data, rowsPerPage }) => {
  // Convert your data to the format expected by DataGrid
  const rows = data.map((item, index) => ({ id: index, ...item }));
  const columns = [
    { field: 'Name', headerName: 'Name', width: 130 },
    { field: 'Birthdate', headerName: 'Birthdate', width: 130 },
    { field: 'Score', headerName: 'Score', type: 'number', width: 90 },
    { field: 'Grade', headerName: 'Grade', width: 90 },
  ];

  return (
    <Paper style={{ height: 400, width: '100%', overflowX: 'auto' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={rowsPerPage}
        rowsPerPageOptions={[5, 10, 20]}
        components={{
          Toolbar: GridToolbar,
        }}
        checkboxSelection
        disableSelectionOnClick
      />
    </Paper>
  );
};

export default DataTable;
