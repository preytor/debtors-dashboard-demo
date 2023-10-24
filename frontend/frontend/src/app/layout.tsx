import './globals.css'
import type { Metadata } from 'next'
import { Providers } from './providers'
import Header from './(layout)/(header)/header'
import Sidebar from './(layout)/(sidebar)/sidebar'

export const metadata: Metadata = {
  title: 'Debtors Dashboard',
  description: 'Debtors Dashboard demo to show tables with high volume of data',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          <Header />
          <Sidebar />
          <main className=''>{children}</main>
        </Providers>
      </body>
    </html>
  )
}
