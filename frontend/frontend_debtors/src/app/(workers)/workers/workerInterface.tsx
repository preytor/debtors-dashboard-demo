export interface WorkerInterface {
    id: number;
    name: string;
    contact_info: string;
    role: string;
}

export interface WorkerDataInterface {
    count: number;
    results: WorkerInterface[];
}