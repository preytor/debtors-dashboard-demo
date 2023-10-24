'use client';

import { Button, ButtonGroup, Input } from "@nextui-org/react";
import { Spinner } from "@nextui-org/spinner";
import {   
    Table,
    TableHeader,
    TableBody,
    TableColumn,
    TableRow,
    TableCell
} from "@nextui-org/table";
import React from "react";
import { HiOutlineSearch } from "react-icons/hi";
import { BiFilterAlt } from "react-icons/bi";
import SearchFieldWorkers from "./search-field-workers";

import { GoMoveToStart, GoChevronLeft, GoChevronRight, GoMoveToEnd } from "react-icons/go";
import { getWorkers } from "./workersSearcher";


export default function WorkersTable() { 
    let filterValue = '';
    const [page, setPage] = React.useState(0);
    const [perPage, setPerPage] = React.useState(10);

    const [isLoading, setIsLoading] = React.useState(true);

    const columns = [
        {key: 'id', label: 'id'},
        {key: 'name', label: 'name'},
        {key: 'contact_info', label: 'contact info'},
        {key: 'role', label: 'role'},
    ]
    const workers: any = getWorkers(page, perPage, filterValue);
    
    console.log("workers: ", workers.results);
    function getWorkersPaginationText() {
        return <p>Showing {(1*perPage)*page} - {perPage} of {workers.count}</p>;
    }

    return (
        <div className="container max-w-3xl px-4 mx-auto sm:px-8">
            <div className="py-8">
                <SearchFieldWorkers page={page} perPage={perPage}  />
                <div className="px-4 py-4 -mx-4 overflow-x-auto sm:-mx-8 sm:px-8">
                    <div className="inline-block min-w-full overflow-hidden rounded-lg shadow">
                        <Table className="min-w-full leading-normal">
                            <TableHeader columns={columns}>
                                {columns.map((column) => (
                                    <TableColumn key={column.key}>{column.label}</TableColumn>
                                ))}
                            </TableHeader>
                            <TableBody>
                                {workers!.results.map((worker: any) => (
                                    <TableRow key={worker.id}>
                                        <TableCell>{worker.id}</TableCell>
                                        <TableCell>{worker.name}</TableCell>
                                        <TableCell>{worker.contact_info}</TableCell>
                                        <TableCell>{worker.role}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                        <div className="flex items-center justify-end pt-2">
                            {getWorkersPaginationText()}
                            <ButtonGroup>
                                <Button 
                                    type="button"
                                    isIconOnly  
                                    aria-label="Go to beginning"
                                    className="text-gray-600 bg-white hover:bg-gray-100">
                                    {<GoMoveToStart />}
                                </Button>
                                <Button 
                                    type="button"
                                    isIconOnly  
                                    aria-label="Previous Page"
                                    className="text-gray-600 bg-white hover:bg-gray-100">
                                    {<GoChevronLeft />}
                                </Button>
                                <Button 
                                    type="button"
                                    isIconOnly  
                                    aria-label="Next Page"
                                    className="text-gray-600 bg-white hover:bg-gray-100">
                                    {<GoChevronRight />}
                                </Button>
                                <Button 
                                    type="button"
                                    isIconOnly  
                                    aria-label="Go to End"
                                    className="text-gray-600 bg-white hover:bg-gray-100">
                                    {<GoMoveToEnd />}
                                </Button>
                            </ButtonGroup>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )


    /*
    return (
        <Table
            isHeaderSticky
            bottomContent={
                hasMore && !isLoading ? (
                    <div className="flex w-full justify-center">
                    <Button isDisabled={workers.isLoading} variant="flat" onPress={workers.loadMore}>
                      {workers.isLoading && <Spinner color="white" size="sm" />}
                      Load More
                    </Button>
                  </div>
                ) : null
            }
        >
            <TableHeader>
                {columns.map((column: any) => (
                    <TableColumn key={column.id}>{column.name}</TableColumn>
                ))}
            </TableHeader>
            <TableBody
                emptyContent={"No rows to display."}
                isLoading={isLoading}
                items={workers.items}
                loadingContent={<Spinner label="Loading..." />}
            >
                {[]}
            </TableBody>
        </Table>
    )*/

    
    function onClear() {
    }

    function onSearchChange(e: any) {
        filterValue += e;
        console.log("search change", e)
    }
}