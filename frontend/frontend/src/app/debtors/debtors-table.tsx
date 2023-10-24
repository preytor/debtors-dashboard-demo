'use client'

import { Table, TableBody, TableCell, TableColumn, TableHeader, TableRow } from "@nextui-org/react"
import { getDebtors } from "./debtors-searcher"
import { DebtorsInterface } from "./debtors-interface"


export default async function DebtorsTable({ page, perPage, args }: { page: number, perPage: number, args: string }) {
    const columns = [
        {key: 'id', label: 'id'},
        {key: 'name', label: 'name'},
        {key: 'contact_info', label: 'contact info'},
        {key: 'legal_status', label: 'legal status'},
    ]
    const debtors = await getDebtors(page, perPage, args)

    return (
        <Table className="min-w-full leading-normal">
            <TableHeader columns={columns}>
                {columns.map((column) => (
                    <TableColumn key={column.key}>{column.label}</TableColumn>
                ))}
            </TableHeader>
            <TableBody>
                {debtors!.results.map((debtors: DebtorsInterface) => (
                    <TableRow key={debtors.id}>
                        <TableCell>{debtors.id}</TableCell>
                        <TableCell>{debtors.name}</TableCell>
                        <TableCell>{debtors.contact_info}</TableCell>
                        <TableCell>{debtors.legal_status}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    )
}