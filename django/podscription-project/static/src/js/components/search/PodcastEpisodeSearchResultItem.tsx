import React from 'react'
import { HiPlay, HiDocumentText } from 'react-icons/hi';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import LinesEllipsis from 'react-lines-ellipsis'
import responsiveHOC from 'react-lines-ellipsis/lib/responsiveHOC'
import { PodcastEpisodeSearchResultOut, PodcastOut } from '../../adapters/models';
import { Link } from 'react-router-dom';
import { formatDate, formatSeconds } from '../../utils';

const ResponsiveEllipsis = responsiveHOC()(LinesEllipsis)


// create interface for props
interface PodcastEpisodeItemProps {
    episode: PodcastEpisodeSearchResultOut
    podcast: PodcastOut
    updateAudioCallback: (source: string) => void
    itemKey: string
}

const PodcastEpisodeSearchResultItem = (props: PodcastEpisodeItemProps) => {

    return (
        <Link to={`/podcast/${props.podcast.slug}/episode/${props.episode.slug}`}>

            <div className="flex flex-row my-2 mx-4 sm:mx-0" key={props.itemKey}>

                <div className="hidden flex-none sm:block mr-5">
                    <img src={props.podcast.logoUrl} alt={props.podcast.name} width={100} />
                </div>

                <div >
                    <div className="flex flex-col sm:flex-row items-baseline">
                        <div className="font-medium dark:text-white">{props.podcast.name}</div>
                        <div className="hidden sm:block font-medium dark:text-white mx-1"> | </div>
                        <div className="text-sm dark:text-white">{props.episode.title}</div>
                    </div>

                    <p className="text-xs text-slate-500 dark:text-slate-200">
                        {formatDate(props.episode.date)} | {formatSeconds(props.episode.duration)}
                    </p>

                    <div className="flex flex-col">
                        <div className='text-sm dark:text-white' dangerouslySetInnerHTML={{ __html: props.episode.headline + '...' }} />

                    </div>
                    <div className="flex flex-row mt-2">

                        <Button onClick={() => props.updateAudioCallback(props.episode.resolvedAudioUrl)} size="xs" outline={true} color='gray'
                            pill={true} className="mr-2">
                            <HiPlay className="mr-2 h-5 w-5" />
                            Play
                        </Button>
                        <Link to={`/podcast/${props.podcast.slug}/episode/${props.episode.slug}`}>
                            <Button size="xs" outline={true} color='gray'
                                pill={true} className="mr-2">
                                <HiDocumentText className="mr-2 h-5 w-5" />
                                Transcript
                            </Button>
                        </Link>

                    </div>
                </div>

            </div>

        </Link >
    );
};


export default PodcastEpisodeSearchResultItem;