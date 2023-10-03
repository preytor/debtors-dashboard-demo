'use client';

import { useState } from "react";
import { Container, Navbar } from "reactstrap";
import Header from "./layouts/header/header";

import SideBar from "./layouts/sidebar/SideBar";

export default function Layout({ children }: any) {
    return (
        <main>
            <div className="pageWrapper d-md-block d-lg-flex">
                {/*** Sidebar ***/}
                <aside className={`sidebarArea shadow bg-white ${
                    !open ? "" : "showSidebar"
                }`}>
                    <SideBar/>
                </aside>
                {/*** Content Area ***/}

                <div className="contentArea">
                    {/*** Header ***/}
                    {/**<Header showMobmenu={() => showMobilemenu()} />*/}

                    {/*** Content ***/}
                    <Container className="py-4 wrapper" fluid>
                        <div>{children}</div>
                    </Container>
                </div>
            </div>
        </main>
    )
  }