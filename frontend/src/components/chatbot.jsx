import { useEffect, useRef, useState } from "react";
import "./Chatbot.css";

function Chatbot({ setPage }) {

  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! 👋 I'm your HomeFix app assistant. How can I help you?"
    }
  ]);

  const messagesEndRef = useRef(null);


  // ==========================================
  // AUTO SCROLL TO LATEST MESSAGE
  // ==========================================

  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);


  // ==========================================
  // BOT REPLY
  // ==========================================

  const getBotReply = (userMessage) => {

    const text = userMessage.toLowerCase().trim();


    // GREETING
    if (
      text === "hi" ||
      text === "hello" ||
      text === "hey" ||
      text === "hii" ||
      text === "helo"
    ) {

      return (
        "Hello! 👋 Welcome to HomeFix Smart Care.\n\n" +
        "I can help you with:\n" +
        "🔐 Login\n" +
        "🔑 OTP\n" +
        "➕ Add Appliance\n" +
        "📦 My Appliances\n" +
        "🩺 Smart Diagnosis\n" +
        "📋 Track History\n" +
        "🚪 Logout\n" +
        "🏠 Home navigation"
      );

    }


    // ==========================================
    // LOGIN PROBLEM
    // ==========================================

    if (
      text.includes("login problem") ||
      text.includes("login issue") ||
      text.includes("login not working") ||
      text.includes("can't login") ||
      text.includes("cannot login") ||
      text.includes("unable to login") ||
      text.includes("how can i login") ||
      text.includes("how do i login") ||
      text.includes("how to login") ||
      text.includes("log in") ||
      text.includes("sign in") ||
      text.includes("login")
    ) {

      return (
        "🔐 Here's how to login to HomeFix:\n\n" +
        "1️⃣ Open the Login page.\n" +
        "2️⃣ Choose Email or Mobile.\n" +
        "3️⃣ Enter your email or mobile number.\n" +
        "4️⃣ Click 'Send OTP'.\n" +
        "5️⃣ Check your email or phone for the OTP.\n" +
        "6️⃣ Enter the 6-digit OTP.\n" +
        "7️⃣ Click 'Verify OTP'.\n\n" +
        "If you still cannot login, check your details and try again."
      );

    }


    // ==========================================
    // OTP PROBLEM
    // ==========================================

    if (
      text.includes("otp not received") ||
      text.includes("didn't receive otp") ||
      text.includes("did not receive otp") ||
      text.includes("otp not coming") ||
      text.includes("otp not getting") ||
      text.includes("otp problem") ||
      text.includes("otp issue") ||
      text.includes("no otp")
    ) {

      return (
        "🔑 If you are not receiving the OTP:\n\n" +
        "1️⃣ Check that your email/mobile number is correct.\n" +
        "2️⃣ Check your SMS inbox or email inbox.\n" +
        "3️⃣ Wait a few seconds.\n" +
        "4️⃣ Check your internet/network connection.\n" +
        "5️⃣ Click 'Resend OTP' if available.\n\n" +
        "Then enter the new 6-digit OTP."
      );

    }


    // GENERAL OTP
    if (
      text.includes("otp") ||
      text.includes("verification code") ||
      text.includes("verify")
    ) {

      return (
        "🔑 OTP Verification:\n\n" +
        "Enter the 6-digit OTP sent to your registered email or mobile number.\n\n" +
        "Then click 'Verify OTP'.\n\n" +
        "If you didn't receive the OTP, use 'Resend OTP'."
      );

    }


    // ==========================================
    // MOBILE LOGIN
    // ==========================================

    if (
      text.includes("mobile login") ||
      text.includes("login with mobile") ||
      text.includes("phone login") ||
      text.includes("mobile number")
    ) {

      return (
        "📱 To login using your mobile number:\n\n" +
        "1️⃣ Open the Login page.\n" +
        "2️⃣ Select 'Mobile'.\n" +
        "3️⃣ Select your country code.\n" +
        "4️⃣ Enter your mobile number.\n" +
        "5️⃣ Click 'Send OTP'.\n" +
        "6️⃣ Enter the OTP received on your phone.\n" +
        "7️⃣ Click 'Verify OTP'."
      );

    }


    // ==========================================
    // EMAIL LOGIN
    // ==========================================

    if (
      text.includes("email login") ||
      text.includes("login with email") ||
      text.includes("email address")
    ) {

      return (
        "📧 To login using your email:\n\n" +
        "1️⃣ Open the Login page.\n" +
        "2️⃣ Select 'Email'.\n" +
        "3️⃣ Enter your email address.\n" +
        "4️⃣ Click 'Send OTP'.\n" +
        "5️⃣ Check your email for the OTP.\n" +
        "6️⃣ Enter the OTP.\n" +
        "7️⃣ Click 'Verify OTP'."
      );

    }


    // ==========================================
    // ADD APPLIANCE
    // ==========================================

    if (
      text.includes("add appliance") ||
      text.includes("add an appliance") ||
      text.includes("adding appliance") ||
      text.includes("add my appliance") ||
      text.includes("new appliance") ||
      text.includes("how can i add") ||
      text.includes("how do i add")
    ) {

      return (
        "➕ To add a new appliance:\n\n" +
        "1️⃣ Open the Home page.\n" +
        "2️⃣ Select 'My Appliances'.\n" +
        "3️⃣ Click 'Add New Appliance'.\n" +
        "4️⃣ Enter the appliance name.\n" +
        "5️⃣ Select the appliance type/category.\n" +
        "6️⃣ Enter the brand.\n" +
        "7️⃣ Enter the model if available.\n" +
        "8️⃣ Enter the purchase year.\n" +
        "9️⃣ Add warranty information if available.\n" +
        "🔟 Add notes if needed.\n" +
        "1️⃣1️⃣ Click 'Save Appliance'.\n\n" +
        "Your appliance should then appear under 'My Appliances'."
      );

    }


    // ==========================================
    // APPLIANCE NOT SHOWING
    // ==========================================

    if (
      text.includes("appliance not showing") ||
      text.includes("appliance is not showing") ||
      text.includes("appliance missing") ||
      text.includes("can't see my appliance") ||
      text.includes("cannot see my appliance") ||
      text.includes("appliance not visible")
    ) {

      return (
        "📦 If your appliance is not showing:\n\n" +
        "1️⃣ Open 'My Appliances'.\n" +
        "2️⃣ Refresh the page.\n" +
        "3️⃣ Check whether the appliance was saved.\n" +
        "4️⃣ Make sure all required fields were entered.\n" +
        "5️⃣ Try adding the appliance again.\n\n" +
        "If the problem continues, check your connection and try again."
      );

    }


    // ==========================================
    // MY APPLIANCES
    // ==========================================

    if (
      text.includes("my appliances") ||
      text.includes("view appliances") ||
      text.includes("see my appliances") ||
      text.includes("where are my appliances")
    ) {

      return (
        "📦 To view your appliances:\n\n" +
        "1️⃣ Go to the Home page.\n" +
        "2️⃣ Open 'My Appliances'.\n\n" +
        "Here you can see all appliances you have added to HomeFix."
      );

    }


    // ==========================================
    // SMART DIAGNOSIS
    // ==========================================

    if (
      text.includes("smart diagnosis") ||
      text.includes("diagnosis") ||
      text.includes("diagnose")
    ) {

      return (
        "🩺 Smart Diagnosis helps you identify possible appliance problems.\n\n" +
        "1️⃣ Open Smart Diagnosis from the Home page.\n" +
        "2️⃣ Select your appliance.\n" +
        "3️⃣ Follow the questions.\n" +
        "4️⃣ Enter the symptoms or problem.\n" +
        "5️⃣ Submit the diagnosis.\n\n" +
        "HomeFix will then show the diagnosis result."
      );

    }


    // ==========================================
    // HISTORY
    // ==========================================

    if (
      text.includes("track history") ||
      text.includes("history") ||
      text.includes("previous diagnosis")
    ) {

      return (
        "📋 To view your history:\n\n" +
        "Open 'Track History' from the Home page.\n\n" +
        "You can view your previous diagnosis and repair-related information there."
      );

    }


    // ==========================================
    // LOGOUT
    // ==========================================

    if (
      text.includes("logout") ||
      text.includes("log out") ||
      text.includes("sign out")
    ) {

      return (
        "🚪 To logout from HomeFix:\n\n" +
        "1️⃣ Open your account/profile section.\n" +
        "2️⃣ Select 'Logout'.\n\n" +
        "You will be signed out of the application."
      );

    }


    // ==========================================
    // HOME
    // ==========================================

    if (
      text.includes("home page") ||
      text.includes("go home") ||
      text.includes("back home")
    ) {

      return (
        "🏠 To return to the Home page, click the 'Back to Home' button."
      );

    }


    // ==========================================
    // FEATURES
    // ==========================================

    if (
      text.includes("features") ||
      text.includes("what can i do") ||
      text.includes("what can i use")
    ) {

      return (
        "✨ HomeFix features include:\n\n" +
        "🏠 Home\n" +
        "📦 My Appliances\n" +
        "➕ Add Appliance\n" +
        "🩺 Smart Diagnosis\n" +
        "📋 Track History\n" +
        "🔐 Login & OTP\n" +
        "🤖 HomeFix Chatbot"
      );

    }


    // ==========================================
    // ABOUT HOMEFIX
    // ==========================================

    if (
      text.includes("what is homefix") ||
      text.includes("what is this app") ||
      text.includes("about homefix")
    ) {

      return (
        "🏠 HomeFix is a smart home-appliance management application.\n\n" +
        "You can add and manage appliances, use Smart Diagnosis, " +
        "view history, login securely with OTP, and get help through the chatbot."
      );

    }


    // ==========================================
    // HELP
    // ==========================================

    if (
      text === "help" ||
      text.includes("how to use") ||
      text.includes("what should i do")
    ) {

      return (
        "😊 I can help you with HomeFix.\n\n" +
        "Try asking:\n\n" +
        "• How do I login?\n" +
        "• I didn't receive OTP\n" +
        "• How can I add my appliance?\n" +
        "• Where can I see my appliances?\n" +
        "• What is Smart Diagnosis?\n" +
        "• How do I see my history?\n" +
        "• How do I logout?"
      );

    }


    // ==========================================
    // THANK YOU
    // ==========================================

    if (
      text.includes("thank") ||
      text.includes("thanks")
    ) {

      return "You're welcome! 😊 I'm happy to help you with HomeFix.";

    }


    // ==========================================
    // DEFAULT
    // ==========================================

    return (
      "🤖 I'm your HomeFix app assistant.\n\n" +
      "I can help you with Login, OTP, adding appliances, " +
      "My Appliances, Smart Diagnosis, Track History, Logout, " +
      "and navigating the HomeFix application.\n\n" +
      "Try asking:\n" +
      "👉 How can I add my appliance?\n" +
      "👉 How do I login?\n" +
      "👉 I didn't receive OTP"
    );

  };


  // ==========================================
  // SEND MESSAGE
  // ==========================================

  const handleSend = (e) => {

    e.preventDefault();

    const userText = message.trim();

    if (!userText) {
      return;
    }


    // Add customer message

    setMessages((previousMessages) => [
      ...previousMessages,
      {
        sender: "user",
        text: userText
      }
    ]);


    // Clear input

    setMessage("");


    // Bot reply

    setTimeout(() => {

      const botReply = getBotReply(userText);

      setMessages((previousMessages) => [
        ...previousMessages,
        {
          sender: "bot",
          text: botReply
        }
      ]);

    }, 400);

  };


  // ==========================================
  // PAGE
  // ==========================================

  return (

    <div className="chatbot-page">

      <div className="chatbot-card">


        {/* HEADER */}

        <div className="chatbot-header">

          <div className="chatbot-icon">
            🤖
          </div>

          <div>

            <span className="chatbot-badge">
              HOMEFIX SMART CARE
            </span>

            <h1>
              HomeFix <span>Chatbot</span>
            </h1>

            <p>
              Smart app assistance
            </p>

          </div>

        </div>


        {/* CHAT MESSAGES */}

        <div className="chatbot-messages">

          {messages.map((msg, index) => (

            <div
              key={index}
              className={
                msg.sender === "user"
                  ? "chat-message user-message"
                  : "chat-message bot-message"
              }
            >

              <div className="message-icon">
                {msg.sender === "user" ? "👤" : "🤖"}
              </div>

              <div className="message-bubble">

                {msg.text.split("\n").map((line, i) => (

                  <div key={i}>
                    {line || "\u00A0"}
                  </div>

                ))}

              </div>

            </div>

          ))}

          {/* Invisible element used for automatic scrolling */}

          <div ref={messagesEndRef} />

        </div>


        {/* INPUT */}

        <form
          className="chatbot-input"
          onSubmit={handleSend}
        >

          <input
            type="text"
            placeholder="Ask about HomeFix..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button type="submit">
            ➤
          </button>

        </form>


        {/* BACK */}

        <button
          type="button"
          className="chatbot-back"
          onClick={() => setPage("home")}
        >
          ← Back to Home
        </button>

      </div>

    </div>

  );

}

export default Chatbot;