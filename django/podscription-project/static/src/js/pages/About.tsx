import React from 'react'
import Header from '../components/headers/Header';


const About = () => {
    return (
        <div className="h-screen">
            <Header />
            <div className="container px-5 py-12 min-w-full sm:px-24 min-h-full dark:bg-slate-800">
                <h1 className="text-2xl font-semibold text-left dark:text-white mb-2 mx-4 sm:mx-0">
                    About
                </h1>
                <p>It was all a dream, I used to read Wired magazine.</p>
            </div>
        </div>
    );
};

export default About;