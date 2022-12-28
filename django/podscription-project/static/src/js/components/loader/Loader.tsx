import React from 'react';
import { Spinner } from 'flowbite-react/lib/cjs/components/Spinner';

const Loader = () => {
    return (
        <div className="text-center ">
            <Spinner aria-label="Center-aligned spinner" size="xl" />
        </div>
    );
};

export default Loader;