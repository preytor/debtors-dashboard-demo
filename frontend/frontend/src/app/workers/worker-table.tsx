import { WorkersInterface } from "./workers-interface";




export default function WorkerTable( { workers }: { workers: WorkersInterface[] }) {
    return (
        <ul>
            {workers.map((worker: any) => (
                <li>worker.name</li>
            ))}
        </ul>
    )
}