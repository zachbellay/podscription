import React from 'react'
import LinesEllipsis from 'react-lines-ellipsis'
import responsiveHOC from 'react-lines-ellipsis/lib/responsiveHOC'
import { PodcastOut } from '../../adapters/models';
import { Link } from 'react-router-dom';

const ResponsiveEllipsis = responsiveHOC()(LinesEllipsis)


interface PodcastItemProps {
    podcast: PodcastOut
    itemKey: string
}

const PodcastItem: React.FC<PodcastItemProps> = ({ podcast, itemKey }) => {

    return (

        <div className="col-span-1" key={itemKey}>
            <Link to={`/podcast/${podcast.slug}`}>
                <img src={podcast.logoUrl} alt={podcast.name} width={300} className="mx-auto" />
            </Link>
            <Link to={`/podcast/${podcast.slug}`}>
                <h4 className="font-medium text-center dark:text-white">{podcast.name}</h4>
            </Link>
        </div>

    );
};


export default PodcastItem;