
import styles from './workers.module.css'

import { Card } from 'reactstrap'
import { 
    Table,
    TableContainer,
    TableHead,
    TableRow,
    TableCell,
    TableBody,
    TableFooter
} from '@mui/material'

import { WorkerInterface } from './workerInterface'
import { getWorkers } from './workersSearcher'
import Worker from './worker'
import WorkerPagination from './workerPagination'



export default async function Workers({
    searchParams,
}: {
    searchParams?: { [key: string]: string} | undefined
}) {
    const pageSearch = searchParams?.page ?? '0';
    const perPageSearch = searchParams?.perPage ?? '10';

    let page = parseInt(pageSearch);
    let perPage = parseInt(perPageSearch);

    let totalWorkers = (await getWorkers(1, 1)).count;

    if (page < 0) {
        page = 0;
    }
    if (page > (totalWorkers / perPage)) {
        page = (totalWorkers / perPage);
    }

    if (perPage < 0) {
        perPage = 10;
    }
    if (perPage > 500) {
        perPage = 500;
    }


    const columns = [
        {id: 'id', name: 'id'},
        {id: 'name', name: 'name'},
        {id: 'contact_info', name: 'contact info'},
        {id: 'role', name: 'role'},
    ]

    let data = await getWorkers(page, perPage);
    let workers = data.results;

    return (
        <section className={styles.workersCard}>
            <h1>All workers</h1>
            <Card>
                <TableContainer>
                    <Table size="small">
                        <TableHead>
                            <TableRow>
                                {columns.map((column: any) => (
                                    <TableCell key={column.id}>{column.name}</TableCell>
                                ))}
                            </TableRow>
                        </TableHead> 
                        <TableBody>
                            {workers?.map((worker: WorkerInterface) => {
                                return <Worker worker={worker} />;
                            })}
                        </TableBody>
                        </Table>
                        <WorkerPagination totalWorkers={totalWorkers} selectedPerPage={perPage} />
                </TableContainer>
                    {/*
                    <TableFooter>
                        pagination
                        <WorkerPagination page={page} perPage={perPage} />
                    </TableFooter>*/}
            </Card>
        </section>
    )
}