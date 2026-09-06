import "./HomePage.css";

function HomePage({ setPage }) {

  return (
    <div className="welcome-page">

      <div className="welcome-card">

        {/* =========================================
            HERO SECTION
        ========================================= */}

        <div className="welcome-hero">

          {/* LEFT SIDE */}

          <div className="welcome-content">

            <span className="welcome-badge">
              SMART APPLIANCE CARE
            </span>

            <h1>
              Your Appliances.
              <br />
              <span>Smarter Care.</span>
            </h1>

            <p>
              Diagnose appliance problems, manage your appliances,
              and get smart solutions — all in one place.
            </p>


            {/* =========================================
                LOGIN / REGISTER / CHATBOT
            ========================================= */}

            <div className="welcome-actions">

              {/* LOGIN */}

              <button
                className="welcome-login"
                onClick={() => setPage("login")}
              >
                🔐 Login
              </button>


              {/* REGISTER */}

              <button
                className="welcome-register"
                onClick={() => setPage("register")}
              >
                🆕 New Register
              </button>


              {/* CHATBOT */}

              <button
                className="welcome-chatbot"
                onClick={() => setPage("chatbot")}
                title="HomeFix Chatbot"
              >
                🤖
              </button>

            </div>

          </div>


          {/* =========================================
              APPLIANCE ORBIT
          ========================================= */}

          <div className="appliance-orbit">

            <div className="orbit-ring"></div>


            {/* HOMEFIX CENTER */}

            <div className="homefix-center">

              <div className="homefix-house">
                🏠
              </div>

              <strong>
                HOMEFIX
              </strong>

              <span>
                SMART CARE
              </span>

            </div>


            {/* REFRIGERATOR */}

            <div className="orbit-item refrigerator">

              <div>
                🧊
              </div>

              <span>
                Refrigerator
              </span>

            </div>


            {/* AC */}

            <div className="orbit-item ac">

              <div>
                ❄️
              </div>

              <span>
                AC
              </span>

            </div>


            {/* FAN */}

            <div className="orbit-item fan">

              <div>
                🌀
              </div>

              <span>
                Fan
              </span>

            </div>


            {/* TV */}

            <div className="orbit-item tv">

              <div>
                📺
              </div>

              <span>
                TV
              </span>

            </div>


            {/* WASHING MACHINE */}

            <div className="orbit-item washing">

              <div>
                🧺
              </div>

              <span>
                Washing Machine
              </span>

            </div>


            {/* MICROWAVE */}

            <div className="orbit-item microwave">

              <div>
                🍳
              </div>

              <span>
                Microwave
              </span>

            </div>

          </div>

        </div>


        {/* =========================================
            FEATURE CARDS
        ========================================= */}

        <div className="feature-grid">


          {/* =========================================
              TRUSTED & RELIABLE
          ========================================= */}

          <div className="feature-card trusted-card">

            <div className="feature-icon">
              🛡️
            </div>

            <div className="feature-text">

              <h3>
                Trusted & Reliable
              </h3>

              <p>
                Smart care you can trust for your
                appliances.
              </p>

            </div>

            <span className="feature-arrow">
              →
            </span>

          </div>


          {/* =========================================
              SAVES TIME & MONEY
          ========================================= */}

          <div className="feature-card time-card">

            <div className="feature-icon">
              ⚡
            </div>

            <div className="feature-text">

              <h3>
                Saves Time & Money
              </h3>

              <p>
                Avoid unnecessary repairs and save more.
              </p>

            </div>

            <span className="feature-arrow">
              →
            </span>

          </div>


          {/* =========================================
              ECO FRIENDLY
          ========================================= */}

          <div className="feature-card eco-card">

            <div className="feature-icon">
              🌱
            </div>

            <div className="feature-text">

              <h3>
                Eco Friendly
              </h3>

              <p>
                Extend your appliance life and care
                for the planet.
              </p>

            </div>

            <span className="feature-arrow">
              →
            </span>

          </div>

        </div>


        {/* =========================================
            FLOATING CHATBOT
        ========================================= */}

        <button
          className="welcome-chatbot-icon"
          onClick={() => setPage("chatbot")}
          title="HomeFix Chatbot"
        >
          💬
        </button>


      </div>

    </div>
  );
}

export default HomePage;