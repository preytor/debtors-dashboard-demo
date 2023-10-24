import { WorkersInterface, WorkersResultInterface } from "./workers-interface";
import { HOST_BACKEND } from "../../utils/public-env";

export const getWorkers = async (page: number=0, perPage: number=20, args: string=''): Promise<WorkersResultInterface> => {
    // We add 1 since the backend starts counting from 1 
    page += 1;
    const response = await fetch(
        `${HOST_BACKEND}/api/workers?page=${page}&page_size=${perPage}${args}`,
        //{ next: { revalidate: 10 } }
    );
    const workers = await response.json();

    const data: any = {
        count: workers?.count as number,
        results: workers?.results as WorkersInterface[],
    }  
    return data
}