'use client'

import { useState } from "react"
import DebtorsTable from "./debtors-table"
import { DebtorSearcher, DebtorTablePagination } from "./debtors-tools"
import { useRouter } from "next/navigation"


export default function Page() {
    
    const router = useRouter()

    const [page, setPage] = useState(0)
    const [perPage, setPerPage] = useState(0)
    const [args, setArgs] = useState("")

    return (
        <div className="ps-40">
            <DebtorSearcher />
            <DebtorsTable page={page} perPage={perPage} args={args} />
            <DebtorTablePagination />
            <p>
                <button onClick={() => {
                        setPage(page - 1); 
                        console.log("Previous");
                        router.refresh()
                    }
                }>Previous</button>
                <button onClick={() => {
                        setPage(page + 1); 
                        console.log("Next");
                        router.refresh()
                    }
                }>Next</button>
            </p>
        </div>
    )
}