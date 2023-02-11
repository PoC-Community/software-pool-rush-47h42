import React, { useRef, useEffect } from 'react';
import fabric from 'fabric';


function BlockSet() {
	const canvasRef = useRef<HTMLCanvasElement>(null);

	useEffect(() => {
	  if (canvasRef.current) {
		const canvas = new fabric.fabric.Canvas(canvasRef.current);
		const rect = new fabric.fabric.Rect({
		  left: 100,
		  top: 100,
		  fill: 'red',
		  width: 20,
		  height: 20
		});
		rect.selectable = true;
		canvas.add(rect);
	  }
	}, []);

	return <canvas ref={canvasRef} />;
  }

export default BlockSet;

console.log(process.env.REACT_APP_SECRET_CODE);