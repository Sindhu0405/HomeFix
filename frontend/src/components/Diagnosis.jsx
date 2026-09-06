import { useRef, useState } from "react";
import axios from "axios";
import "./Diagnosis.css";

function Diagnosis({ setPage,selectedAppliance,setDiagnosis,previousSymptom
}) {

  const [symptom, setSymptom] = useState(previousSymptom || "");
  const [loading, setLoading] = useState(false);

  // Reference to problem textbox
  const problemInputRef = useRef(null);


  // ==========================================
  // START DIAGNOSIS
  // ==========================================

  const handleDiagnosis = async () => {

    if (!symptom.trim()) {
      alert("Please describe your appliance problem.");
      problemInputRef.current?.focus();
      return;
    }

    setLoading(true);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/diagnosis",
        {
          category: selectedAppliance?.type || "Refrigerator",
          symptom: symptom,
        }
      );

      console.log("Diagnosis response:", response.data);

      // Save result in App.jsx
      setDiagnosis(response.data);

      // Go to result page
      setPage("diagnosis-result");

    } catch (error) {

      console.error("Diagnosis error:", error);

      alert(
        "Unable to get diagnosis. Please check if the backend is running."
      );

    } finally {

      setLoading(false);

    }
  };


  // ==========================================
  // IDENTIFY PROBLEM
  // ==========================================

  const handleIdentifyProblem = () => {

    problemInputRef.current?.focus();

  };


  // ==========================================
  // SMART TROUBLESHOOTING
  // ==========================================

  const handleTroubleshooting = () => {

    if (!symptom.trim()) {

      alert(
        "Please describe your appliance problem first."
      );

      problemInputRef.current?.focus();

      return;
    }

    handleDiagnosis();

  };


  // ==========================================
  // REPAIR GUIDANCE
  // ==========================================

  const handleRepairGuidance = () => {

    if (!symptom.trim()) {

      alert(
        "Please describe your appliance problem first."
      );

      problemInputRef.current?.focus();

      return;
    }

    handleDiagnosis();

  };


  return (

    <div className="diagnosis-page">

      <div className="diagnosis-card">

        {/* ICON */}
        <div className="diagnosis-icon">
          🔍
        </div>


        {/* BADGE */}
        <span className="diagnosis-badge">
          HOMEFIX SMART CARE
        </span>


        {/* TITLE */}
        <h1>
          Smart <span>Diagnosis</span>
        </h1>


        {/* SELECTED APPLIANCE */}
        {selectedAppliance && (

          <div className="selected-appliance">
            🔧 {selectedAppliance.name}
          </div>

        )}


        {/* DESCRIPTION */}
        <p className="diagnosis-intro">
          Describe your appliance problem and get
          smart troubleshooting guidance.
        </p>


        {/* PROBLEM INPUT */}
        <div className="problem-section">

          <h3>
            What's wrong with your appliance?
          </h3>

          <textarea
            ref={problemInputRef}
            className="problem-input"
            placeholder="Example: My refrigerator is not cooling..."
            rows="4"
            value={symptom}
            onChange={(e) => setSymptom(e.target.value)}
          />

        </div>


        {/* FEATURES */}
        <div className="diagnosis-features">


          {/* IDENTIFY */}
          <div
            className="diagnosis-item"
            onClick={handleIdentifyProblem}
            role="button"
            tabIndex="0"
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                handleIdentifyProblem();
              }
            }}
          >

            <div className="diagnosis-item-icon">
              🔎
            </div>

            <div>

              <h3>
                Identify the Problem
              </h3>

              <p>
                Tell us what is wrong with your appliance.
              </p>

            </div>

          </div>


          {/* SMART TROUBLESHOOTING */}
          <div
            className="diagnosis-item"
            onClick={handleTroubleshooting}
            role="button"
            tabIndex="0"
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                handleTroubleshooting();
              }
            }}
          >

            <div className="diagnosis-item-icon">
              ⚡
            </div>

            <div>

              <h3>
                Smart Troubleshooting
              </h3>

              <p>
                Get helpful guidance to understand the issue.
              </p>

            </div>

          </div>


          {/* REPAIR GUIDANCE */}
          <div
            className="diagnosis-item"
            onClick={handleRepairGuidance}
            role="button"
            tabIndex="0"
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                handleRepairGuidance();
              }
            }}
          >

            <div className="diagnosis-item-icon">
              🛠️
            </div>

            <div>

              <h3>
                Repair Guidance
              </h3>

              <p>
                Find the next step for your appliance problem.
              </p>

            </div>

          </div>


        </div>


        {/* BUTTONS */}
        <div className="diagnosis-buttons">

          <button
            className="diagnosis-start-btn"
            onClick={handleDiagnosis}
            disabled={loading}
          >

            {loading
              ? "Diagnosing..."
              : "Start Diagnosis →"
            }

          </button>


          <button
            className="diagnosis-back-btn"
            onClick={() => setPage("dashboard")}
          >
            ← Back to Dashboard
          </button>

        </div>


      </div>

    </div>

  );
}

export default Diagnosis;