'use client'

import { useState } from "react";

import { Button, Input } from "@nextui-org/react";
import { BiFilterAlt } from "react-icons/bi";
import { HiOutlineSearch } from "react-icons/hi";


export default function SearchFieldWorkers({ page, perPage }: { page: number, perPage: number }) {
    const [query, setQuery] = useState('');

    const handleSubmit = async (e: any) => {
        e.preventDefault();
        const response = await fetch(`http://localhost:8001/api/workers?page=${page}&perPage=${perPage}&name=${query}`);
        const data = await response.json();
        console.log(data);

        return data;
    }

    return (
        <>
            <div className="flex flex-row justify-between w-full mb-1 sm:mb-0">
                <h2 className="text-2xl leading-tight">
                    Workers
                </h2>
                <div className="text-end">
                    <form 
                        onSubmit={handleSubmit} 
                        className="flex flex-col justify-center w-3/4 max-w-sm space-y-3 md:flex-row md:w-full md:space-x-3 md:space-y-0">
                        <div className=" relative ">     
                            <Input 
                                id="&quot;form-workers-Filter" 
                                className=" rounded-lg border-transparent flex-1 appearance-none w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent" 
                                placeholder="Search by name..."
                                startContent={<HiOutlineSearch />}
                                value={query}
                                onValueChange={(e) => setQuery(e)}
                                type="text"
                                />
                        </div>
                        <Button 
                            className="flex-shrink-0 px-4 py-2 text-base font-semibold text-white rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-blue-200"
                            startContent={<BiFilterAlt />}
                            color="primary">
                            Filter
                        </Button>
                    </form>
                </div>
            </div>
        </>
    )

}

/*
                    <form onSubmit={handleSubmit} className="flex flex-col justify-center w-3/4 max-w-sm space-y-3 md:flex-row md:w-full md:space-x-3 md:space-y-0">
                        <div className=" relative ">
                            <Input
                                id="searchWorkersInput"
                                className="w-full sm:max-w-[66%]"
                                placeholder="Search by name..."
                                startContent={<HiOutlineSearch />}
                                value={query}
                                onValueChange={(e) => setQuery(e)}
                                type="submit"
                            />
                        </div>
                    </form>
                    <Button
                        startContent={<BiFilterAlt />}
                        color="primary"
                    >
                        Filters
                    </Button>
*/