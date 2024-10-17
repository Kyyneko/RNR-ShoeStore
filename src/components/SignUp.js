import React from 'react';
import './SignUp.css'; // buat file CSS untuk styling

function SignUp() {
  return (
    <div className="signup-container">
      <div className="signup-content">
        <div className="signup-image">
          <img src="/images/adidas_trail_run.png" alt="Shoes" /> {/* Sesuaikan gambar */}
        </div>
        <div className="signup-form">
          <h2>Sign Up Now</h2>
          
          <form>
            <input type="text" placeholder="Username" required />
            <input type="password" placeholder="Password" required />
            <input type="email" placeholder="Phone Number or Email" required />
            <button type="submit" className="signup-button-1">Sign Up</button>
          </form>

          <p className='sign-in'>Already have a Roots&Routes account? <a href="/signin">Log In</a></p>
          <p className="terms">
            By signing up, I agree to Roots&Routes's <a href="/">Terms & Conditions</a> and <a href="/">Privacy Policy</a>.
          </p>
        </div>
      </div>
    </div>
  );
}

export default SignUp;
