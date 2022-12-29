import React from 'react'
import Cookies from 'js-cookie';
import { Configuration } from '../adapters/runtime';
import { PodcastOut } from '../adapters/models/PodcastOut';
import { PodcastsApi } from '../adapters/apis/PodcastsApi';
import InfiniteScroll from 'react-infinite-scroll-component';
import Header from '../components/headers/Header';
import PodcastItem from '../components/podcast-list/PodcastItem';
import { Spinner } from 'flowbite-react/lib/cjs/components/Spinner';
import Loader from '../components/loader/Loader';
import EndMessage from '../components/end-message/EndMessage';

const podcastsApi = new PodcastsApi(new Configuration({
    basePath: 'http://localhost:8888',
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));


const PodcastAll = () => {

    // paginated podcasts stored here
    const [podcasts, setPodcasts] = React.useState<PodcastOut[]>([]);

    // pagination state
    const [hasMore, setHasMore] = React.useState(true);
    const [page, setPage] = React.useState(1);

    const [error, setError] = React.useState<Record<string, string> | null>(null);

    const fetchMoreData = () => {

        if (!hasMore) {
            return;
        }

        podcastsApi.listPodcasts({ page: page })
            .then((response) => {
                if (response.length < 20) {
                    setHasMore(false);
                }
                setPodcasts([...podcasts, ...response]);
                setPage(page + 1);
            })
            .catch((err) => {
                let { statusCode, statusText } = err;
                setError({ code: statusCode, message: statusText })

            });
    };

    React.useEffect(() => {
        fetchMoreData();
    }, []);

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
            {/* <div className="container px-5 py-12 min-w-full sm:px-24 min-h-full dark:bg-slate-800"> */}
            <div className="container px-5 min-w-full min-h-full dark:bg-slate-800">
                <h1 className="text-3xl font-bold text-center dark:text-white py-5">All Podcasts</h1>

                <InfiniteScroll
                    dataLength={podcasts.length} //This is important field to render the next data
                    next={fetchMoreData}
                    hasMore={hasMore}
                    loader={
                        <Loader />
                    }
                    endMessage={
                        <EndMessage />
                    }
                >
                    <div className="grid md:grid-cols-4 gap-1">
                        {podcasts && podcasts.map((podcast, index) => (
                            <div className="col-span-1">
                                <PodcastItem
                                    itemKey={String(podcast.id)}
                                    podcast={podcast}
                                />
                            </div>

                        ))
                        }
                    </div>
                </InfiniteScroll >

            </div >
        </div >
    );
};

export default PodcastAll;