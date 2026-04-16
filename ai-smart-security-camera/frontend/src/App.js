import React from "react";
import useWebSocket from "./hooks/useWebSocket";
import VideoFeed from "./components/VideoFeed";

function App() {
  const detections = useWebSocket("ws://localhost:8000/ws");

  return (
    <div>
      <h1>AI Smart Security Camera</h1>

      <VideoFeed />

      <h2>Detections</h2>
      {detections.map((d, i) => (
        <div key={i}>
          Class: {d.class} | Confidence: {d.confidence.toFixed(2)}
        </div>
      ))}
    </div>
  );
}

export default App;
