import './globals.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import SideBar from './(dashboardLayout)/layouts/sidebar/SideBar'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Debtors Dashboard',
  description: 'Dashboards for Debtors',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className + " flex flex-row"}>
        <SideBar/>
        {children}
      </body>
    </html>
  )
}
