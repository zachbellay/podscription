import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar } from 'flowbite-react/lib/cjs/components/Navbar';
import DarkModeButton from '../buttons/DarkModeButton';

import PodscriptionLogo from '../../../assets/podscription.svg';

import styled, { css } from "styled-components";


// Horrific hack but it's what I have to do so I don't have to copy the entire
// flowbite-react Navbar component into this project.
const StyledLink = styled(Navbar.Link)`
    @media (min-width: 768px) {
        margin-top: 10px;
        margin-bottom: 10px;
    }
`;

const Header = () => {

    return (
        <Navbar
            fluid={true}
            rounded={false}
        >
            <Link to="/">
                <Navbar.Brand>
                    <img
                        src={PodscriptionLogo}
                        className="mr-3 h-6 sm:h-9 dark:invert"
                        alt="Podscription Logo"
                    />
                    <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
                        Podscription
                    </span>
                </Navbar.Brand>
            </Link>
            <Navbar.Toggle />

            <Navbar.Collapse >
                <Link to="/">
                    <StyledLink
                        href="/"
                        active={true}
                    >
                        Home
                    </StyledLink>
                </Link>

                <Link to="/podcast/all">
                    <StyledLink >
                        Podcasts
                    </StyledLink>
                </Link>

                <Link to="/about">
                    <StyledLink>
                        About
                    </StyledLink>
                </Link>


                <DarkModeButton />

            </Navbar.Collapse>




        </Navbar >

    );
};

export default Header;
