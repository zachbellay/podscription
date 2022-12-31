import React from 'react'
import Header from '../components/headers/Header';
import { useParams } from "react-router-dom";
import { PodcastsApi } from '../adapters/apis/PodcastsApi';
import { PodcastEpisodesApi } from '../adapters/apis/PodcastEpisodesApi';
import { Configuration } from '../adapters/runtime';
import { PodcastOut } from '../adapters/models/PodcastOut';
import Cookies from 'js-cookie';
import { PodcastEpisodeOut } from '../adapters/models';
import { Link } from 'react-router-dom';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import { HiPlay } from 'react-icons/hi';
import { formatDate } from '../utils';
import Transcript from '../components/transcript/Transcript';
import { getBaseUrl } from '../utils';
import { convert } from 'html-to-text';

// TODO : Make basePath come from env in vite config
const podcastsApi = new PodcastsApi(new Configuration({
    basePath: getBaseUrl(),
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));

const podcastEpisodesApi = new PodcastEpisodesApi(new Configuration({
    basePath: getBaseUrl(),
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));


interface SingleEpisodeProps {
    updateAudioCallback: (source: string, location?: number | null) => void;
}

const SingleEpisode: React.FC<SingleEpisodeProps> = ({ updateAudioCallback }) => {
    const { podcastSlug, episodeSlug } = useParams<string>();

    // current podcast state
    const [podcast, setPodcast] = React.useState<PodcastOut>();

    // get current podcast episode
    const [podcastEpisode, setPodcastEpisode] = React.useState<PodcastEpisodeOut>();

    const [error, setError] = React.useState<Record<string, string> | null>(null);

    React.useEffect(() => {
        podcastsApi.getPodcastBySlug({ podcastSlug: podcastSlug as string })
            .then((response) => {
                setPodcast(response);
            })
            .catch((err) => {
                let { statusCode, statusText } = err;
                setError({ code: statusCode, message: statusText })

            });

        podcastEpisodesApi.getPodcastEpisode({ podcastSlug: podcastSlug as string, episodeSlug: episodeSlug as string })
            .then((response) => {
                setPodcastEpisode(response);
            })
            .catch((err) => {
                let { statusCode, statusText } = err;
                setError({ code: statusCode, message: statusText })

            });



    }, [podcastSlug]);

    React.useEffect(() => {
        if (podcast && podcastEpisode) {
            document.title = `Podscription - ${podcast.name} - ${podcastEpisode.title}`;
        }
    }, [podcast, podcastEpisode]);


    return (
        <div className="h-screen">
            <Header />
            {(podcast && podcastEpisode) && (
                <div className="container px-5 py-12 min-w-full sm:px-24 min-h-full dark:bg-slate-800">
                    <div className="flex flex-wrap -m-4 justify-center">
                        <div className="p-4 md:w-1/3 ">
                            <Link to={`/podcast/${podcast.slug}`}>
                                <img className="object-right" src={podcast.logoUrl} alt={podcast.name} width={300} />
                            </Link>
                        </div>
                        <div className="p-4 md:w-2/3">
                            <Link to={`/podcast/${podcast.slug}`}>
                                <h1 className="text-xl font-medium dark:text-slate-400">{podcast.name}</h1>
                            </Link>

                            <h1 className="text-3xl font-semibold dark:text-white">{podcastEpisode.title}</h1>

                            <p className="font-light text-sm text-gray-800 dark:text-gray-400">{formatDate(podcastEpisode.date)} | {Math.floor(podcastEpisode.duration / 60)}m {podcastEpisode.duration % 60}s</p>

                            <p className="dark:text-gray-300">{convert(podcastEpisode.description)}</p>

                            <Button onClick={() => updateAudioCallback(podcastEpisode.resolvedAudioUrl)} size="xs" outline={true} color='gray'
                                pill={true} className="mr-2 my-1">
                                <HiPlay className="mr-2 h-5 w-5" />
                                Play
                            </Button>

                        </div>
                    </div>

                    <h3 className="text-xl font-semibold dark:text-white mt-8 mb-2">Transcript</h3>
                    <div className="flex flex-wrap mt-8">

                        <Transcript podcastEpisode={podcastEpisode} updateAudioCallback={updateAudioCallback} />

                    </div>

                </div>

            )}
        </div>
    );
};

export default SingleEpisode;