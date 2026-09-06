import "./TrustSection.css";

function TrustSection() {
  return (
    <section className="trust-section">

      {/* TRUSTED */}
      <div className="trust-item">

        <div className="trust-icon">
          🛡️
        </div>

        <div className="trust-content">
          <h3>Trusted & Reliable</h3>
          <p>Smart care you can trust</p>
        </div>

      </div>


      {/* SAVE TIME */}
      <div className="trust-item">

        <div className="trust-icon">
          ⚡
        </div>

        <div className="trust-content">
          <h3>Saves Time & Money</h3>
          <p>Avoid unnecessary repairs</p>
        </div>

      </div>


      {/* ECO */}
      <div className="trust-item">

        <div className="trust-icon">
          🌱
        </div>

        <div className="trust-content">
          <h3>Eco Friendly</h3>
          <p>Extend your appliance life</p>
        </div>

      </div>

    </section>
  );
}

export default TrustSection;