import WorkersTable from "./workers-table";
import WorkersTable2 from "./workers-table-2";
import WorkersTable3 from "./workers-table-3";


export default function Page() {


    /*
    Project structure:

    <search /> (CLIENT)
    <table /> (SERVER)
    <pagination /> (CLIENT)
    */
    return (
        <section className="ps-40">
            <WorkersTable3 />
        </section>
    )
}