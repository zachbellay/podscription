import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from './pages/Landing';
import SearchResults from './pages/SearchResults';
import SinglePodcast from './pages/SinglePodcast';
import NotFound from './pages/NotFound';


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/search" element={<SearchResults />} />
        <Route path="/podcast/:slug" element={<SinglePodcast />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}


export default App
