import { DebtorsInterface, DebtorsResultInterface } from "./debtors-interface";
import { HOST_BACKEND } from "../../utils/public-env";

export const getDebtors = async (page: number=0, perPage: number=20, args: string=''): Promise<DebtorsResultInterface> => {
    // We add 1 since the backend starts counting from 1 
    page += 1;
    const response = await fetch(
        `${HOST_BACKEND}/api/debtors?page=${page}&page_size=${perPage}${args}`,
        //{ next: { revalidate: 10 } }
    );
    const debtors = await response.json();

    const data: any = {
        count: debtors?.count as number,
        results: debtors?.results as DebtorsInterface[],
    }  
    return data
}