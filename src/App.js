import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./App.css";
import Categories from "./components/Categories";
import Sale from "./components/Sale";
import SignIn from "./components/SignIn";
import SignUp from "./components/SignUp";
import ShoeDetail from "./components/ShoeDetail";
import Cart from "./components/Cart";
import Payment from "./components/Payment";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="navbar">
          <div className="logo">R&R</div>
          <nav className="menu">
            <Link to="/" className="menu-item">
              Home
            </Link>
            <Link to="/categories" className="menu-item">
              Categories
            </Link>
            <Link to="/sale" className="menu-item">
              Sale
            </Link>
            <Link to="/cart" className="menu-item">
              <i className="fas fa-shopping-cart">Cart</i>
            </Link>
          </nav>
          <div className="auth-buttons">
            <Link to="/signin" className="signin-button">
              <button className="signin">Sign in</button>
            </Link>
            <Link to="/signup" className="signup-button">
              <button className="signup">Sign Up</button>
            </Link>
          </div>
        </header>

        {/* Main content for each route */}
        <Routes>
          {/* Home route */}
          <Route
            path="/"
            element={
              <section className="hero">
                <div className="text-container">
                  <h1 className="title">Roots & Routes</h1>
                  <p className="description">
                    "Roots & Routes is an e-commerce platform that connects you
                    with a wide variety of quality fashion products, from shoes,
                    clothing, to the latest accessories. Discover style
                    inspiration from our exclusive collections and enjoy a
                    seamless, fast, and secure shopping experience. We believe
                    that every step you take is part of your journey, and we're
                    here to support it."
                  </p>
                </div>
                <div className="image-container">
                  <img src="/images/sneakers_nike.png" alt="Shoes" />
                </div>
              </section>
            }
          />

          {/* Categories route */}
          <Route path="/categories" element={<Categories />} />

          {/* Sale route */}
          <Route path="/sale" element={<Sale />} />

          {/* Sign In route */}
          <Route path="/signin" element={<SignIn />} />

          {/* Sign Up route */}
          <Route path="/signup" element={<SignUp />} />

          {/* ShoeDetail route - dynamic */}
          <Route path="/shoes/:id" element={<ShoeDetail />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/payment/:id" element={<Payment />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
