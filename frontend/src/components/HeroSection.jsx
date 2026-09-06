import "./HeroSection.css";

function HeroSection({ setPage }) {
  return (
    <section className="hero-section">

      {/* LEFT CONTENT */}
      <div className="hero-content">

        <span className="hero-badge">
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

        <div className="hero-buttons">

          <button
            className="hero-primary-btn"
            onClick={() => setPage("appliances")}
          >
            📋 My Appliances
          </button>

          <button
            className="hero-secondary-btn"
            onClick={() => setPage("add")}
          >
            ＋ Add Appliance
          </button>

        </div>

      </div>


      {/* RIGHT APPLIANCE AREA */}
      <div className="hero-visual">

        <div className="appliance-orbit"></div>

        {/* HOMEFIX CENTER */}
        <div className="homefix-center">
          <div className="homefix-icon">
            🏠
          </div>

          <strong>HOMEFIX</strong>
          <small>SMART CARE</small>
        </div>


        {/* REFRIGERATOR */}
        <div className="mini-appliance refrigerator">
          <div className="mini-icon">🧊</div>
          <span>Refrigerator</span>
        </div>


        {/* AC */}
        <div className="mini-appliance ac">
          <div className="mini-icon">❄️</div>
          <span>AC</span>
        </div>


        {/* TV */}
        <div className="mini-appliance tv">
          <div className="mini-icon">📺</div>
          <span>TV</span>
        </div>


        {/* WASHING MACHINE */}
        <div className="mini-appliance washing">
          <div className="mini-icon">🧺</div>
          <span>Washing Machine</span>
        </div>


        {/* MICROWAVE */}
        <div className="mini-appliance microwave">
          <div className="mini-icon">🍳</div>
          <span>Microwave</span>
        </div>


        {/* FAN */}
        <div className="mini-appliance fan">
          <div className="mini-icon">🌀</div>
          <span>Fan</span>
        </div>

      </div>

    </section>
  );
}

export default HeroSection;