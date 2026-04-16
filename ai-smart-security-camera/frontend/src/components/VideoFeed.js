import React, { useEffect, useRef } from "react";

export default function VideoFeed() {
  const videoRef = useRef();

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        videoRef.current.srcObject = stream;
      });
  }, []);

  return <video ref={videoRef} autoPlay width="500" />;
}
