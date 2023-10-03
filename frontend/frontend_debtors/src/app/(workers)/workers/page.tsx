'use client'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'reactstrap'

import { Table } from "reactstrap";

import WorkerInterface from "./workerInterface";

async function getWorkers(page: number=1, perPage: number=1000) {
    const backend = process.env.BACKEND_URL;
    const response = await fetch(
        `${backend}/api/workers?page=${page}&page_size=${perPage}`,
        { cache: 'no-store' }
    );
    const workers = await response.json();
    return workers?.results as WorkerInterface[];
}


export default async function Workers() {
    const workers = await getWorkers();
    
    return (
        <>
        <h1>all workers</h1>
        
        <Table 
            hover
            responsive
        >
            <thead>
                <tr>
                    <th>name</th>
                    <th>contact info</th>
                    <th>role</th>
                </tr>
            </thead>
            <tbody>
                {workers.map((worker) => (
                    
                    <tr key={worker.id}>
                        <td>{worker.name}</td>
                        <td>{worker.contact_info}</td>
                        <td>{worker.role}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
        </>
    )
}