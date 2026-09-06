import "./ChatbotButton.css";

function ChatbotButton({ setPage }) {
  return (
    <button
      className="chatbot-button"
      onClick={() => setPage("chatbot")}
      aria-label="Open HomeFix Chatbot"
      title="HomeFix Assistant"
    >
      <span className="chatbot-icon">💬</span>
    </button>
  );
}

export default ChatbotButton;