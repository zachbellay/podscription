import React from 'react'
import { HiPlay, HiDocumentText } from 'react-icons/hi';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import LinesEllipsis from 'react-lines-ellipsis'
import responsiveHOC from 'react-lines-ellipsis/lib/responsiveHOC'

const ResponsiveEllipsis = responsiveHOC()(LinesEllipsis)

const PodcastEpisodeItem = (props) => {
    return (
        <div className="flex flex-col w-full h-full mb-4" key={props.key}>
            <h4 className="font-medium dark:text-white">{props.episode.title}</h4>

            <div className="flex flex-wrap">
                <LinesEllipsis className="text-sm dark:text-white"
                    text={props.episode.description}
                    maxLine='3'
                    ellipsis='...'
                    trimRight
                    basedOn='words'
                />

                <div className="flex flex-row mt-2">
                    <Button size="xs" outline={true} color='gray'
                        pill={true} href={props.episode.url} className="mr-2">
                        <HiPlay className="mr-2 h-5 w-5" />
                        Play
                    </Button>
                    <Button size="xs" outline={true} color='gray'
                        pill={true} href={props.episode.url} className="mr-2">
                        <HiDocumentText className="mr-2 h-5 w-5" />
                        Transcript
                    </Button>

                </div>
            </div>
        </div>
    );
};

export default PodcastEpisodeItem;