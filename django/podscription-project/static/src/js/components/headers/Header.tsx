import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar } from 'flowbite-react/lib/cjs/components/Navbar';

const Header = () => {
    return (
        <Navbar
            fluid={true}
            rounded={false}
        >
            <Navbar.Brand href="https://podscription.app/">
                <img
                    src="https://flowbite.com/docs/images/logo.svg"
                    className="mr-3 h-6 sm:h-9 "
                    alt="Podscription Logo"
                />
                <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
                    Podscription
                </span>
            </Navbar.Brand>
            <Navbar.Toggle />
            <Navbar.Collapse>
                <Navbar.Link
                    href="/"
                    active={true}
                >
                    Home
                </Navbar.Link>
                <Navbar.Link href="/podcasts/all">
                    Podcasts
                </Navbar.Link>
                <Navbar.Link href="/about">
                    About
                </Navbar.Link>
            </Navbar.Collapse>
        </Navbar>
    );
};

export default Header;
