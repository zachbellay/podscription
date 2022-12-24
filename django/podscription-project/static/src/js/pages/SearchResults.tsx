import React from 'react'
import Header from '../components/headers/Header';
import Cookies from 'js-cookie';
import { SearchApi } from '../adapters/apis/SearchApi';
import { Configuration } from '../adapters/runtime';
import { useLocation } from 'react-router-dom';
import { PodcastSearchResultOut } from '../adapters/models/PodcastSearchResultOut';


// TODO : Make basePath come from env in vite config
const api = new SearchApi(new Configuration({
    basePath: 'http://localhost:8888',
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}));



const SearchResults = () => {

    const location = useLocation();
    const query = new URLSearchParams(location.search).get('q') || '';

    const [results, setResults] = React.useState<PodcastSearchResultOut[]>([]);

    React.useEffect(() => {

        api.search({ q: query }).then((response) => {
            setResults(response);
        });

    }, [query]);


    return (
        <div>
            <Header />
            Search Results for "{query}"
            {results.map((result) => {
                return (
                    <div>
                        <p>{result.headline}</p>
                        <br />
                    </div>
                );
            })
            }
        </div >
    );
};

export default SearchResults;