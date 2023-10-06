/** @type {import('next').NextConfig} */
const nextConfig = {
    experimental: {
        serverComponentsExternalPackages: ['reactstrap'],
        serverActions: true,
    },
    images: {
        domains: ['xsgames.co'],
    },
}

module.exports = nextConfig
