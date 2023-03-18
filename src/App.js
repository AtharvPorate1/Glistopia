import logo from './logo.svg';

import './App.css';
import Header from './components/Header'
import HouseListing from './pages/HouseListing'

// This is basic page


function App() {
  return (
    <div className="App">
      <Header/>
      <HouseListing/>
      
    </div>
  );
}

export default App;
