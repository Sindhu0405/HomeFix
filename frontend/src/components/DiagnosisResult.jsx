import "./Diagnosis.css";

function DiagnosisResult({ result, setPage, previousPage, startNewDiagnosis }) {
  if (!result) {
    return (
      <div className="diagnosis-page">
        <div className="diagnosis-card">
          <h2>No diagnosis result found.</h2>

          <button
            className="diagnosis-back-btn"
            onClick={() => setPage("diagnosis")}
          >
            ← Back to Diagnosis
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="diagnosis-page">

      <div className="diagnosis-result-page">

        {/* HEADER */}
        <div className="result-icon">
          🔍
        </div>

        <span className="diagnosis-badge">
          HOMEFIX SMART CARE
        </span>

        <h1>
          Diagnosis <span>Result</span>
        </h1>

        <p className="result-subtitle">
          Here is the diagnosis based on the problem you described.
        </p>


        {/* PROBLEM */}
        <div className="result-section">

          <h2>📝 Reported Problem</h2>

          <div className="result-box">
            {result.symptom}
          </div>

        </div>


        {/* POSSIBLE CAUSES */}
        <div className="result-section">

          <h2>⚠️ Possible Causes</h2>

          <div className="cause-list">

            {result.possible_causes?.map((cause, index) => (

              <div className="cause-card" key={index}>

                <div className="cause-number">
                  {index + 1}
                </div>

                <div className="cause-content">

                  <h3>
                    {cause.cause}
                  </h3>

                  <p>
                    Likelihood: <strong>{cause.likelihood}</strong>
                  </p>

                </div>

              </div>

            ))}

          </div>

        </div>


        {/* SAFETY CHECKS */}
        <div className="result-section">

          <h2>🛡️ Safety Checks</h2>

          <div className="safety-list">

            {result.safe_checks?.map((check, index) => (

              <div className="safety-item" key={index}>

                <span>✓</span>

                <p>{check}</p>

              </div>

            ))}

          </div>

        </div>


        {/* REPAIR COST */}
        <div className="result-section">

          <h2>💰 Estimated Repair Cost</h2>

          <div className="repair-cost">

            {result.estimated_repair_range}

          </div>

        </div>
        {/* FIND NEARBY SERVICE SHOPS */}
<button
  className="find-shops-btn"
  onClick={() => {
    window.open(
      "https://www.google.com/maps/search/appliance+repair+shops+near+me",
      "_blank"
    );
  }}
>
  📍 Find Nearby Service Shops
</button>
        {/* ACTION BUTTONS */}
        <div className="result-buttons">

          <button
            className="diagnosis-start-btn"
            onClick={startNewDiagnosis}
          >
            ← New Diagnosis
          </button>

          <button
            className="diagnosis-back-btn"
            onClick={() => setPage("diagnosis")}
          >
            ← Back 
          </button>

        </div>

      </div>

    </div>
  );
}

export default DiagnosisResult;
