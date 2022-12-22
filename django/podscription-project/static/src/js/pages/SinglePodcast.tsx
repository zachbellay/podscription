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
import AudioPlayer from '../components/audio-player/AudioPlayer';
//////////
import { APITypes } from "plyr-react";
import InfiniteScroll from 'react-infinite-scroll-component';
import { PodcastEpisodeLightOut } from '../adapters/models';
import PodcastEpisodeItem from '../components/postcast-list/PodcastEpisodeItem';


// TODO : Make basePath come from env in vite config
const podcastsApi = new PodcastsApi(new Configuration({
    basePath: 'http://localhost:8888',
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));

const podcastEpisodesApi = new PodcastEpisodesApi(new Configuration({
    basePath: 'http://localhost:8888',
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));



const videoSource = {
    type: "audio" as const,
    sources: [
        {
            type: "audio/wav",
            src: "https://dts.podtrac.com/redirect.mp3/chrt.fm/track/8DB4DB/pdst.fm/e/nyt.simplecastaudio.com/03d8b493-87fc-4bd1-931f-8a8e9b945d8a/episodes/cf1f5291-8408-4b4c-bc45-c51f00569d13/audio/128/default.mp3?aid=rss_feed&awCollectionId=03d8b493-87fc-4bd1-931f-8a8e9b945d8a&awEpisodeId=cf1f5291-8408-4b4c-bc45-c51f00569d13&feed=54nAGcIl",
        },
    ],
};


const SinglePodcast = () => {

    const { slug } = useParams<string>();

    const [podcast, setPodcast] = React.useState<PodcastOut | null>(null);
    const [podcastEpisodes, setPodcastEpisodes] = React.useState<PodcastEpisodeLightOut[]>([]);
    const [hasMore, setHasMore] = React.useState(true);
    const [page, setPage] = React.useState(1);


    const [error, setError] = React.useState<Record<string, string> | null>(null);


    const ref = React.useRef<APITypes>(null);

    const fetchMoreData = () => {

        if (!hasMore) {
            return;
        }

        podcastEpisodesApi.listPodcastEpisodes({ podcastId: podcast?.id as number, page: page })
            .then((response) => {
                if (response.length < 20) {
                    setHasMore(false);
                }
                // console.log(response)
                // podcastEpisodes.concat(response);
                setPodcastEpisodes([...podcastEpisodes, ...response]);
                setPage(page + 1);
            });
    };



    React.useEffect(() => {
        podcastsApi.getPodcastBySlug({ podcastSlug: slug as string })
            .then((response) => {
                setPodcast(response);
            })
            .catch((err) => {
                let { statusCode, statusText } = err;
                setError({ code: statusCode, message: statusText })

            });
    }, [slug]);

    React.useEffect(() => {
        fetchMoreData();
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
                                <Button size="xs" outline={true} color='gray' pill={true} href={podcast.url}>
                                    <HiSpeakerphone className="mr-2 h-5 w-5" />
                                    Google Podcasts
                                </Button>

                            </div>

                            <p className="dark:text-gray-300">{podcast.description}</p>



                        </div>
                    </div>


                    <div className="flex flex-wrap mt-8">

                        <h3 className="text-xl font-semibold dark:text-white mb-2">Podcast Episodes</h3>

                        <InfiniteScroll
                            dataLength={podcastEpisodes.length} //This is important field to render the next data
                            next={fetchMoreData}
                            hasMore={hasMore}
                            loader={<h4 className="dark:text-white">Loading...</h4>}
                            endMessage={
                                <p style={{ textAlign: 'center' }}>
                                    <b>Yay! You have seen it all</b>
                                </p>
                            }
                        >
                            {podcastEpisodes && podcastEpisodes.map((episode, index) => (
                                <div>
                                    <div className="h-px relative w-full bg-slate-500 my-1"></div>
                                    <PodcastEpisodeItem key={index} episode={episode} />
                                </div>
                            ))}
                        </InfiniteScroll>
                    </div>

                </div>

            )}




            {/* <div className="wrapper" >
                <Button onClick={() => console.log(podcastEpisodes)}>dsa</Button>
                <Button onClick={() => ref.current?.plyr.play()}>Play</Button>
                <Button onClick={() => ref.current?.plyr.pause()}>Pause</Button>
                {videoSource && (
                    <AudioPlayer
                        ref={ref}
                        source={videoSource}
                    />
                )}
            </div> */}
        </div >
    );
};


export default SinglePodcast;

