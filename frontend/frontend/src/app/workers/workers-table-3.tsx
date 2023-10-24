'use client';

import React from "react";
import { getWorkers } from "./workersSearcher";
import WorkerTable from "./worker-table";

export default async function WorkersTable3() {
    const [page, setPage] = React.useState(0);
    const [perPage, setPerPage] = React.useState(10);
    const [filterValue, setFilterValue] = React.useState('');
    
    const workersData = await getWorkers(page, perPage, filterValue);
    const workers = workersData?.results;
    const totalWorkers = workersData?.count;

    return (
        <> 
        {/* filter */}
        <p>filter</p>
        
        {/* table */}
        <p>table</p>

        {/* pagination */}
        <p>pagination {totalWorkers}</p>
        </>
    )
}