import { 
    Navbar, 
    NavbarBrand, 
    NavbarContent,
} from "@nextui-org/navbar";
import AvatarMenu from "./avatarMenu";
import Link from "next/link";
import { BiSolidPieChartAlt2 } from "react-icons/bi";

export default function Header() {
  return (
    <Navbar maxWidth="2xl" className="bg-gray-50 dark:bg-gray-800">
      <NavbarBrand>
        <Link href="/" className="ml-3 flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
          <BiSolidPieChartAlt2 className="w-5 h-5 text-gray-500" />
          Debtors Dashboard
        </Link>
      </NavbarBrand>

      <NavbarContent as="div" justify="end">
        <AvatarMenu />
      </NavbarContent>
    </Navbar>
  )
}