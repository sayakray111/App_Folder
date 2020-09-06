import React from 'react'
import Link from 'next/link'
import Button from '@material-ui/core/Button'

const ButtonLink = ({ className, href, hrefAs, children, prefetch }) => (
    <Link href={href} as={hrefAs} prefetch>
        <a className={className}>
            {children}
        </a>
    </Link>
)

// https://material-ui.com/demos/buttons/#third-party-routing-library
const RenderButton2 = () => <Button component={ButtonLink} href={'/api/login'}>Abaqus Design</Button>
export default RenderButton2