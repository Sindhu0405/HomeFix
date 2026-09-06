import "./SafeSecure.css";

function SafeSecure({ setPage }) {
  return (
    <div className="safe-secure-page">

      <div className="security-card">

        <div className="security-icon">
          🛡️
        </div>

        <span className="security-badge">
          HOMEFIX SECURITY
        </span>

        <h1>
          Safe <span>&</span> Secure
        </h1>

        <p className="security-intro">
          Your appliance information is handled securely
          and responsibly.
        </p>

        <div className="security-features">

          <div className="security-item">
            <div>🔐</div>
            <section>
              <h3>Protected Information</h3>
              <p>
                Your appliance details are kept protected
                while using HomeFix.
              </p>
            </section>
          </div>

          <div className="security-item">
            <div>🛡️</div>
            <section>
              <h3>Secure Access</h3>
              <p>
                Your information is designed to be accessed
                only through the HomeFix application.
              </p>
            </section>
          </div>

          <div className="security-item">
            <div>✓</div>
            <section>
              <h3>Responsible Data Handling</h3>
              <p>
                We aim to keep your appliance information
                safe and responsibly managed.
              </p>
            </section>
          </div>

        </div>

        <button
          className="security-back-btn"
          onClick={() => setPage("home")}
        >
          ← Back to Home
        </button>

      </div>

    </div>
  );
}

export default SafeSecure;