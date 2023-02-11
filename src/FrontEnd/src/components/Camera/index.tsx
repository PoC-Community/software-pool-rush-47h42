import React, { useRef } from 'react';
import Webcam from 'react-webcam';

function MyComponent() {
    const webcamRef = React.useRef<Webcam>(null);

    const capture = React.useCallback(
      () => {
        if (!webcamRef.current) return;

        const imageSrc = webcamRef.current.getScreenshot();
        // You can use the captured image here to display or send it to a server
      },
      [webcamRef]
    );

    return (
        <div>
            <Webcam ref={webcamRef} />
            <button onClick={capture}>Capture image</button>
        </div>
    );
}

export default MyComponent;
