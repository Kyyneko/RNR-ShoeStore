import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Categories from './components/Categories';
import Sale from './components/Sale';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="navbar">
          <div className="logo">R&R</div>
          <nav className="menu">
            <Link to="/" className="menu-item">Home</Link>
            <Link to="/categories" className="menu-item">Categories</Link>
            <Link to="/sale" className="menu-item">Sale</Link>
            <Link to="/cart" className="menu-item">
              <i className="fas fa-shopping-cart"></i>
            </Link>
          </nav>
          <div className="auth-buttons">
            {/* Gunakan Link untuk mengarahkan ke /signin saat tombol Sign in ditekan */}
            <Link to="/signin" className="signin-button">
              <button className="signin">Sign in</button>
            </Link>
            {/* Gunakan Link untuk mengarahkan ke /signup saat tombol Sign Up ditekan */}
            <Link to="/signup" className="signup-button">
              <button className="signup">Sign Up</button>
            </Link>
          </div>
        </header>

        <Routes>
          <Route path="/" element={
            <section className="hero">
              <div className="text-container">
                <h1 className="title">Roots & Routes</h1>
                <p className="description">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                  dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                </p>
              </div>
              <div className="image-container">
                <img src="/images/sneakers_nike.png" alt="Shoes" />
              </div>
            </section>
          } />

          <Route path="/categories" element={<Categories />} />
          <Route path="/sale" element={<Sale />} />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
