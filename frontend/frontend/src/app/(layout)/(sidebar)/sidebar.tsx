import Link from "next/link";
import { IoPersonSharp } from "react-icons/io5";
import { BsPersonLinesFill } from "react-icons/bs";
import { SiFiles } from "react-icons/si";

export default function Sidebar() {
    return (
        <>
        <aside id="default-sidebar" className="fixed left-0 z-40 w-45 h-screen" aria-label="Sidebar">
            <div className="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
                <ul className="space-y-2 font-medium">
                    <li>
                        <Link href="/workers" className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                        <IoPersonSharp className="w-5 h-5 text-gray-500" />
                        <span className="flex-1 ml-3 whitespace-nowrap">Workers</span>
                        </Link>
                    </li>
                    <li>
                        <Link href="/debtors" className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                        <BsPersonLinesFill className="w-5 h-5 text-gray-500" />
                        <span className="flex-1 ml-3 whitespace-nowrap">Debtors</span>
                        </Link>
                    </li>
                    <li>
                        <Link href="/cases" className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                        <SiFiles className="w-5 h-5 text-gray-500" />
                        <span className="flex-1 ml-3 whitespace-nowrap">Cases</span>
                        </Link>
                    </li>
                </ul>
            </div>
        </aside>
        </>
    )
}