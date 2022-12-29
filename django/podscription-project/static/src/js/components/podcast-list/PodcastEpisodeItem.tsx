import React from 'react'
import { HiPlay, HiDocumentText } from 'react-icons/hi';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import LinesEllipsis from 'react-lines-ellipsis'
import responsiveHOC from 'react-lines-ellipsis/lib/responsiveHOC'
import { PodcastEpisodeLightOut, PodcastOut } from '../../adapters/models';
import { Link } from 'react-router-dom';
import { formatDate, formatSeconds } from '../../utils';

const ResponsiveEllipsis = responsiveHOC()(LinesEllipsis)



// create interface for props
interface PodcastEpisodeItemProps {
    episode: PodcastEpisodeLightOut
    podcast: PodcastOut
    updateAudioCallback: (source: string) => void
    itemKey: string
}

const PodcastEpisodeItem = (props: PodcastEpisodeItemProps) => {

    return (
        <div className="flex flex-col w-full h-full mb-4" key={props.itemKey}>
            <Link to={`/podcast/${props.podcast.slug}/episode/${props.episode.slug}`}>
                <h4 className="font-medium dark:text-white">{props.episode.title}</h4>
                <p className="text-sm text-slate-500 dark:text-slate-200">{formatDate(props.episode.date)} | {formatSeconds(props.episode.duration)}</p>
            </Link>
            <div className="flex flex-wrap">
                <Link to={`/podcast/${props.podcast.slug}/episode/${props.episode.slug}`}>
                    <LinesEllipsis className="text-sm dark:text-white"
                        text={props.episode.description}
                        maxLine='3'
                        ellipsis='...'
                        trimRight
                        basedOn='words'
                    />
                </Link>

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
    );
};


export default PodcastEpisodeItem;