

export interface DebtorsInterface {
    id: number;
    name: string;
    contact_info: string;
    legal_status: string;
}

export interface DebtorsResultInterface {
    count: number;
    results: DebtorsInterface[];
}