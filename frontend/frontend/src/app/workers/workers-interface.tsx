

export interface WorkersInterface {
    id: number;
    name: string;
    contact_info: string;
    role: string;
}

export interface WorkersResultInterface {
    count: number;
    results: WorkersInterface[];
}