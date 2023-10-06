import { TableCell, TableRow } from "@mui/material";
import { WorkerInterface } from "./workerInterface";


export default function Worker( { worker }: { worker: WorkerInterface } ) {
    return (    
        <TableRow key={worker.id}>
            <TableCell>{worker.id}</TableCell>
            <TableCell>{worker.name}</TableCell>
            <TableCell>{worker.contact_info}</TableCell>
            <TableCell>{worker.role}</TableCell>
        </TableRow>
    )
}
