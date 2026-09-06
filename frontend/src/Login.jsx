import { useState } from "react";
import axios from "axios";
import "./Login.css";

function Login({ setPage, onLoginSuccess }) {

  // ==========================================
  // STATES
  // ==========================================

  const [loginType, setLoginType] = useState("email");

  const [email, setEmail] = useState("");

  const [mobile, setMobile] = useState("");

  const [countryCode, setCountryCode] = useState("+91");

  const [otp, setOtp] = useState("");

  const [otpSent, setOtpSent] = useState(false);

  const [loading, setLoading] = useState(false);


  // ==========================================
  // COUNTRY LIST
  // ==========================================

  const countries = [
    { name: "India", code: "+91", flag: "🇮🇳" },
    { name: "United States", code: "+1", flag: "🇺🇸" },
    { name: "United Kingdom", code: "+44", flag: "🇬🇧" },
    { name: "United Arab Emirates", code: "+971", flag: "🇦🇪" },
    { name: "Australia", code: "+61", flag: "🇦🇺" },
    { name: "Canada", code: "+1", flag: "🇨🇦" },
    { name: "Singapore", code: "+65", flag: "🇸🇬" },
    { name: "Germany", code: "+49", flag: "🇩🇪" },
    { name: "France", code: "+33", flag: "🇫🇷" },
    { name: "Japan", code: "+81", flag: "🇯🇵" },
    { name: "Saudi Arabia", code: "+966", flag: "🇸🇦" },
    { name: "Qatar", code: "+974", flag: "🇶🇦" }
  ];


  // ==========================================
  // SEND OTP
  // ==========================================

  const handleSendOtp = async (e) => {

    e.preventDefault();

    // ========================================
    // EMAIL VALIDATION
    // ========================================

    if (loginType === "email") {

      const cleanEmail = email.trim();

      if (!cleanEmail) {

        alert("Please enter your email address.");

        return;
      }

      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleanEmail)) {

        alert("Please enter a valid email address.");

        return;
      }

    }


    // ========================================
    // MOBILE VALIDATION
    // ========================================

    if (loginType === "mobile") {

      const cleanMobile = mobile.trim();

      if (!cleanMobile) {

        alert("Please enter your mobile number.");

        return;
      }

      if (!/^\d+$/.test(cleanMobile)) {

        alert("Please enter numbers only.");

        return;
      }


      // INDIA

      if (countryCode === "+91") {

        if (cleanMobile.length !== 10) {

          alert(
            "Please enter a valid 10-digit Indian mobile number."
          );

          return;
        }

      }


      // OTHER COUNTRIES

      else {

        if (
          cleanMobile.length < 7 ||
          cleanMobile.length > 15
        ) {

          alert(
            "Please enter a valid mobile number."
          );

          return;
        }

      }

    }


    // ========================================
    // START LOADING
    // ========================================

    setLoading(true);


    try {

      let data;


      // ======================================
      // EMAIL DATA
      // ======================================

      if (loginType === "email") {

        data = {

          type: "email",

          email: email.trim(),

          mobile: null,

          country_code: null

        };

      }


      // ======================================
      // MOBILE DATA
      // ======================================

      else {

        data = {

          type: "mobile",

          email: null,

          mobile: mobile.trim(),

          country_code: countryCode

        };

      }


      console.log(
        "Sending OTP request:",
        data
      );


      // ======================================
      // BACKEND REQUEST
      // ======================================

      const response = await axios.post(

        "http://127.0.0.1:8000/api/auth/send-otp",

        data

      );


      console.log(
        "Send OTP response:",
        response.data
      );


      // ======================================
      // SUCCESS
      // ======================================

      if (response.data.success) {

        setOtpSent(true);

        setOtp("");

        alert(
          loginType === "email"
            ? "OTP sent successfully. Please check your email."
            : "OTP sent successfully. Please check your mobile phone."
        );

      }

      else {

        alert(
          response.data.message ||
          "Unable to send OTP."
        );

      }

    }


    // ========================================
    // ERROR
    // ========================================

    catch (error) {

      console.error(
        "Send OTP error:",
        error
      );


      if (error.response) {

        alert(

          error.response.data?.detail ||

          "Unable to send OTP."

        );

      }

      else {

        alert(
          "Unable to connect to HomeFix server."
        );

      }

    }


    finally {

      setLoading(false);

    }

  };


  // ==========================================
  // VERIFY OTP
  // ==========================================

  const handleVerifyOtp = async (e) => {

    e.preventDefault();


    // ========================================
    // OTP VALIDATION
    // ========================================

    if (!otp.trim()) {

      alert("Please enter the OTP.");

      return;
    }


    if (!/^\d{6}$/.test(otp)) {

      alert(
        "OTP must contain exactly 6 digits."
      );

      return;
    }


    setLoading(true);


    try {

      let data;


      // ======================================
      // EMAIL
      // ======================================

      if (loginType === "email") {

        data = {

          type: "email",

          email: email.trim(),

          mobile: null,

          country_code: null,

          otp: otp.trim()

        };

      }


      // ======================================
      // MOBILE
      // ======================================

      else {

        data = {

          type: "mobile",

          email: null,

          mobile: mobile.trim(),

          country_code: countryCode,

          otp: otp.trim()

        };

      }


      console.log(
        "Verifying OTP:",
        data
      );


      // ======================================
      // BACKEND REQUEST
      // ======================================

      const response = await axios.post(

        "http://127.0.0.1:8000/api/auth/verify-otp",

        data

      );


      console.log(
        "Verify OTP response:",
        response.data
      );


      // ======================================
      // LOGIN SUCCESS
      // ======================================

      if (response.data.success) {

        // Save login status

        localStorage.setItem(
          "isLoggedIn",
          "true"
        );


        // Save login type

        localStorage.setItem(
          "loginType",
          loginType
        );


        // ====================================
        // SAVE EMAIL
        // ====================================

        if (loginType === "email") {

          localStorage.setItem(
            "userEmail",
            email.trim()
          );

        }


        // ====================================
        // SAVE MOBILE
        // ====================================

        else {

          localStorage.setItem(
            "userMobile",
            countryCode + mobile.trim()
          );

        }


        // ====================================
        // SUCCESS POPUP
        // ====================================

        alert(
          "Login successful!"
        );


        // ====================================
        // GO TO DASHBOARD
        // ====================================

        if (onLoginSuccess) {

          onLoginSuccess();

        }

        else {

          setPage("dashboard");

        }

      }


      // ======================================
      // INVALID OTP
      // ======================================

      else {

        alert(
          response.data.message ||
          "Invalid OTP. Please try again."
        );

      }

    }


    // ========================================
    // ERROR
    // ========================================

    catch (error) {

      console.error(
        "Verify OTP error:",
        error
      );


      if (error.response) {

        alert(

          error.response.data?.detail ||

          "Invalid OTP. Please try again."

        );

      }

      else {

        alert(
          "Unable to connect to HomeFix server."
        );

      }

    }


    finally {

      setLoading(false);

    }

  };


  // ==========================================
  // RESEND OTP
  // ==========================================

  const handleResendOtp = async () => {

    setOtp("");

    await handleSendOtp({
      preventDefault: () => {}
    });

  };


  // ==========================================
  // CHANGE EMAIL / MOBILE
  // ==========================================

  const handleChangeLogin = () => {

    setOtpSent(false);

    setOtp("");

  };


  // ==========================================
  // CHANGE LOGIN TYPE
  // ==========================================

  const handleLoginTypeChange = (type) => {

    setLoginType(type);

    setOtpSent(false);

    setOtp("");

  };


  // ==========================================
  // GET OTP DESTINATION
  // ==========================================

  const getDestination = () => {

    if (loginType === "email") {

      return `📧 ${email}`;

    }

    return `📱 ${countryCode} ${mobile}`;

  };


  // ==========================================
  // PAGE
  // ==========================================

  return (

    <div className="login-page">

      <div className="login-card">


        {/* ================================= */}
        {/* ICON */}
        {/* ================================= */}

        <div className="login-icon">
          🏠
        </div>


        {/* ================================= */}
        {/* BADGE */}
        {/* ================================= */}

        <span className="login-badge">
          HOMEFIX SMART CARE
        </span>


        {/* ================================= */}
        {/* TITLE */}
        {/* ================================= */}

        <h1>
          Welcome <span>Back</span>
        </h1>


        {/* ================================= */}
        {/* INTRO */}
        {/* ================================= */}

        <p className="login-intro">

          {otpSent

            ? `Enter the OTP sent to your ${
                loginType === "email"
                  ? "email."
                  : "mobile number."
              }`

            : "Login to manage your appliances and get smart repair assistance."

          }

        </p>


        {/* ================================= */}
        {/* OTP SCREEN */}
        {/* ================================= */}

        {otpSent ? (

          <form onSubmit={handleVerifyOtp}>


            {/* OTP DESTINATION */}

            <div className="otp-destination">

              {getDestination()}

            </div>


            {/* OTP FIELD */}

            <div className="login-field">

              <label>
                Enter OTP
              </label>

              <input
                type="text"
                inputMode="numeric"
                maxLength="6"
                placeholder="Enter 6-digit OTP"
                value={otp}
                onChange={(e) =>
                  setOtp(
                    e.target.value.replace(
                      /\D/g,
                      ""
                    )
                  )
                }
                autoFocus
              />

            </div>


            {/* VERIFY */}

            <button
              type="submit"
              className="login-submit-btn"
              disabled={loading}
            >

              {loading
                ? "Verifying..."
                : "Verify OTP →"
              }

            </button>


            {/* RESEND */}

            <button
              type="button"
              className="resend-otp-btn"
              onClick={handleResendOtp}
              disabled={loading}
            >

              ↻ Resend OTP

            </button>


            {/* CHANGE */}

            <button
              type="button"
              className="login-back-btn"
              onClick={handleChangeLogin}
            >

              ← Change Email / Mobile

            </button>

          </form>

        )


        : (


          /* ================================= */
          /* EMAIL / MOBILE SCREEN */
          /* ================================= */

          <form onSubmit={handleSendOtp}>


            {/* ================================= */}
            {/* TABS */}
            {/* ================================= */}

            <div className="login-type-tabs">


              {/* EMAIL */}

              <button
                type="button"
                className={
                  loginType === "email"
                    ? "login-type active"
                    : "login-type"
                }
                onClick={() =>
                  handleLoginTypeChange(
                    "email"
                  )
                }
              >

                📧 Email

              </button>


              {/* MOBILE */}

              <button
                type="button"
                className={
                  loginType === "mobile"
                    ? "login-type active"
                    : "login-type"
                }
                onClick={() =>
                  handleLoginTypeChange(
                    "mobile"
                  )
                }
              >

                📱 Mobile

              </button>

            </div>


            {/* ================================= */}
            {/* EMAIL */}
            {/* ================================= */}

            {loginType === "email" && (

              <div className="login-field">

                <label>
                  Email Address
                </label>

                <input
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) =>
                    setEmail(e.target.value)
                  }
                />

              </div>

            )}


            {/* ================================= */}
            {/* MOBILE */}
            {/* ================================= */}

            {loginType === "mobile" && (

              <div className="login-field">

                <label>
                  Mobile Number
                </label>

                <div className="mobile-input-row">

                  {/* COUNTRY CODE */}

                  <select
                    className="mobile-country-code"
                    value={countryCode}
                    onChange={(e) => {

                      setCountryCode(
                        e.target.value
                      );

                      setMobile("");

                    }}
                  >

                    {countries.map(
                      (country, index) => (

                        <option
                          key={index}
                          value={country.code}
                        >
                          {country.code}
                        </option>

                      )
                    )}

                  </select>


                  {/* MOBILE NUMBER */}

                  <input
                    className="mobile-number-input"
                    type="tel"
                    inputMode="numeric"
                    placeholder="Enter mobile number"
                    value={mobile}
                    maxLength={
                      countryCode === "+91"
                        ? 10
                        : 15
                    }
                    onChange={(e) =>
                      setMobile(
                        e.target.value.replace(
                          /\D/g,
                          ""
                        )
                      )
                    }
                  />

                </div>

              </div>

            )}


            {/* ================================= */}
            {/* SEND OTP */}
            {/* ================================= */}

            <button
              type="submit"
              className="login-submit-btn"
              disabled={loading}
            >

              {loading
                ? "Sending OTP..."
                : "Send OTP →"
              }

            </button>


            {/* ================================= */}
            {/* BACK */}
            {/* ================================= */}

            <button
              type="button"
              className="login-back-btn"
              onClick={() =>
                setPage("home")
              }
            >

              ← Back to Home

            </button>

          </form>

        )}

      </div>

    </div>

  );

}

export default Login;