"use client"
import { 
    DropdownItem, 
    DropdownTrigger, 
    Dropdown, 
    DropdownMenu,
    DropdownSection,
} from "@nextui-org/dropdown";
import { User } from "@nextui-org/user";
import { Avatar } from "@nextui-org/avatar";
import { useTheme } from 'next-themes'

import { IoSettingsSharp } from "react-icons/io5";
import { BiSolidUser } from "react-icons/bi";
import { RiLogoutBoxRFill } from "react-icons/ri";
import { BsLightbulbFill } from "react-icons/bs";


export default function AvatarMenu() {
    const { theme, setTheme } = useTheme();

    return (
        <Dropdown placement="bottom-end">
            <DropdownTrigger>
            <Avatar
              isBordered
              as="button"
              className="transition-transform"
              color="secondary"
              name="John Smith"
              size="sm"
              src="https://i.pravatar.cc/150?img=57"
            />
            </DropdownTrigger>
            <DropdownMenu
                aria-label="Custom item styles"
                disabledKeys={["profile"]}
                className="p-3"
                itemClasses={{
                    base: [
                    "rounded-md",
                    "text-default-500",
                    "transition-opacity",
                    "data-[hover=true]:text-foreground",
                    "data-[hover=true]:bg-default-100",
                    "dark:data-[hover=true]:bg-default-50",
                    "data-[selectable=true]:focus:bg-default-50",
                    "data-[pressed=true]:opacity-70",
                    "data-[focus-visible=true]:ring-default-500",
                    ],
                }}
            >
            <DropdownSection aria-label="Profile & Actions" showDivider>
                <DropdownItem
                isReadOnly
                key="profile"
                className="h-14 gap-2 opacity-100"
                >
                    <User
                        name="John Smith"
                        description=""
                        classNames={{
                        name: "text-default-600",
                        description: "text-default-500",
                        }}
                        avatarProps={{
                        size: "sm",
                        src: "https://i.pravatar.cc/150?img=57",
                        }}
                    />
                </DropdownItem>
                <DropdownItem key="user" startContent={<BiSolidUser />}>Profile</DropdownItem>
                <DropdownItem key="settings" startContent={<IoSettingsSharp />}>Settings</DropdownItem>
            </DropdownSection>

            <DropdownItem startContent={<BsLightbulbFill />}
                isReadOnly
                key="theme"
                className="cursor-default"
                endContent={
                    <select
                    className="z-10 outline-none w-16 py-0.5 rounded-md text-tiny group-data-[hover=true]:border-default-500 border-small border-default-300 dark:border-default-200 bg-transparent text-default-500"
                    id="theme"
                    name="theme"
                    >
                    <option  onClick={() => setTheme('light')}>Light</option>
                    <option  onClick={() => setTheme('dark')}>Dark</option>
                    </select>
                }
            >
                    Theme
            </DropdownItem>

            <DropdownSection aria-label="Help & Feedback">
                <DropdownItem key="logout" startContent={<RiLogoutBoxRFill />}>Log Out</DropdownItem>
            </DropdownSection> 
            </DropdownMenu>
        </Dropdown>
    )
}