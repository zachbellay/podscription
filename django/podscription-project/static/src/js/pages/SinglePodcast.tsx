import React from 'react'
import Cookies from 'js-cookie';
import { useParams } from "react-router-dom";
import Header from '../components/headers/Header';
import { PodcastsApi } from '../adapters/apis/PodcastsApi';
import { PodcastEpisodesApi } from '../adapters/apis/PodcastEpisodesApi';
import { Configuration } from '../adapters/runtime';
import { PodcastOut } from '../adapters/models/PodcastOut';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import { HiGlobeAlt, HiSpeakerphone } from 'react-icons/hi';
import { APITypes } from "plyr-react";
import InfiniteScroll from 'react-infinite-scroll-component';
import { PodcastEpisodeLightOut } from '../adapters/models';
import PodcastEpisodeItem from '../components/podcast-list/PodcastEpisodeItem';
import Loader from '../components/loader/Loader';
import EndMessage from '../components/end-message/EndMessage';
import { getBaseUrl } from '../utils';

import styled, { css } from "styled-components";

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



interface SinglePodcastProps {
    updateAudioCallback: (source: string) => void;
}

const SinglePodcast: React.FC<SinglePodcastProps> = ({ updateAudioCallback }) => {

    // gets the slug from the url
    const { podcastSlug } = useParams<string>();

    // current podcast state
    const [podcast, setPodcast] = React.useState<PodcastOut>();


    // paginated podcasts stored here
    const [podcastEpisodes, setPodcastEpisodes] = React.useState<PodcastEpisodeLightOut[]>([]);

    // pagination state
    const [hasMore, setHasMore] = React.useState(true);
    const [page, setPage] = React.useState(1);


    const [error, setError] = React.useState<Record<string, string> | null>(null);
    const ref = React.useRef<APITypes>(null);

    // function to get more data using pagination for podcast episodes
    const fetchMoreData = () => {

        if (!hasMore || !podcast) {
            return;
        }

        podcastEpisodesApi.listPodcastEpisodes({ podcastId: podcast.id as number, page: page })
            .then((response) => {
                if (response.length < 20) {
                    setHasMore(false);
                }
                setPodcastEpisodes([...podcastEpisodes, ...response]);
                setPage(page + 1);
            });
    };

    // initialize the podcast that is being viewed
    React.useEffect(() => {
        podcastsApi.getPodcastBySlug({ podcastSlug: podcastSlug as string })
            .then((response) => {
                setPodcast(response);
            })
            .catch((err) => {
                let { statusCode, statusText } = err;
                setError({ code: statusCode, message: statusText })

            });
    }, [podcastSlug]);

    // get the first page of podcast episodes
    React.useEffect(() => {
        fetchMoreData();
    }, [podcast]);

    React.useEffect(() => {
        if (podcast) {
            document.title = `Podscription - ${podcast.name}`;
        }
    }, [podcast]);

    if (error) {
        return (
            <div className="h-screen">
                <Header />
                <h3>Error: {error.code}</h3>
                <h3>Error: {error.message}</h3>
            </div>
        );
    }

    return (
        <div className="h-screen">
            <Header />

            {podcast && (
                <div className="container px-5 py-12 min-w-full sm:px-24 min-h-full dark:bg-slate-800">
                    <div className="flex flex-wrap -m-4 justify-center">
                        <div className="p-4 md:w-1/3 ">
                            <img className="object-right" src={podcast.logoUrl} alt={podcast.name} width={300} />
                        </div>
                        <div className="p-4 md:w-2/3">

                            <h1 className="text-2xl font-semibold dark:text-white">{podcast.name}</h1>
                            <p className="font-light text-sm text-gray-800 dark:text-gray-400">{podcast.author}</p>

                            <div className="flex flex-row my-2">

                                <Button size="xs" outline={true} color='gray' pill={true} href={podcast.websiteUrl} className="mr-2">
                                    <HiGlobeAlt className="mr-2 h-5 w-5" />
                                    Website
                                </Button>


                            </div>

                            <p className="dark:text-gray-300" dangerouslySetInnerHTML={{ __html: podcast.description }} />

                        </div>
                    </div>

                    <h3 className="text-xl font-semibold dark:text-white mt-8 mb-2">Podcast Episodes</h3>
                    <div className="flex flex-wrap">

                        <InfiniteScroll
                            dataLength={podcastEpisodes.length} //This is important field to render the next data
                            next={fetchMoreData}
                            hasMore={hasMore}
                            loader={
                                <Loader />
                            }
                            endMessage={
                                <EndMessage />
                            }
                        >
                            {podcastEpisodes && podcastEpisodes.map((episode, index) => (
                                <div>
                                    <div className="h-px relative w-full bg-slate-500 my-1"></div>
                                    <PodcastEpisodeItem
                                        itemKey={String(episode.id)}
                                        episode={episode}
                                        podcast={podcast}
                                        updateAudioCallback={updateAudioCallback}
                                    />
                                </div>
                            ))}
                        </InfiniteScroll>
                    </div>

                </div>

            )}

        </div >
    );
};


export default SinglePodcast;

