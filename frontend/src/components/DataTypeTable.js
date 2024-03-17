import React from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';

const DataTypeTable = ({ dataTypes }) => {
  if (!dataTypes) {
    return null;
  }

  return (
    <Paper sx={{ overflowX: "auto" }}>
      <Table sx={{ minWidth: 650, '& .MuiTableCell-root': { border: 1 }, '& .MuiTableCell-head': { backgroundColor: '#f5f5f5' } }}>
        <TableHead>
          <TableRow>
            <TableCell>Field Name</TableCell>
            <TableCell>Data Type</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {Object.entries(dataTypes).map(([key, value]) => (
            <TableRow key={key}>
              <TableCell>{key}</TableCell>
              <TableCell>{value}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default DataTypeTable;
