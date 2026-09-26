import { useEffect, useState } from "react";
import axios from "axios";

import HomePage from "./HomePage";
import Login from "./Login";
import Register from "./Register";

import Diagnosis from "./components/Diagnosis";
import DiagnosisResult from "./components/DiagnosisResult";
import SafeSecure from "./components/SafeSecure";
import AddAppliance from "./components/AddAppliance";
import Chatbot from "./components/chatbot";

import "./App.css";
import "./components/Appliances.css";
import "./components/Diagnosis.css";


function App() {

  // ==========================================
  // PAGE
  // ==========================================

  const [page, setPage] = useState("home");


  // ==========================================
  // LOGIN STATUS
  // ==========================================

  const [isLoggedIn, setIsLoggedIn] = useState(
    localStorage.getItem("isLoggedIn") === "true"
  );

  const [showProfile, setShowProfile] = useState(false);


  // ==========================================
  // APPLIANCES
  // ==========================================

  const [appliances, setAppliances] = useState([]);

  const [selectedAppliance, setSelectedAppliance] = useState(null);


  // ==========================================
  // DIAGNOSIS
  // ==========================================

  const [diagnosis, setDiagnosis] = useState(null);

  const [previousPage, setPreviousPage] = useState("dashboard");


  const startNewDiagnosis = () => {
    setDiagnosis(null);
    setPage("diagnosis");
  };


  // ==========================================
  // PROTECTED PAGES
  // ==========================================

  const protectedPages = [
    "dashboard",
    "appliances",
    "add",
    "diagnosis",
    "diagnosis-result",
    "history",
    "secure"
  ];


  // ==========================================
  // NAVIGATION
  // ==========================================

  const navigate = (targetPage) => {

    if (
      protectedPages.includes(targetPage) &&
      !isLoggedIn
    ) {
      setPage("login");
      return;
    }

    setPage(targetPage);
  };


  // ==========================================
  // LOAD APPLIANCES
  // ==========================================

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/api/appliances")

      .then((response) => {

        const backendAppliances = response.data;

        const localAppliances =
          JSON.parse(
            localStorage.getItem("homefix_appliances")
          ) || [];

        setAppliances([
          ...backendAppliances,
          ...localAppliances
        ]);

      })

      .catch((error) => {

        console.error(
          "Error loading appliances:",
          error
        );

        const localAppliances =
          JSON.parse(
            localStorage.getItem("homefix_appliances")
          ) || [];

        setAppliances(localAppliances);

      });

  }, [page]);


  // ==========================================
  // HOME / WELCOME PAGE
  // ==========================================

  if (page === "home") {

    return (
      <HomePage
        setPage={navigate}
      />
    );

  }


  // ==========================================
  // LOGIN
  // ==========================================

  if (page === "login") {

    return (
      <Login
        setPage={navigate}

        onLoginSuccess={() => {

          setIsLoggedIn(true);

          setPage("dashboard");

        }}

      />
    );

  }


  // ==========================================
  // REGISTER
  // ==========================================

  if (page === "register") {

    return (
      <Register
        setPage={navigate}
      />
    );

  }


  // ==========================================
  // DASHBOARD
  // ==========================================

  if (page === "dashboard") {

    return (

      <div className="dashboard-page">

        <div className="dashboard-container">


          {/* ==========================================
              PROFILE
          ========================================== */}

          <div className="profile-area">

            <button
              className="profile-button"

              onClick={() =>
                setShowProfile(!showProfile)
              }

              title="Profile"
            >
              👤
            </button>


            {showProfile && (

              <div className="profile-popup">

                <h3>
                  👤 User Profile
                </h3>


                <div className="profile-info">

                  <p>
                    👤 {localStorage.getItem("userName") || "User"}
                  </p>

                </div>


                <button
                  className="profile-logout"

                  onClick={() => {

                    localStorage.removeItem(
                      "isLoggedIn"
                    );

                    localStorage.removeItem(
                      "userName"
                    );

                    localStorage.removeItem(
                      "loginType"
                    );

                    localStorage.removeItem(
                      "userEmail"
                    );

                    localStorage.removeItem(
                      "userMobile"
                    );

                    setIsLoggedIn(false);

                    setShowProfile(false);

                    setPage("home");

                  }}
                >
                  🚪 Logout
                </button>

              </div>

            )}

          </div>


          <span className="dashboard-badge">
            HOMEFIX SMART CARE
          </span>


          <h1>

            Your Appliances.

            <br />

            <span>
              Smarter Care.
            </span>

          </h1>


          <p className="dashboard-intro">

            Manage your appliances and get smart
            assistance whenever you need it.

          </p>


          {/* ==========================================
              SMART DIAGNOSIS
          ========================================== */}

          <button
            className="dashboard-main-card"

            onClick={() => {

              setPreviousPage("dashboard");

              navigate("diagnosis");

            }}
          >

            <span className="dashboard-card-icon">
              🩺
            </span>


            <span>

              <strong>
                Smart Diagnosis
              </strong>

              <small>
                Find appliance problems quickly
              </small>

            </span>


            <span className="dashboard-arrow">
              →
            </span>

          </button>


          {/* ==========================================
              SECOND ROW
          ========================================== */}

          <div className="dashboard-grid">


            <button
              onClick={() =>
                navigate("secure")
              }
            >

              <span>
                🛡️
              </span>

              <strong>
                Safe & Secure
              </strong>

              <small>
                Protect your appliance data
              </small>

            </button>


            <button
              onClick={() =>
                navigate("history")
              }
            >

              <span>
                📋
              </span>

              <strong>
                Track History
              </strong>

              <small>
                View diagnosis history
              </small>

            </button>


          </div>


          {/* ==========================================
              THIRD ROW
          ========================================== */}

          <div className="dashboard-grid">


            <button
              onClick={() =>
                navigate("appliances")
              }
            >

              <span>
                📦
              </span>

              <strong>
                My Appliances
              </strong>

              <small>
                View your appliances
              </small>

            </button>


            <button
              onClick={() =>
                navigate("add")
              }
            >

              <span>
                ➕
              </span>

              <strong>
                Add Appliance
              </strong>

              <small>
                Register a new appliance
              </small>

            </button>


          </div>


          {/* ==========================================
              CHATBOT
          ========================================== */}

          <button
            className="dashboard-chatbot"

            onClick={() =>
              navigate("chatbot")
            }

            title="HomeFix Assistant"
          >
            💬
          </button>

        </div>

      </div>

    );

  }


  // ==========================================
  // MY APPLIANCES
  // ==========================================

  if (page === "appliances") {

    return (

      <div className="appliances-page">

        <div className="appliances-container">


          <span className="appliances-badge">
            HOMEFIX SMART CARE
          </span>


          <h1>
            My <span>Appliances</span>
          </h1>


          <p className="appliances-intro">
            Select an appliance to diagnose or manage it.
          </p>


          {/* BACK TO DASHBOARD */}

          <button
            className="appliances-back-btn"

            onClick={() =>
              navigate("dashboard")
            }
          >
            ← Back to Dashboard
          </button>


          {/* ==========================================
              APPLIANCES
          ========================================== */}

          <div className="appliances-grid">


            {appliances.length === 0 ? (

              <div className="no-appliances">

                <div className="no-appliances-icon">
                  📦
                </div>


                <h3>
                  No Appliances Yet
                </h3>


                <p>
                  Add your first appliance to get started.
                </p>


                <button
                  onClick={() =>
                    navigate("add")
                  }
                >
                  ＋ Add Appliance
                </button>

              </div>

            ) : (

              appliances.map(
                (appliance, index) => (

                  <div

                    key={
                      appliance.id ||
                      `local-${index}`
                    }

                    className="appliance-card"

                    onClick={() => {

                      setSelectedAppliance(
                        appliance
                      );

                      setPreviousPage(
                        "appliances"
                      );

                      navigate("diagnosis");

                    }}

                  >


                    <div className="appliance-card-icon">

                      {getApplianceIcon(
                        appliance.type ||
                        appliance.category
                      )}

                    </div>


                    <div className="appliance-card-info">

                      <h3>
                        {appliance.name}
                      </h3>


                      <span>
                        {
                          appliance.type ||
                          appliance.category
                        }
                      </span>


                      {appliance.brand && (

                        <small>
                          {appliance.brand}
                        </small>

                      )}


                      {appliance.model && (

                        <small>
                          Model: {appliance.model}
                        </small>

                      )}

                    </div>


                    <div className="appliance-card-arrow">
                      →
                    </div>


                  </div>

                )

              )

            )}

          </div>


          {/* ADD NEW */}

          <button
            className="add-new-appliance-btn"

            onClick={() =>
              navigate("add")
            }
          >
            ＋ Add New Appliance
          </button>


        </div>

      </div>

    );

  }


  // ==========================================
  // ADD APPLIANCE
  // ==========================================

  if (page === "add") {

    return (
      <AddAppliance
        setPage={navigate}
      />
    );

  }


  // ==========================================
  // SMART DIAGNOSIS
  // ==========================================

  if (page === "diagnosis") {

    return (

      <Diagnosis

        setPage={setPage}

        selectedAppliance={
          selectedAppliance
        }

        setDiagnosis={
          setDiagnosis
        }

        previousSymptom={
          diagnosis?.symptom || ""
        }

      />

    );

  }


  // ==========================================
  // DIAGNOSIS RESULT
  // ==========================================

  if (page === "diagnosis-result") {

    return (

      <DiagnosisResult

        result={
          diagnosis
        }

        setPage={
          setPage
        }

        previousPage={
          previousPage
        }

        startNewDiagnosis={
          startNewDiagnosis
        }

      />

    );

  }


  // ==========================================
  // SAFE & SECURE
  // ==========================================

  if (page === "secure") {

    return (

      <SafeSecure
        setPage={navigate}
      />

    );

  }


  // ==========================================
  // TRACK HISTORY
  // ==========================================

  if (page === "history") {

    return (

      <div className="history-page">

        <div className="history-container">


          <span className="history-badge">
            HOMEFIX SMART CARE
          </span>


          <div className="history-icon">
            📋
          </div>


          <h1>
            Track <span>History</span>
          </h1>


          <p className="history-intro">
            Keep track of your appliance diagnosis and repair activity.
          </p>


          {/* EMPTY HISTORY */}

          <div className="history-empty">

            <div className="history-empty-icon">
              📝
            </div>


            <h3>
              No Diagnosis History Yet
            </h3>


            <p>
              Your diagnosis history will appear here
              after you diagnose an appliance.
            </p>


            <button
              onClick={() =>
                navigate("appliances")
              }
            >
              📦 View My Appliances
            </button>

          </div>


          {/* BACK */}

          <button
            className="history-back-btn"

            onClick={() =>
              navigate("dashboard")
            }
          >
            ← Back to Dashboard
          </button>


        </div>

      </div>

    );

  }


  // ==========================================
  // CHATBOT
  // ==========================================

  if (page === "chatbot") {

    return (

      <Chatbot
        setPage={navigate}
      />

    );

  }


  // ==========================================
  // FALLBACK
  // ==========================================

  return (

    <HomePage
      setPage={navigate}
    />

  );

}


// ==========================================
// APPLIANCE ICON
// ==========================================

function getApplianceIcon(type) {

  switch (type?.toLowerCase()) {

    case "refrigerator":
      return "🧊";

    case "washing machine":
      return "🧺";

    case "ac":
    case "air conditioner":
      return "❄️";

    case "tv":
      return "📺";

    case "microwave":
      return "🍳";

    case "fan":
      return "🌀";

    case "oven":
      return "🔥";

    case "dishwasher":
      return "🍽️";

    case "water heater":
      return "💧";

    case "vacuum cleaner":
      return "🧹";

    default:
      return "🔧";

  }

}


export default App;