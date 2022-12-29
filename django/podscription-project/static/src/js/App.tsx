import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from './pages/Landing';
import SearchResults from './pages/SearchResults';
import SinglePodcast from './pages/SinglePodcast';
import PodcastAll from './pages/PodcastAll';
import NotFound from './pages/NotFound';
import About from './pages/About';
import SingleEpisode from './pages/SingleEpisode';
import { Button } from 'flowbite-react/lib/cjs/components/Button';
import AudioPlayer from './components/audio-player/AudioPlayer';
import { APITypes, PlyrSource, PlyrInstance } from "plyr-react";


function App() {
  const ref = React.useRef<APITypes>(null);
  const [audioSource, setAudioSource] = React.useState<PlyrSource | null>(null);

  const [location, setLocation] = React.useState<number | null>(null);

  // install event listener to pause if space bar is pressed
  React.useEffect(() => {
    const handleKeyPresses = (e: KeyboardEvent) => {


      const { current } = ref as React.MutableRefObject<APITypes>;
      const api = current as { plyr: PlyrInstance };
      if (!api) return;

      if (e.code === "Space") {
        e.preventDefault();
        api.plyr.togglePlay();
      } else if (e.code === "ArrowRight") {
        e.preventDefault();
        api.plyr.forward();
      } else if (e.code === "ArrowLeft") {
        e.preventDefault();
        api.plyr.rewind();
      } else if (e.code === "ArrowUp") {
        e.preventDefault();
        api.plyr.increaseVolume(0.1);
      } else if (e.code === "ArrowDown") {
        e.preventDefault();
        api.plyr.decreaseVolume(0.1);
      } else if (e.code === "KeyM") {
        e.preventDefault();
        api.plyr.muted = !api.plyr.muted;
      } else if (e.code == "Digit1") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.1;
      } else if (e.code == "Digit2") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.2;
      } else if (e.code == "Digit3") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.3;
      } else if (e.code == "Digit4") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.4;
      } else if (e.code == "Digit5") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.5;
      } else if (e.code == "Digit6") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.6;
      } else if (e.code == "Digit7") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.7;
      } else if (e.code == "Digit8") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.8;
      } else if (e.code == "Digit9") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0.9;
      } else if (e.code == "Digit0") {
        e.preventDefault();
        api.plyr.currentTime = api.plyr.duration * 0;
      }

    }

    window.addEventListener("keydown", handleKeyPresses);

    return () => {
      window.removeEventListener("keydown", handleKeyPresses);
    }
  }, [window])


  const updateAudioSourceCallback = (source: string, location?: number | null) => {
    const { current } = ref as React.MutableRefObject<APITypes>;
    const api = current as { plyr: PlyrInstance };

    // dirty hack that adds a random number to the location to ensure that the audio player updates
    const randomNoise = Math.random() * 0.04 + 0.01;

    // ensure that location is not null or undefined, but location could be 0
    if (location !== null && location !== undefined) {
      setLocation(location + randomNoise);
    }

    // if the audio source is the same, just play it
    if (audioSource && source === audioSource.sources[0].src) {
      api.plyr.play()
      return;
    }

    setAudioSource({
      type: "audio" as const,
      sources: [
        {
          type: "audio/wav",
          src: source,
        },
      ],
    })



  }





  return (
    <BrowserRouter>

      <div className="fixed inset-x-0 bottom-0 z-50" >
        {audioSource && (
          <AudioPlayer
            ref={ref}
            source={audioSource}
            location={location}
          />
        )}
      </div>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/about" element={<About />} />
        <Route path="/search" element={<SearchResults updateAudioCallback={updateAudioSourceCallback} />} />
        <Route path="/podcast/all" element={<PodcastAll />} />
        <Route path="/podcast/:podcastSlug" element={<SinglePodcast updateAudioCallback={updateAudioSourceCallback} />} />
        <Route path="/podcast/:podcastSlug/episode/:episodeSlug" element={<SingleEpisode updateAudioCallback={updateAudioSourceCallback} />} />
        <Route path="*" element={<NotFound />} />
      </Routes>

    </BrowserRouter>
  )
}



export default App
