"use client";

import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { Button, FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import { addOrModifyQueryParam, getQueryParamValue } from "@/app/(dashboardLayout)/layouts/shared/queryParams";


export default function WorkerPagination({ totalWorkers, selectedPerPage }: { totalWorkers: number, selectedPerPage: number }) {
    const router = useRouter();
    const pathname = usePathname();
    const searchParams = useSearchParams();

    const onPageChange = (pageChange: number) => {
        const current = new URLSearchParams(searchParams);

        const currentPage = getQueryParamValue('page', current.toString(), 0);
        const properPage = currentPage ? parseInt(currentPage)+pageChange : pageChange; 
        const query = addOrModifyQueryParam('page', properPage.toString(), current.toString());
        console.log("query", query);
        router.push(`${pathname}${query}`);
    }

    const handleChange = (event: React.SelectChangeEvent<{ value: number }>) => {
        const search = new URLSearchParams(searchParams);
        
        const selected = event.target.value;
        const query = addOrModifyQueryParam('perPage', selected.toString(), search.toString());
        router.push(`${pathname}${query}`);
    }

    return (
        <>
            <FormControl variant="standard" sx={{ m: 1, minWidth: 120 }}>
                <InputLabel id="demo-simple-select-label">Per Page</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={selectedPerPage}
                    label="Age"
                    onChange={handleChange}
                >
                <MenuItem value={10}>10</MenuItem>
                <MenuItem value={20}>20</MenuItem>
                <MenuItem value={50}>50</MenuItem>
                <MenuItem value={500}>500</MenuItem>
                </Select>
            </FormControl>
            <Button onClick={() => {
                onPageChange(-1);
            }}>
                left
            </Button>
            <Button onClick={() => {
                onPageChange(1);
            }}>
                right
            </Button>
        </>
    )
}