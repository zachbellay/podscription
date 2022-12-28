import React from 'react';
import { PodcastEpisodeOut } from '../../adapters/models';


interface TranscriptProps {
    podcastEpisode: PodcastEpisodeOut;
    updateAudioCallback: (source: string, location: number | null) => void;
}

const formatSeconds = (duration: number) => {
    const hours = Math.floor(duration / 3600);
    const minutes = Math.floor(duration / 60);
    const seconds = duration % 60;

    // pad with leading zeros
    const hoursString = hours.toString().padStart(2, '0');
    const minutesString = minutes.toString().padStart(2, '0');
    const secondsString = seconds.toString().padStart(2, '0');

    if (hours > 0) {
        return `${hoursString}:${minutesString}:${secondsString}`;
    } else {
        return `${minutesString}:${secondsString}`;
    }
}

const Transcript: React.FC<TranscriptProps> = ({ podcastEpisode, updateAudioCallback }) => {

    const timeLocationClickHandler = (timeLocation: number) => {
        updateAudioCallback(podcastEpisode.resolvedAudioUrl, timeLocation);
        console.log(timeLocation);
    }


    if (!podcastEpisode.transcription) {
        return (
            <p className="dark:text-white">No transcript currently available. Please check again later.</p>
        )
    }

    return (
        <div className="w-100">
            {podcastEpisode.transcription.map((item, index) => (
                <div>

                    <button className="text-xs font-medium select-none -ml-4 hover:text-slate-400 dark:hover:text-slate-500 dark:text-white" onClick={() => { timeLocationClickHandler(Number(item.start)) }}>► {formatSeconds(Number(item.start))}</button>

                    <p className="pb-3 -mt-1 dark:text-white">{item.text}</p>
                </div>
            ))}
        </div>
    )
};

export default Transcript;