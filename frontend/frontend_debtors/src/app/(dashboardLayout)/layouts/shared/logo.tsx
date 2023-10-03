import LogoImg from 'public/images/logo.png'
import Image from 'next/image'
import Link from 'next/link'

export default function Logo() {
    return (
        <Link href="/">
            <Image 
                src={LogoImg} 
                alt="Logo" 
                className="logo"
                width={40}
                height={40} 
            />
        </Link>
    )
}