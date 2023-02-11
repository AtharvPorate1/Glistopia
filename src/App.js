import logo from './logo.svg';

import './App.css';

function App() {
  return (
    <div className="App">
      <div className="main-page">
      <div className="header">
        <img src="logo-placeholder.png" alt="Logo Placeholder" />
        <input type="text" placeholder="Search" />
      </div>
      <div className="main-section">
        <div className="menu">
          <h2>Main Menu</h2>
          <ul>
            <li>Placeholder 1</li>
            <li>Placeholder 2</li>
            <li>Placeholder 3</li>
          </ul>
        </div>
        <div className="center-section">
          <img src="image-placeholder.png" alt="Image Placeholder" />
        </div>
        <div className="side-section">
          <h2>Best Nearby Hostels</h2>
          <ul>
            <li>Hostel Placeholder 1</li>
            <li>Hostel Placeholder 2</li>
            <li>Hostel Placeholder 3</li>
          </ul>
          <h2>Best Nearby Food Places</h2>
          <ul>
            <li>Food Placeholder 1</li>
            <li>Food Placeholder 2</li>
            <li>Food Placeholder 3</li>
          </ul>
        </div>
      </div>
    </div>
    </div>
  );
}

export default App;
