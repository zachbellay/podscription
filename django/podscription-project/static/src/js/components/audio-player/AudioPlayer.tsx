import { APITypes, PlyrInstance, PlyrProps, usePlyr } from "plyr-react";
import "plyr-react/plyr.css"
import React from 'react'


const videoOptions = undefined;

const videoSource = {
    type: "audio" as const,
    sources: [
        {
            type: "audio/wav",
            src: "https://dts.podtrac.com/redirect.mp3/chrt.fm/track/8DB4DB/pdst.fm/e/nyt.simplecastaudio.com/03d8b493-87fc-4bd1-931f-8a8e9b945d8a/episodes/cf1f5291-8408-4b4c-bc45-c51f00569d13/audio/128/default.mp3?aid=rss_feed&awCollectionId=03d8b493-87fc-4bd1-931f-8a8e9b945d8a&awEpisodeId=cf1f5291-8408-4b4c-bc45-c51f00569d13&feed=54nAGcIl",
        },
    ],
};

const AudioPlayer = React.forwardRef<APITypes, PlyrProps>(
    (props, ref) => {
        const { source, options = null } = props;
        const raptorRef = usePlyr(ref, { options, source });

        // Do all api access here, it is guaranteed to be called with the latest plyr instance
        React.useEffect(() => {
            /**
             * Fool react for using forward ref as normal ref
             * NOTE: in a case you don't need the forward mechanism and handle everything via props
             * you can create the ref inside the component by yourself
             */
            const { current } = ref as React.MutableRefObject<APITypes>;
            if (current.plyr.source === null) return;

            const api = current as { plyr: PlyrInstance };
            api.plyr.on("ready", () => console.log("I'm ready"));
            api.plyr.on("canplay", () => {
                // NOTE: browser may pause you from doing so:  https://goo.gl/xX8pDD
                // api.plyr.play();
                console.log("duration of audio is", api.plyr.duration);
            });
            api.plyr.on("ended", () => console.log("I'm Ended"));
        });

        return (
            <video
                ref={raptorRef as React.MutableRefObject<HTMLVideoElement>}
                className="plyr-react plyr"
            />
        );
    }
);

export default AudioPlayer;