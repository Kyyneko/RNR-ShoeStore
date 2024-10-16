import React, { useState } from 'react';
import './SignIn.css'; 

function SignIn() {
  // State untuk menampilkan atau menyembunyikan modal
  const [isModalOpen, setModalOpen] = useState(false);

  // Fungsi untuk membuka modal Sign In
  const openModal = () => {
    setModalOpen(true);
  };

  // Fungsi untuk menutup modal Sign In
  const closeModal = () => {
    setModalOpen(false);
  };

  return (
    <div className="signin-page">
      {/* Tombol Sign In */}
      <button className="signin-btn" onClick={openModal}>
        Sign In
      </button>

      {/* Modal Sign In */}
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <h2 className="modal-title">Sign In</h2>
            <button className="close-btn" onClick={closeModal}>
              &times;
            </button>

            {/* Form Sign In */}
            <form className="signin-form">
              <div className="input-group">
                <label htmlFor="username">Username</label>
                <input type="text" id="username" placeholder="Username" />
              </div>

              <div className="input-group">
                <label htmlFor="password">Password</label>
                <input type="password" id="password" placeholder="Password" />
              </div>

              <div className="actions">
                <p className="help-link">Need Help?</p>
                <button type="submit" className="submit-btn">Log In</button>
              </div>
            </form>
            <p className="register-link">Register</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default SignIn;
