import { APITypes, PlyrInstance, PlyrProps, usePlyr } from "plyr-react";
import "plyr-react/plyr.css"
import React from 'react'

// create a new prop AudioPlayerProps that includes the location to seek to
type AudioPlayerLocationProps = {
    location?: number | null;
}

type AudioPlayerProps = AudioPlayerLocationProps & PlyrProps;



const AudioPlayer = React.forwardRef<APITypes, AudioPlayerProps>(
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

            if (props.location) {
                api.plyr.currentTime = props.location;
            }

            api.plyr.on("canplay", () => {
                api.plyr.play();
            });
            api.plyr.on("loadeddata", () => {
                if (props.location) {
                    api.plyr.currentTime = props.location;
                }

            });
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