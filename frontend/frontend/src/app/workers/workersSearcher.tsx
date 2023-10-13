


export const getWorkers = async (page: number=1, perPage: number=20, args: string='') => {
    const backend = process.env.BACKEND_URL;
    // We add 1 since the backend starts counting from 1 
    page += 1;
    console.log(`${backend}/api/workers?page=${page}&page_size=${perPage}${args}`)
    const response = await fetch(
        `${backend}/api/workers?page=${page}&page_size=${perPage}${args}`,
        //{ next: { revalidate: 10 } }
    );
    const workers = await response.json();

    const data: any = {
        count: workers?.count as number,
        results: workers?.results as any[],
    }  
    return data
}