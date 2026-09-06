import "./FeatureCards.css";

function FeatureCards({ setPage }) {
  return (
    <section className="feature-section">

      {/* ROW 1 */}

      <div
        className="feature-card diagnosis-card"
        onClick={() => setPage("diagnosis")}
      >
        <div className="feature-icon">
          🔍
        </div>

        <div className="feature-content">
          <h3>Smart Diagnosis</h3>

          <p>
            Describe your appliance problem and get
            smart troubleshooting guidance.
          </p>
        </div>

        <span className="feature-arrow">→</span>
      </div>


      <div
        className="feature-card secure-card"
        onClick={() => setPage("secure")}
      >
        <div className="feature-icon">
          🛡️
        </div>

        <div className="feature-content">
          <h3>Safe & Secure</h3>

          <p>
            Your appliance information is handled
            securely and responsibly.
          </p>
        </div>

        <span className="feature-arrow">→</span>
      </div>


      <div className="feature-card history-card">
        <div className="feature-icon">
          📋
        </div>

        <div className="feature-content">
          <h3>Track History</h3>

          <p>
            View your previous appliance diagnoses
            and repair information.
          </p>
        </div>

        <span className="feature-arrow">→</span>
      </div>


      {/* ROW 2 */}

      <div className="feature-card trusted-card">

        <div className="feature-icon">
          🛡️
        </div>

        <div className="feature-content">
          <h3>Trusted & Reliable</h3>

          <p>
            Smart care you can trust for your appliances.
          </p>
        </div>

        <span className="feature-arrow">→</span>

      </div>


      <div className="feature-card money-card">

        <div className="feature-icon">
          ⚡
        </div>

        <div className="feature-content">
          <h3>Saves Time & Money</h3>

          <p>
            Avoid unnecessary repairs and save more.
          </p>
        </div>

        <span className="feature-arrow">→</span>

      </div>


      <div className="feature-card eco-card">

        <div className="feature-icon">
          🌱
        </div>

        <div className="feature-content">
          <h3>Eco Friendly</h3>

          <p>
            Extend your appliance life and care
            for the planet.
          </p>
        </div>

        <span className="feature-arrow">→</span>

      </div>

    </section>
  );
}

export default FeatureCards;