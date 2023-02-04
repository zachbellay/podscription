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

// TODO : Make basePath come from env in vite config
const api = new SearchApi(new Configuration({
    basePath: getBaseUrl(),
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));

interface SearchResultsProps {
    updateAudioCallback: (source: string) => void
    setSearchSelectedCallback: (searchSelected: boolean) => void
}

const SearchResults = ({ updateAudioCallback, setSearchSelectedCallback }: SearchResultsProps) => {

    const location = useLocation();
    const query = new URLSearchParams(location.search).get('q') || '';

    const [podcasts, setPodcasts] = React.useState<PodcastOut[]>([]);
    const [episodes, setEpisodes] = React.useState<PodcastEpisodeSearchResultOut[]>([]);

    // React.useEffect(() => {
    //     api.searchEpisodes({ q: query }).then((response) => {
    //         setEpisodes(response);
    //     });
    //     api.searchPodcasts({ q: query }).then((response) => {
    //         setPodcasts(response);
    //     });
    // }, [query]);

    // rewrite the above to add a loading state
    const [loading, setLoading] = React.useState<boolean>(true);
    React.useEffect(() => {
        setLoading(true);
        api.searchEpisodes({ q: query }).then((response) => {
            setEpisodes(response);
            setLoading(false);
        });
        api.searchPodcasts({ q: query }).then((response) => {
            setPodcasts(response);
            setLoading(false);
        });
    }, [query]);







    return (

        <div className="h-screen">
            <Header />
            <div className="container min-w-full pb-12 sm:px-24 min-h-full dark:bg-slate-800">

                <div className="mx-4 sm:mx-0">
                    <Search
                        query={query}
                        setSearchSelectedCallback={setSearchSelectedCallback}
                    />
                </div>
                <div className="my-10"></div>

                {loading &&
                    <div className="flex flex-col justify-center items-center">
                        <h1 className="text-2xl font-semibold text-left dark:text-white mb-2 mx-4 sm:mx-0">
                            Loading...
                        </h1>
                    </div>
                }

                {!loading && podcasts && podcasts.length > 0 &&
                    <div className="mb-14">
                        <h1 className="text-2xl font-semibold text-left dark:text-white mb-2 mx-4 sm:mx-0">Top Podcast Results</h1>

                        <div className="flex flex-col justify-center items-center md:flex-row md:gap-4">
                            {podcasts.map((podcast) => {
                                return (
                                    <PodcastItem podcast={podcast} itemKey={podcast.slug} />
                                )
                            })}
                        </div>
                    </div>
                }

                {!loading && episodes && episodes.length > 0 &&
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

                {!loading && podcasts.length === 0 && episodes.length === 0 &&
                    <div className="flex flex-col justify-center items-center">
                        <h1 className="text-2xl font-semibold text-left dark:text-white mb-2 mx-4 sm:mx-0">
                            No Results Found
                        </h1>
                    </div>
                }

            </div >
        </div >
    );
};

export default SearchResults;