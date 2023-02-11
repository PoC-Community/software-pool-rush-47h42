import BlockSet from './components/Block/block';
import React, { useState } from 'react';

/* function ClickableBlock() {
  const [isClicked, setIsClicked] = useState(false);
  const handleClick = () => {
    setIsClicked(!isClicked);
  };

  return (
    <div onClick={handleClick}>
    </div>
  );
} */

interface ButtonProps {
  backgroundColor: string;
  color: string;
  children: React.ReactNode;
}

function Button(props: ButtonProps) {
  return (
    <button style={{ backgroundColor: props.backgroundColor, color: props.color }}>
      {props.children}
    </button>
  );
}
function App(): JSX.Element {
  return (
    <div className="App">
      <Button backgroundColor="#3f51b5" color="#fff">Cliquez ici</Button>
      <BlockSet />
      <canvas id="c" width={500} height={500} />
    </div>
  );
}

export default App;
