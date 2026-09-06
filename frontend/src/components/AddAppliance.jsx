import { useState } from "react";
import "./AddAppliance.css";

function AddAppliance({ setPage }) {
  const [name, setName] = useState("");
  const [type, setType] = useState("Refrigerator");
  const [brand, setBrand] = useState("");
  const [model, setModel] = useState("");

  const handleSave = () => {
    if (!name.trim()) {
      alert("Please enter an appliance name.");
      return;
    }

    const appliance = {
      id: Date.now(),
      name: name,
      type: type,
      brand: brand,
      model: model,
    };

    const existing =
      JSON.parse(localStorage.getItem("homefix_appliances")) || [];

    localStorage.setItem(
      "homefix_appliances",
      JSON.stringify([...existing, appliance])
    );

    alert("Appliance added successfully!");

    setPage("appliances");
  };

  return (
    <div className="add-appliance-page">

      <div className="add-appliance-card">

        <div className="add-appliance-icon">
          ➕
        </div>

        <span className="add-appliance-badge">
          HOMEFIX SMART CARE
        </span>

        <h1>
          Add <span>Appliance</span>
        </h1>

        <p className="add-appliance-intro">
          Add your appliance details to manage and diagnose it easily.
        </p>


        {/* APPLIANCE NAME */}

        <div className="form-group">
          <label>Appliance Name</label>

          <input
            type="text"
            placeholder="Example: My Refrigerator"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>


        {/* TYPE */}

        <div className="form-group">
          <label>Appliance Type</label>

          <select
            value={type}
            onChange={(e) => setType(e.target.value)}
          >
            <option>Refrigerator</option>
            <option>Washing Machine</option>
            <option>AC</option>
            <option>TV</option>
            <option>Microwave</option>
            <option>Fan</option>
            <option>Oven</option>
            <option>Dishwasher</option>
            <option>Water Heater</option>
            <option>Vacuum Cleaner</option>
          </select>
        </div>


        {/* BRAND */}

        <div className="form-group">
          <label>Brand</label>

          <input
            type="text"
            placeholder="Example: Samsung"
            value={brand}
            onChange={(e) => setBrand(e.target.value)}
          />
        </div>


        {/* MODEL */}

        <div className="form-group">
          <label>Model Number</label>

          <input
            type="text"
            placeholder="Example: RT28T3922S8"
            value={model}
            onChange={(e) => setModel(e.target.value)}
          />
        </div>


        {/* BUTTONS */}

        <div className="add-appliance-buttons">

          <button
            className="save-appliance-btn"
            onClick={handleSave}
          >
            ✓ Save Appliance
          </button>

          <button
            className="back-appliance-btn"
            onClick={() => setPage("home")}
          >
            ← Back to Home
          </button>

        </div>

      </div>

    </div>
  );
}

export default AddAppliance;