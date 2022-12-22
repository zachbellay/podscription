import React from 'react';

//  

const Hero = (props) => {
    return (
        <section className="flex h-[calc(100vh-56px)] bg-white dark:bg-gray-900">
            <div className="m-auto text-center max-w-screen-xl">


                <h1 className="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Search Podcast Transcripts Instantly</h1>

                <p className="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">Easily find and access transcripts for your favorite podcasts</p>

                {props.children}
            </div>

        </section>
    );
};

export default Hero;


// convert png to jpg linux command
