/** @type {import('next').NextConfig} */
const nextConfig = {
    experimental: {
        serverComponentsExternalPackages: ['reactstrap'],
    },
    images: {
        domains: ['xsgames.co'],
    },
}

module.exports = nextConfig
