import { useState } from "react";
import axios from "axios";
import "./Register.css";

function Register({ setPage }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();

    if (!name.trim()) {
      alert("Please enter your name.");
      return;
    }

    if (!password.trim()) {
      alert("Please enter a password.");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/auth/register",
        {
          name: name.trim(),
          password: password
        }
      );

      console.log("Register response:", response.data);

      alert("Account created successfully! Please login.");

      setPage("login");

    } catch (error) {
      console.error("Register error:", error);

      alert(
        error.response?.data?.detail ||
        "Unable to create account. Please try again."
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="register-page">

      <div className="register-card">

        {/* HOME ICON */}
        <div className="register-icon">
          🏠
        </div>

        {/* BADGE */}
        <span className="register-badge">
          HOMEFIX SMART CARE
        </span>

        {/* TITLE */}
        <h1>
          Create Your Account
        </h1>

        <p className="register-intro">
          Create your HomeFix account to get started
        </p>

        <form onSubmit={handleRegister}>

          {/* NAME */}
          <div className="register-field">
            <label>Name</label>

            <input
              type="text"
              placeholder="Enter your name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          {/* PASSWORD */}
          <div className="password-wrapper">
  <input
    type={showPassword ? "text" : "password"}
    placeholder="Create a password"
    value={password}
    onChange={(e) => setPassword(e.target.value)}
  />

  <button
    type="button"
    className="password-toggle"
    onClick={() => setShowPassword(!showPassword)}
  >
    {showPassword ? "👁️" : "🙈"}
  </button>
</div>

          {/* CREATE ACCOUNT */}
          <button
            type="submit"
            className="register-submit-btn"
            disabled={loading}
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>

        </form>

        {/* LOGIN */}
        <p className="register-login-text">
          Already have an account?

          <button
            type="button"
            className="register-login-btn"
            onClick={() => setPage("login")}
          >
            Login
          </button>
        </p>

        {/* BACK */}
        <button
          type="button"
          className="register-back-btn"
          onClick={() => setPage("home")}
        >
          ← Back to Home
        </button>

      </div>

    </div>
  );
}

export default Register;