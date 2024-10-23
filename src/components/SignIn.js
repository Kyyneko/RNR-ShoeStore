import React from 'react';
import './SignIn.css'; 

function SignIn() {
  return (
    <div className="signin-form-container">
      <h2 className="modal-title">Sign In</h2>
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
  );
}

export default SignIn;
