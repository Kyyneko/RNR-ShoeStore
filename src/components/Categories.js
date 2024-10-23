import React from 'react';
import { Link } from 'react-router-dom';
import './Categories.css';

function Categories() {
  const products = [
    { id: 1, name: 'NIKE-Air Lorem Ipsum', price: 1699000, image: '/images/sepatu2.png', category: 'Men Original' },
    { id: 2, name: 'ADIDAS Lorem Ipsum', price: 2699000, image: '/images/adidas_trail_run.png', category: 'Men Original' },
    { id: 3, name: 'NIKE Lorem Ipsum', price: 1899000, image: '/images/nike-air.png', category: 'Unisex Original' }
  ];

  return (
    <div className="categories-page">
      <h2 className="best-product-title">Best Product R&R</h2>
      <div className="search-container">
        <input type="text" placeholder="Cari di R&R" className="search-bar" />
      </div>

      <div className="product-grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <Link to={`/shoes/${product.id}`}>
              <img src={product.image} alt={product.name} className="product-image" />
              <div className="product-details">
                <span className="product-category">{product.category}</span>
                <h3 className="product-name">{product.name}</h3>
                <p className="product-price">{product.price.toLocaleString('id-ID', { style: 'currency', currency: 'IDR' })}</p>
              </div>
            </Link>
            <button className="wishlist-btn"><i className="fas fa-heart"></i></button>
            <button className="cart-btn"><i className="fas fa-plus"></i></button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Categories;
