import { Button, Nav, NavItem, NavLink } from 'reactstrap';
import styles from './sidebar.module.css';

import classNames from "classnames";
import Logo from '../shared/logo';
import Link from 'next/link';
import Image from 'next/image';

import { 
  GrUserManager,
  GrUser,
  GrDocumentUser
} from 'react-icons/gr';

export default function SideBar() {
  return (
    <aside className={styles.sidebar + "flex flex-col justify-betweeen h-screen p-4"}>
      <div className="flex flex-col items-center">
        <Logo />
        <Nav 
          className='mb-4' 
          vertical
          pills
        >
          <Link href="/workers">
          <NavItem className="mb-2 hover:bg-gray-200 rounded-full py-2 px-4 flex items-center space-x-2 text-xl" label='Workers'>
          <GrUserManager className="text-xl" />
            Workers
          </NavItem> 
          </Link>
          <Link href="/debtors">
          <NavItem className="mb-2 hover:bg-gray-200 rounded-full py-2 px-4 flex items-center space-x-2 text-xl" label='Debtors'>
          <GrUser className="text-xl" />
            Debtors
          </NavItem> 
          </Link>
          <Link href="/cases">
          <NavItem className="mb-2 hover:bg-gray-200 rounded-full py-2 px-4 flex items-center space-x-2 text-xl" label='Cases'>
          <GrDocumentUser className="text-xl" />
            Cases
          </NavItem> 
          </Link>
        </Nav>
      </div>
      <button className={styles.sideButton + " bg-white rounded-full border border-gray-200 text-gray-800 px-4 py-2 flex items-center space-x-2 hover:bg-gray-200"}>
        <Image
          width={36}
          height={36}
          className="rounded-full"
          src="https://xsgames.co/randomusers/avatar.php?g=male"
          alt="User profile"
        />
        <span>Profile</span>
      </button>
    </aside>
  );
};