import React from 'react'
import Header from '../components/headers/Header';
import { Link } from 'react-router-dom';

const NotFound = () => {
    return (
        <div className="h-screen">
            <Header />
            <div className="flex h-[calc(100vh-56px)] bg-white dark:bg-gray-900">
                <div className="m-auto text-center max-w-screen-xl">
                    <Link to="/">
                        <h1 className="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">404: Page Not Found</h1>
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default NotFound;