import React from 'react'
import Header from '../components/headers/Header';
import Hero from '../components/heros/Hero';
import Search from '../components/search/Search';

// setSearchSelectedCallback

interface LandingProps {
    setSearchSelectedCallback: (searchSelected: boolean) => void
}

const Landing = ({ setSearchSelectedCallback }: LandingProps) => {
    return (
        <div className="landing h-screen overflow-hidden">
            <Header />
            <Hero>
                <Search placeholder="Search podcasts, episodes..." setSearchSelectedCallback={setSearchSelectedCallback} />
            </Hero>
        </div>
    );
};

export default Landing;