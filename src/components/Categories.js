import React from 'react';
import './Categories.css';

function Categories() {
  return (
    <div className="categories-page">
      <h2 className="best-product-title">Best Product R&R</h2>
      <div className="search-container">
        <input type="text" placeholder="Cari di R&R" className="search-bar" />
      </div>
      
      
      <div className="product-grid">
        <div className="product-card">
          <img src="/images/sepatu2.png" alt="Product 1" className="product-image" />
          <div className="product-details">
            <span className="product-category">Men Original</span>
            <h3 className="product-name">NIKE Lorem Ipsum</h3>
            <p className="product-price">Rp. 1,699,000</p>
          </div>
          <button className="wishlist-btn"><i className="fas fa-heart"></i></button>
          <button className="cart-btn"><i className="fas fa-plus"></i></button>
        </div>

        <div className="product-card">
          <img src="/images/adidas.png" alt="Product 2" className="product-image" />
          <div className="product-details">
            <span className="product-category">Men Original</span>
            <h3 className="product-name">ADIDAS Lorem Ipsum</h3>
            <p className="product-price">Rp. 2,699,000</p>
          </div>
          <button className="wishlist-btn"><i className="fas fa-heart"></i></button>
          <button className="cart-btn"><i className="fas fa-plus"></i></button>
        </div>

        <div className="product-card">
          <img src="/images/nike-air.png" alt="Product 3" className="product-image" />
          <div className="product-details">
            <span className="product-category">Unisex Original</span>
            <h3 className="product-name">NIKE AIR Lorem Ipsum</h3>
            <p className="product-price">Rp. 1,899,000</p>
          </div>
          <button className="wishlist-btn"><i className="fas fa-heart"></i></button>
          <button className="cart-btn"><i className="fas fa-plus"></i></button>
        </div>
      </div>
    </div>
  );
}

export default Categories;
