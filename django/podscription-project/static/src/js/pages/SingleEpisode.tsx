import React from 'react'
import Header from '../components/headers/Header';
import { useParams } from "react-router-dom";


interface SingleEpisodeProps {
    updateAudioCallback: (source: string) => void;
}

const SingleEpisode: React.FC<SingleEpisodeProps> = ({ updateAudioCallback }) => {
    const { podcastSlug, episodeSlug } = useParams<string>();
    return (
        <div className="h-screen">
            <Header />
            <h3>Podcast: {podcastSlug}</h3>
            <h3>Episode: {episodeSlug}</h3>
        </div>
    );
};

export default SingleEpisode;