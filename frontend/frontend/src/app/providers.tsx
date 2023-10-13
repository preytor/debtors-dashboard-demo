'use client'

import { NextUIProvider } from '@nextui-org/react'
import { ThemeProvider } from './theme-provider'

export function Providers({children}: { children: React.ReactNode }) {
  return (
    <NextUIProvider>
      <ThemeProvider
        attribute="class"
        defaultTheme="system"
        enableSystem
        disableTransitionOnChange
      >
        {children}
      </ThemeProvider>
    </NextUIProvider>
  )
}