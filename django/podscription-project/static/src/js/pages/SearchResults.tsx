import React from 'react'
import Header from '../components/headers/Header';
import Cookies from 'js-cookie';
import { SearchApi } from '../adapters/apis/SearchApi';
import { Configuration } from '../adapters/runtime';
import { useLocation } from 'react-router-dom';
import Search from '../components/search/Search';
import PodcastOut from '../adapters/models/PodcastOut';
import { PodcastEpisodeSearchResultOut } from '../adapters/models';
import { getBaseUrl } from '../utils';
// import PodcastSearchResults from '../components/search/PodcastSearchResults';

import PodcastItem from '../components/podcast-list/PodcastItem';
// import PodcastEpisodeItem from '../components/podcast-list/PodcastEpisodeItem';

import PodcastEpisodeSearchResultItem from '../components/search/PodcastEpisodeSearchResultItem';

console.log(import.meta.env.MODE)
console.log(import.meta.env.VITE_API_BASE_URI)
console.log(getBaseUrl())

// TODO : Make basePath come from env in vite config
const api = new SearchApi(new Configuration({
    // basePath: basePath,
    basePath: getBaseUrl(),
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));

// console.log('basePath', basePath);
console.log('hello world')

interface SearchResultsProps {
    updateAudioCallback: (source: string) => void
}

const SearchResults = ({ updateAudioCallback }: SearchResultsProps) => {

    const location = useLocation();
    const query = new URLSearchParams(location.search).get('q') || '';

    const [podcasts, setPodcasts] = React.useState<PodcastOut[]>([]);
    const [episodes, setEpisodes] = React.useState<PodcastEpisodeSearchResultOut[]>([]);

    React.useEffect(() => {
        api.searchEpisodes({ q: query }).then((response) => {
            setEpisodes(response);
        });
        api.searchPodcasts({ q: query }).then((response) => {
            setPodcasts(response);
        });
    }, [query]);


    return (

        <div className="h-screen">
            <Header />
            <div className="container min-w-full sm:px-24 min-h-full dark:bg-slate-800">

                <div className="mx-4 sm:mx-0">
                    <Search query={query} />
                </div>
                <div className="my-10"></div>


                {podcasts && podcasts.length > 0 &&
                    <div className="mb-14">
                        <h1 className="text-2xl font-semibold text-left dark:text-white mb-2">Top Podcast Results</h1>

                        <div className="flex flex-col justify-center items-center md:flex-row md:gap-4">
                            {podcasts.map((podcast) => {
                                return (
                                    <PodcastItem podcast={podcast} itemKey={podcast.slug} />
                                )
                            })}
                        </div>
                    </div>
                }

                {episodes && episodes.length > 0 &&
                    <div>
                        <h1 className="text-2xl font-semibold text-left dark:text-white mb-2 mx-4 sm:mx-0">Top Episode Results</h1>
                        <div>
                            {episodes.map((episode) => {
                                return (
                                    <PodcastEpisodeSearchResultItem
                                        episode={episode}
                                        podcast={episode.podcast}
                                        itemKey={episode.slug}
                                        updateAudioCallback={updateAudioCallback}
                                    />
                                )
                            })
                            }
                        </div>
                    </div>
                }


            </div >
        </div >
    );
};

export default SearchResults;