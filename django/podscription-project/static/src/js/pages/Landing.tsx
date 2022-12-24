import React from 'react'
import Header from '../components/headers/Header';
import Hero from '../components/heros/Hero';
import Search from '../components/search/Search';

const Landing = () => {
    return (
        <div className="h-screen overflow-hidden">
            <Header />
            <Hero>
                <Search placeholder="Search podcasts, episodes..." />
            </Hero>
        </div>
    );
};

export default Landing;